#!-*-coding:utf-8-*-
# 打开文件
file = open("README", 'r', encoding='UTF-8')
# 按行读取
while True:
    text = file.readline()
    # 判断是否读取到内容
    if not text:
        break
    print(text)

file.close()
