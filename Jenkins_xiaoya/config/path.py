import os
path_dir = os.path.abspath(__file__)      #path路径
config_dir = os.path.dirname(path_dir)     #config路径
review_dir = os.path.dirname(config_dir)      #review路径
reports_dir = os.path.join(review_dir,"reports")    #reports路径
if not os.path.exists(reports_dir):     #如果reports目录不在，创建目录
    os.mkdir(reports_dir)
logs_dir = os.path.join(review_dir,"logs")     #logs路径
if not os.path.exists(logs_dir):      #如果logs目录不在，创建目录
    os.mkdir(logs_dir)
data_dir = os.path.join(review_dir,"data")
if not os.path.exists(data_dir):      #如果data目录不在，创建目录
    os.mkdir(data_dir)
cases_file = os.path.join(data_dir,"cases.xlsx")
if __name__ == '__main__':
    print(111)
    




