import sys
import os
import json
import re

class Sentence:

    def __init__(self):
        self.all_sentences5 = {}
        self.all_sentences7 = {}
        self.yuns = {}
        self.path = '/Users/bytedance/Desktop/learn/poem_yunlv/poem_reduce/'

    def is_all_chinese(self,strs):
        for _char in strs:
            if not '\u4e00' <= _char <= '\u9fa5':
                return False
        return True

    def get_files(self,path):
        for root,dirs,files in os.walk(path):
            for file in files:
                if r'poet.' in str(file):
                    file_path = os.path.join(path,file)
                    self.get_poets(file_path)

    def get_poets(self,file_path):
        with open(file_path,'r') as f:
            json_string = json.load(f)
            for element in json_string:
                for paragraphs in element["paragraphs"]:
                    res = re.split(r'，|。',paragraphs)
                    for item in res:
                        if self.is_all_chinese(item):
                            if(len(item)==5):
                                yun = self.get_yun(item,self.yuns)
                                if(yun in self.all_sentences5.keys()):
                                    self.all_sentences5[yun].append(item)
                                else:
                                    self.all_sentences5[yun] = [item]
                            if(len(item)==7):
                                yun = self.get_yun(item,self.yuns)
                                if(yun in self.all_sentences7.keys()):
                                    self.all_sentences7[yun].append(item)
                                else:
                                    self.all_sentences7[yun] = [item]
    def get_all_yuns(self):
        with open('./../resource/yunlv/14yun.txt','r') as f:
            for line in f:
                strs = re.split(r"：　　",line)
                self.yuns[strs[1][:-1]] = strs[0]
    def get_yun(self,context,yuns):
        char = context[-1:]
        for key in yuns:
            if char in key:
                return yuns[key]
                break

#单文件做事
#这个文件纯读json好了，读出来两个数组，一个装5言诗的句子，一个装7言的
#还是每个韵读出两个数组好一点
# if __name__ == '__main__':
#     # get_files(path)
#     # print(params5)
#     # print(params7)
#     get_all_yuns()
#     get_poets(path+'poet.song.1000.json')
#     print (all_sentences5)