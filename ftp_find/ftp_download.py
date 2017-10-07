# -*- coding: utf-8 -*-

import ftplib
import os
import time

ftp = ftplib.FTP(host="202.120.38.11", user="public", passwd="public")
ftp.encoding = 'GB18030'

# set the dirname to be downloaded
dirname = "2016.09-2017.08研究生综合测评公示区"


def mkdir_if_not_exist(dir_):
    if not os.path.isdir(dir_):
        os.makedirs(dir_)


def download(dirname):
    mkdir_if_not_exist(dirname)
    os.chdir(dirname)
    ftp.cwd(dirname)

    print("==================================================")
    print("==> local: [{}]".format(os.getcwd()))
    print("==> ftp: [{}]".format(ftp.pwd()))

    filenames = ftp.mlsd()

    for filename in filenames:
        name = filename[0]
        print("==> name: [{}]".format(name))

        if filename[1]['type'] == 'dir':
            download(name)
        elif filename[1]['type'] == 'file':
            with open(name, 'wb') as fd:
                ftp.retrbinary('RETR ' + name,
                               fd.write)
        time.sleep(1)

    print("==========back to upper dir: [{}]==========".format(dirname))
    os.chdir('..')
    ftp.cwd('..')


if __name__ == '__main__':
    download(dirname)

