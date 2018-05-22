# _*_coding:utf-8_*_
# 1.打开文件
# file = open("README", encoding='UTF-8')
# with open("README", 'r', encoding='UTF-8') as file:
#     # 2.读取文件
#     text = file.read()
#     print(text)
file = open("README", 'r', encoding='UTF-8')
text = file.read()
print(text)
# 文件指针的概念，当第一次打开文件时，通常文件指针会指向文件的开始位置，当执行read方法后，文件指针会移动到读取内容的末尾
print(len(text))
print("-" * 50)
text = file.read()
print(text)
print(len(text))
print("-" * 50)

# 3.关闭文件
file.close()
