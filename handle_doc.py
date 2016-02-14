# coding=utf-8

import os
import shutil
import json
import datetime
import time

root_dir = r'./exam_data'
des_dir = r'./data'
update_time = (2015, 12, 25, 0, 0, 0, 0, 0, 0)


def handle_doc():
    for i in os.listdir(root_dir):
        stu_dir = os.path.join(root_dir, i)
        if not os.path.isdir(stu_dir):
            continue
        for j in os.listdir(stu_dir):
            pro_dir = os.path.join(stu_dir, j)
            if os.path.isdir(pro_dir):
                ver = 0
                timestamp = .0
                try:
                    with open(os.path.join(pro_dir, '.status')) as fp:
                        status = json.load(fp)
                        try:
                            # print pro_dir, status
                            ver = status['main.c']['version']
                            timestamp = float(status['main.c']['mtime'])
                        except KeyError:
                            continue
                        except TypeError:
                            continue
                        # print datetime.datetime.fromtimestamp(timestamp)
                        # print timestamp
                        # print time.mktime(update_time)
                        if timestamp - time.mktime(update_time) > 0:
                            if not os.path.exists(os.path.join(des_dir, j)):
                                os.mkdir(os.path.join(des_dir, j))
                            shutil.copy2(os.path.join(pro_dir, 'main.c_'+str(ver)), os.path.join(os.path.join(des_dir, j), i)+'.c')
                except IOError:
                    print pro_dir
                    continue

if __name__ == '__main__':
    handle_doc()
