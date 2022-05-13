import requests
import shutil
import os
import re


def file_list():
    path = '.'
    file_name_list = os.listdir(path)
    with open(path + "/" + "file_list.txt", "a") as f:
        for file_name in re.findall(r"\d+", str(file_name_list)):
            if len(file_name) == 8:
                f.write(file_name+"\n")


def check_url():
    global id
    head = {
        'User-Agent': '',
        'Cookie': ''
    }
    with open("file_list.txt") as f:
        ids = f.read().splitlines()
        for id in ids:
            response = requests.get(
                f'https://bbs.nga.cn/read.php?tid={id}', headers=head)
            if response.status_code == 403:
                with open('checked_url.txt', 'a') as new_f:
                    new_f.write(id+'\n')


def zip_remove():
    with open("checked_url.txt") as f:
        ids = f.read().splitlines()
        for id in ids:
            shutil.make_archive(f'/root/ngapost2md/{id}', 'zip', root_dir=f'{id}')
            print(f'POST{id} has archived')
            shutil.rmtree(f'{id}')
            print(f'removed folder{id}')


def main():
    file_list()
    check_url()
    zip_remove()
    

if __name__ == '__main__':
    main()
