import sys
import os

sys.path.append('/Users/bytedance/Desktop/learn/poem_yunlv/zhconv/dist/zhconv-1.4.1-py3.7.egg')
from zhconv import convert

def change(file):
    #change fanti to jianti
    oldpath = os.path.join('/Users/bytedance/Desktop/learn/poem_yunlv/chinese-poetry/json/',file)
    newpath = os.path.join('/Users/bytedance/Desktop/learn/poem_yunlv/poem_reduce/',file)
    with open(oldpath,'r') as fr:
        with open(newpath,'a+') as fw:
            for line in fr:
                newline = convert(line,'zh-cn')
                #print (newline)
                fw.write(newline)

if __name__ == '__main__':
    for root,dirs,files in os.walk('/Users/bytedance/Desktop/learn/poem_yunlv/chinese-poetry/json/'):
        for file in files:
            print (file)
            if r'.json' in str(file):
                change(file)
