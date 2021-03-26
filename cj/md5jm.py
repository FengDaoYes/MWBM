import hashlib

def md5_encode(zfc):
	m = hashlib.md5()
	
	md5 = zfc.encode('utf-8')
	m.update(md5)
	xxx = m.hexdigest()
	return xxx

def md5jm_main():
	print('================进入md5加密项================\n')
	zfc = input("请输入待处理的字符: ")
	zfc = zfc.strip()
	
	zfc = md5_encode(zfc)
	
	print('===============================================================\n')
	print(zfc)
	
	print('\n==========md5加密项处理完成==========\n')
