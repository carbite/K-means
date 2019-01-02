# coding=utf-8
import os
import codecs

def merge_file(path, resName, nameend):
    if os.path.exists(resName):
        os.remove(resName)
    result = codecs.open(resName, 'w', 'utf-8')

    num = 1
    while num <= 500:
        fileName = path + "News_"+ str(num) + nameend
        source = open(fileName, 'r')
        line = source.readline()
        line = line.strip('\n')
        line = line.strip('\r')

        while line != "":
            line = unicode(line, "utf-8")
            line = line.replace('\n', ' ')
            line = line.replace('\r', ' ')
            result.write(line + ' ')
            line = source.readline()
        else:
            print 'End file: ' + str(num)
            result.write('\r\n')
            source.close()
        num = num + 1

    else:
        print 'End All'
        result.close()

merge_file("data/E/","data/E.txt","_E.txt")
merge_file("data/ZH/","data/C.txt","_C.txt")