

def zmszbm(zm):
	xxx = hex(ord(zm)).replace("0x","\\u00")
	
	return xxx
	


def unicode_bm(strs):
	strs = strs.strip()
	zmsz = "qwertyuiopasdfghjklzxcvbnm0123456789~!@#$%^&*()_+}{[]|\\\"':;?/.>,<-="
	zfc = ""
	
	for i in strs:
		if i in zmsz:
			w = zmszbm(i)
		else:
			w = i.encode('unicode_escape').decode()
		zfc += w
		
	return zfc
	
def unicode_jm(strs):
	strs = strs.encode('utf-8').decode('utf-8')
	s = strs.replace("uni", r"\u").encode('utf-8').decode('unicode_escape')
	
	return s



def unicodebm_main():
	print('================进入Unicode编码项================\n')
	zfc = input("请输入待处理的字符: ")
	zfc = zfc.strip()
	pd = input("编码或解码?[b/j](默认编码): ")
	
	if pd == "b":	
		zfc = unicode_bm(zfc)
	
	elif pd == "j":
		zfc = unicode_jm(zfc)
	else:
		zfc = unicode_bm(zfc)


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
	
	print('==========Unicode编码项处理完成==========\n')

