
import base64


def b64bm(strs):
	try:
		strs = strs.encode('utf-8')
		strsb = base64.encodebytes(strs)
		strsb = strsb.decode('utf-8')
		return strsb
	except:
		return "编码错误...\n"
	

def b64jm(strs):
	try:
		strs = strs.encode('utf-8')
		strsb = base64.decodebytes(strs)
		strsb = strsb.decode('utf-8')
		return strsb
	except:
		return "解码错误...\n"

def base64bm_main():
	print("==========进入base64编码解码项==========")
	zfc = input("请输入待处理的字符串: ")
	zfc = zfc.strip()
	pd = input("编码或解码?[b/j](默认编码): ")
	
	if pd == "b":
		xxx = b64bm(zfc)		
	
	elif pd == "j":
		xxx = b64jm(zfc)
	
	else:
		xxx = b64bm(zfc)
		
		
	
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
	
	print('==========base64编码解码项处理完成==========')
	
	
	
	
