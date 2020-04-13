#!/usr/bin/env python3
import os, sys, time
chunksize = int(1024 * 1024)
j = '='
# 对文件进行切割
def split(srcfile, todir, chunksize=chunksize):
    if not os.path.exists(todir):
        os.mkdir(todir)
    else:
        for fname in os.listdir(todir):
            os.remove(os.path.join(todir, fname))
    # partnum = 0
    # fullsize = os.path.getsize(srcfile)  # 计算被切割文件的大小
    # filesize = 0
    # f_input = open(srcfile, 'rb')
    while True:
        filesize += chunksize
        chunk = f_input.read(chunksize)  # 以chunksize大小从被切割文件中读取
        if not chunk:
            print('分割完成')
            break
        partnum += 1
        filename = os.path.join(todir, ('part%04d' % partnum))  # 标记块的编号
        fileobj = open(filename, 'wb')
        fileobj.write(chunk)
        fileobj.close()
    f_input.close()
    assert partnum <= 9999
    return partnum



