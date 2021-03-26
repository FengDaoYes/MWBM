# 编码

def utf8_encode(zf):
    zfc = ""
    for i in zf:
        zfs = hex(ord(i)).replace("0x","\\x")
        zfc += zfs
    return zfc

#解码
def utf8_decode(zf):
	zfc = ""
	lb = zf.split("\\x")
	lb.pop(0)
	try:
		for i in lb:
			q = '0x'+i
			zfs = chr(eval(q))
			zfc += zfs
	except:
		zfc = "解码异常.."
	return zfc


def utf8bm_main():
	print('================进入utf-8编码项================\n')
	zfc = input("请输入待处理的字符: ")
	zfc = zfc.strip()
	pd = input("编码或解码?[b/j](默认编码): ")
	
	if pd == "b":	
		zfc = utf8_encode(zfc)
	
	elif pd == "j":
		zfc = utf8_decode(zfc)
	else:
		zfc = utf8_encode(zfc)


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
	
	print('==========utf-8编码项处理完成==========\n')
