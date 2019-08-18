import os
# 新建文件夹
def mkdir(path):
	folder = os.path.exists(path)

	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
		print("new folder creates")
 
	else:
		print ("folder exists")
file_path = 'C:/Users/cly/Desktop/20190817/'
file_name = '60%2750V0.71um'

for i in range(1,7):
    file_dir = file_path+file_name+'/layer'+str(i)
    mkdir(file_dir)
