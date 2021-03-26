
def slbm(zf):
	zfc = ""
	for i in zf:
		zfs = hex(ord(i)).replace("0x","")
		zfc +=zfs
	zfc = "0x"+zfc
	return zfc


	


def sljm(zf):
	zfcs = ""
	zf = zf.replace("0x","")
	zfs = ""
	for i in zf:
		zfs += i
		if len(zfs) == 2:
			zfc = chr(eval("0x"+zfs))
			zfcs += zfc
			zfs = ""
			
	return zfcs 
	

def slbm_main():
	print('================进入十六进制项================\n')
	zfc = input("请输入待处理的字符: ")
	zfc = zfc.strip()
	pd = input("编码或解码?[b/j](默认编码): ")
	
	if pd == "b":	
		zfc = slbm(zfc)
	
	elif pd == "j":
		if len(zfc)%2 == 0:
			zfc = sljm(zfc)
		else:
			zfc = "错误,输入数值非偶数"
	else:
		zfc = slbm(zfc)


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
	
	print('==========十六进制项处理完成==========\n')
	
