

def ascii_encode(zfc):
	zfcs = ""
	for i in zfc:
		zfcs += str(ord(i))+' '
	return zfcs.strip()

def ascii_decode(zfc):
	sz = zfc.split(' ')
	zfcs = ""
	for i in sz:
		zfcs += chr(int(i))
	return zfcs


def asciibm_main():
	print("==========进入ascii编码解码项==========")
	print("==========解码注意以空格分隔==========")
	zfc = input("请输入待处理的字符串: ")
	zfc = zfc.strip()
	pd = input("编码或解码?[b/j](默认编码): ")
	
	if pd == "b":
		try:
			xxx = ascii_encode(zfc)
		except:
			xxx = "编码失败!"
	
	elif pd == "j":
		try:
			xxx = ascii_decode(zfc)
		except:
			xxx = "编码失败!"
	
	else:
		try:
			xxx = ascii_encode(zfc)
		except:
			xxx = "编码失败!"
		
		
	
	print('===============================================================')
	print(xxx)
	print('===============================================================')
	pdwj = input("是否要输出为文件?(是则输入文件名，否则回车): ")
	if pdwj:
		pdwj = pdwj.strip()
		wjm = "./clwj/"+pdwj+".txt"
		xxx = xxx.strip()
		with open(wjm,'w') as txt:
			txt.write(xxx)
	
	print('==========ascii编码解码项处理完成==========')