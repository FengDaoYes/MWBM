
# 编码
def url_encode(zf):
    zfc = ""
    for i in zf:
        zfs = hex(ord(i)).replace("0x","%")
        zfc += zfs
    return zfc

#解码
def url_decode(zfc):
	while True:
		if "%" in zfc:
			xxx = zfc.find("%")
			
			bm = zfc[xxx:xxx+3]
			
			bms = bm.replace('%','')
			
			bms = '0x'+bms
			try:
				zz = chr(eval(bms))
				zfc = zfc.replace(bm,zz)
			except:
				zfc = zfc.replace(bm[:1],'异常基础点')
		else:
			break
	zfc = zfc.replace('异常基础点','%')
	return zfc


def urlbm_main():
	print('================进入url编码项================\n')
	zfc = input("请输入待处理的字符: ")
	pd = input("编码或解码?[b/j](默认编码): ")
	
	if pd == "b":	
		js = input("请输入需进行几次编码[默认为1]: ")
		if js:
			for i in range(int(js)):
				zfc = url_encode(zfc)
		else:
			zfc = url_encode(zfc)	
	elif pd == "j":
		
		zfc = url_decode(zfc)	
	else:
		js = input("请输入需进行几次编码[默认为1]: ")
		if js:
			for i in range(int(js)):
				zfc = url_encode(zfc)
		else:
			zfc = url_encode(zfc)
	print('===============================================================\n')
	print(zfc)
	print('===============================================================\n')
	
	pdwj = input("是否要输出为文件?(是则输入文件名，否则回车): ")
	if pdwj:
		pdwj = pdwj.strip()
		wjm = "./clwj/"+pdwj+".txt"
		zfc = zfc.strip()
		with open(wjm,'w') as txt:
			txt.write(zfc)
	
	print('==========url编码解码项处理完成==========\n')
	
