
str = "锅"
print(f"{str}的unicode编码为：{hex(ord(str))}")
print(f"{str}的UTF-8编码为：{str.encode('UTF-8')}")