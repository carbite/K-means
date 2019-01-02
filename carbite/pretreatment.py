#encoding=utf-8
import jieba
import jieba.posseg as pseg
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import re
from nltk.stem.porter import PorterStemmer

def pretreatment_C():

    for i in range(1,501):
        fn = open("data/ZH_Org/News_"+str(i)+"_Org_ZH.txt", "r") #要操作的文件
        f = open("data/ZH/News_"+str(i)+"_C.txt", "w+") #即将写入的文件
        for line in fn.readlines():
            line = line.replace("&nbsp;", "")#下面两步完成删除特殊字符
            line = ' '.join(re.findall(u'[(\u4e00-\u9fff)|(a-zA-Z)]+', unicode(line, 'utf-8')))
            # words=pseg.cut(line)#后面带着词性
            words = jieba.cut(line)#使用jieba分词工具完成中文分词
            # 读取停用词存入停用词数组中
            ZH_stop_word = []
            fn_stop = open("static/ZH_stop_word.txt", "r")  # 要操作的文件
            for line2 in fn_stop.readlines():
                ZH_stop_word.append(line2.strip().encode('utf8'))
            fn_stop.close()
            #删除中文停用词
            result = []
            for w in words:
                if w not in ZH_stop_word:
                    result.append(w)
            for r in result:
                f.write(str(r).strip().encode('utf8')+" ")
        print ("中文文章" + str(i) + "处理完毕")
        f.close()
        fn.close()
    return
def pretreatment_E():

    for i in range(1, 501):
        fn = open("data/E_Org/News_"+str(i)+"_Org_E.txt", "r") #要操作的文件
        f = open("data/E/News_"+str(i)+"_E.txt", "w+") #即将写入的文件
        for line in fn.readlines():
            line = line.replace("&nbsp;", "")#下面两步完成删除特殊字符
            line = ' '.join(re.findall(u'[(\u4e00-\u9fff)|(a-zA-Z)|(0-9)]+', unicode(line, 'utf-8')))
            tmp = line.split(" ")
            # 读取停用词存入停用词数组中
            E_stop_word = []
            fn_stop = open("static/E_stop_word.txt", "r")  # 要操作的文件
            for line2 in fn_stop.readlines():
                E_stop_word.append(line2.strip().encode('utf8'))
            fn_stop.close()
            #删除英文停用词
            result = []
            for t in tmp:
                if t not in E_stop_word:
                    t = PorterStemmer().stem(str(t))#实现Porter Stemmer
                    result.append(t)
            for r in result:
                f.write(str(r).strip().encode('utf8')+" ")
        print ("英文文章" + str(i) + "处理完毕")
        f.close()
        fn.close()

    return
pretreatment_C()
pretreatment_E()