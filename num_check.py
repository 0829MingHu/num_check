import os
import shutil

num=0
apath=r"/home/chenj0g/rgb_flow/rgbflow"#1

s=set()
flag=False
for curdir,roots,files in os.walk(apath):
    if flag==False:
        flag=True
        continue
    s.add(curdir.split('/')[-1])
m=set()
for i in s:
    num1=0
    num2=0
    num3=0
    for curdir,roots,files in os.walk(apath+'/'+i):
        for file in files:
            if 'flow_x' in file:
                num1=num1+1
            if 'flow_y' in file:
                num2=num2+1
            if 'img_' in file:
                num3=num3+1
    if not num1==num2==num3:
        m.add(i)
print(m)
