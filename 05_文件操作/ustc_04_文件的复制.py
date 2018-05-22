# -*-coding:utf-8-*-
# 1.打开
file_read = open("README", 'r', encoding='UTF-8')
file_write = open("README 复件", 'w')
# 2.读 写
text = file_read.read()
file_write.write(text)
# 3.关闭文件
file_read.close()
file_write.close()
