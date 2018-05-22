# 异常的完整语法
try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数 ："))
    # 使用8除以用户输入的整数并且退出
    result = 8 / num

    print(result)

except ValueError:
    print("请输入正确的整数")
    # 捕获未知错误
except Exception as result1:
    print("未知错误%s:" % result1)
else:
    print("尝试代码执行成功！")
finally:
    print("无论成功与否否会被执行")

print("-" * 50)
