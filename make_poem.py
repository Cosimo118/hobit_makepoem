import re
import random
import sys
all_sentence = {}

def get_sentence(context,yuns):
    char = context[-1:]
    for key in yuns:
        if char in key:
            #print (context+" "+yuns[key])
            if(yuns[key] in all_sentence.keys()):
                all_sentence[yuns[key]].append(context)
            else:
                all_sentence[yuns[key]] = [context]
            break

def get_yun(context,yuns):
    char = context[-1:]
    for key in yuns:
        if char in key:
            return yuns[key]
            break

def main(target_word,target_nums):
    yuns = {}
    with open('/Users/bytedance/Desktop/learn/poem_yunlv/14yun.txt','r') as f:
        for line in f:
            strs = re.split(r"：　　",line)
            yuns[strs[1][:-1]] = strs[0]

    #中文
    p2 = re.compile(r'[^\u4e00-\u9fa5]')
    with open('/Users/bytedance/Desktop/learn/poem_yunlv/poem_test.txt','r') as f:
        poem = f.read()
        words = p2.split(poem)
    for word in words:
        if word is not '':
            get_sentence(word,yuns)
    #到这里，已经拿到了k-v的所有唐诗三百首里的句子，下面，给一个字，按照这个字的韵，攒一句诗
    target_yun = get_yun(target_word,yuns)[:-1]
    #target_yun = "七尤"
    target_yun_first = target_yun+"平"
    target_yun_qian = target_yun+"仄"
    target_yun_hou = target_yun+"平"

    target_poem = {}
    words = set()
    for i in range (1,9):
        if i==1:
            flag = 1
            while(flag==1):
                target_poem[i] = random.choice(all_sentence[target_yun_first])
                if(len(target_poem[i]) == target_nums):
                    words.add(target_poem[i][-1:])
                    flag = 0
        elif i%2==0:
            flag = 1
            while(flag==1):
                target_poem[i] = random.choice(all_sentence[target_yun_hou])
                if(target_poem[i][-1:] not in words)&(len(target_poem[i]) == target_nums):
                    words.add(target_poem[i][-1:])
                    flag = 0
        else:
            flag = 1
            while(flag==1):
                target_poem[i] = random.choice(all_sentence[target_yun_qian])
                if(target_poem[i][-1:] not in words)&(len(target_poem[i]) == target_nums):
                    words.add(target_poem[i][-1:])
                    flag = 0
                    
    for i in range(1,9):
        if i%2==1:
            print(target_poem[i]+",")
        else:
            print(target_poem[i]+"。\n")

if __name__ =="__main__":
    target_word = "米"
    target_nums = 7
    main(target_word,target_nums)
