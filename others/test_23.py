# 获取用户输入的十进制数字
decimal_number = int(input("请输入一个十进制数字: "))

# 使用hex函数将其转换为十六进制并打印结果
hexadecimal_number = hex(decimal_number)
print(f"十进制数字 {decimal_number} 转换为十六进制是 {hexadecimal_number}")
