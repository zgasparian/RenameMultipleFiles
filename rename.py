
import os
import re
os.chdir(r'C:\Users\PC-USR\PycharmProjects\Images')
# print(os.getcwd())
for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title,f_num = f_name.split('-')

    f_num = re.sub(r'[( )]','',f_num)
    f_num = re.sub(r'Copy','',f_num)
    f_num= f_num.strip().zfill(2)
    f_title= f_title.replace(" ","")
    # print(f'{f_title}-{f_num}{f_ext}')
    new_name=f'{f_title}-{f_num}{f_ext}'

    os.rename(f,new_name)
