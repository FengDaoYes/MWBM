import html

def htmlbm(strs):
	strs = strs.strip()
	zfs = ""
	for i in strs:
		x = hex(ord(i)).replace('0x','&#x')
		x = x+";"
		zfs += x
	return zfs


def htmljm(strs):
	zfs = html.unescape(strs)
	
	return zfs




def htmlbm_main():
	print('================进入Html实体字符编码项================\n')
	zfc = input("请输入待处理的字符: ")
	zfc = zfc.strip()
	pd = input("编码或解码?[b/j](默认编码): ")
	
	if pd == "b":	
		zfc = htmlbm(zfc)
	
	elif pd == "j":
		zfc = htmljm(zfc)
	else:
		zfc = htmlbm(zfc)


	print('===============================================================\n')
	print(zfc)
	print('\n===============================================================\n')
	
	pdwj = input("是否要输出为文件?(是则输入文件名，否则回车): ")
	if pdwj:
		pdwj = pdwj.strip()
		wjm = "./clwj/"+pdwj+".txt"
		zfc = zfc.strip()
		with open(wjm,'w') as txt:
			txt.write(zfc)
	
	print('==========Html实体字符编码项处理完成==========\n')
	
	
