import os
file = os.path.abspath(__file__)    #文件地址
print(file)
file_dir = os.path.dirname(file)     #文件根目录
print(file_dir)
file_text = os.path.join(file_dir,"data","123.text")    #拼接文件
print(file_text)
print(type(file_text))
path_123 = os.path.join(file_dir,"data","123")    #拼接文件
print(path_123)
if not os.path.exists(path_123):   #创建目录
    os.mkdir(path_123)
else:
    print("目录已创建")
# os.mkdir(file_123)
f = open(file_text,mode="r",encoding="utf-8")
print(f.read())