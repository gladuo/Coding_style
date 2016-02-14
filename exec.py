# coding=utf-8

import os
import cal

ROOT_DIR = './res_data'
DES_FILE = './data.out'


def exe():
    with open(DES_FILE, "w") as f:
        f.write("UID\tCourse\tWhiteSpace\tLastLine\tIndent\n")
    for course in os.listdir(ROOT_DIR):
        course_dir = os.path.join(ROOT_DIR, course)
        if not os.path.isdir(course_dir):
            continue
        for student in os.listdir(course_dir):
            student_file = os.path.join(course_dir, student)
            if os.path.isdir(student_file):
                continue
            if student == '.DS_Store':
                continue
            uid = filter(str.isdigit, student)
            print student_file
            with open(DES_FILE, "a+") as f:
                f.write(str(uid)+'\t'+str(course)+'\t'+str(cal.ws_fscore(student_file))+'\t'+str(cal.ln_fscore(student_file))+'\t'+str(cal.in_fscore(student_file))+'\n')


if __name__ == '__main__':
    exe()
