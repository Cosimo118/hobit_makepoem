import re

def get_yun(context,yuns):
    char = context[-1:]
    for key in yuns:
        if char in key:
            print (context+" "+yuns[key])
            break

if __name__ =="__main__":
    yuns = {}
    with open('14yun.txt','r') as f:
        for line in f:
            strs = re.split(r"：　　",line)
            yuns[strs[1][:-1]] = strs[0]

    #中文
    p2 = re.compile(r'[^\u4e00-\u9fa5]')
    with open('poem_test.txt','r') as f:
        poem = f.read()
        words = p2.split(poem)
    for word in words:
        get_yun(word,yuns)