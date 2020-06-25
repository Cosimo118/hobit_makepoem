from get_all_sentence import Sentence
import re
import random
import sys


def get_all_poems(sentence):
    sentence.get_all_yuns()
    #sentence.get_files(sentence.path)
    sentence.get_poets(sentence.path+'poet.song.1000.json')
    #拿到所有两个sentence了,self.all_sentences5 = {}；self.all_sentences7 = {}
    #key是韵，value是诗句的list

def make_poems(target_word,target_nums,sentence):
    target_yun = sentence.get_yun(target_word,sentence.yuns)[:-1]
    #target_yun = "七尤"
    target_yun_ping = target_yun+"平"
    target_yun_ze = target_yun+"仄"
    target_poem = {}
    words = set()
    
    for i in range (1,9):
        if i==1:
            if(target_nums==7):
                target_poem[i] = random.choice(sentence.all_sentences7[target_yun_ping])
            else:
                target_poem[i] = random.choice(sentence.all_sentences5[target_yun_ping])
            for char in target_poem[i]:
                words.add(char)
        elif i%2==0:
            while 1:
                flag = 1
                if(target_nums==7):
                    target_poem[i] = random.choice(sentence.all_sentences7[target_yun_ping])
                else:
                    target_poem[i] = random.choice(sentence.all_sentences5[target_yun_ping])
                for char in target_poem[i]:
                    if char in words:
                        flag =0
                if(flag ==1):
                    for char in target_poem[i]:
                        words.add(char)
                    break
        else:
            while 1:
                flag = 1
                if(target_nums==7):
                    target_poem[i] = random.choice(sentence.all_sentences7[target_yun_ze])
                else:
                    target_poem[i] = random.choice(sentence.all_sentences5[target_yun_ze])
                for char in target_poem[i]:
                    if char in words:
                        flag =0
                if(flag ==1):
                    for char in target_poem[i]:
                        words.add(char)
                    break
                    
    for i in range(0,4):
        print(target_poem[i*2+1]+","+target_poem[(i+1)*2]+"。")
    print("\n")

sentence = Sentence()
get_all_poems(sentence)
make_poems("端",7,sentence)
make_poems("午",5,sentence)
make_poems("快",5,sentence)
make_poems("乐",7,sentence)