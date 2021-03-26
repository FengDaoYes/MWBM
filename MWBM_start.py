# -*- coding: utf-8 -*-
import cj.urlbm
import cj.base64bm
import cj.slbm
import cj.unicodebm
import cj.htmlbm
import cj.utf8bm
import cj.md5jm
import cj.sqlhx
import cj.asciibm


def biaoti():
	print("""
 _  ___  __        ______  __  __ 			   	 	
|  \/  | \ \      / / __ )|  \/  |
| |\/| |  \ \ /\ / /|  _ \| |\/| |
| |  | |   \ V  V / | |_) | |  | |
|_|  |_|    \_/\_/  |____/|_|  |_|""")
	xinxi = "MWBM: v0.4\n"
	xinxi += "======== BY:F_Dao||========\n\n"
	xinxi += "\t十七张牌你能秒杀我？\n"
	print(xinxi)

def bmdb():
	xinxi = "======================================\n"
	xinxi += "base64编码: MTIzNDU=\n"
	xinxi += "url编码: %31%32%33%34%35\n"
	xinxi += "十六进制: 0x3132333435\n"
	xinxi += "Unicode编码: \\u0031\\u0032\\u0033\\u0034\\u0035\n"
	xinxi += "Html实体字符编码: &#x31;&#x32;&#x33;&#x34;&#x35;\n"
	xinxi += "utf8编码: \\x31\\x32\\x33\\x34\\x35\n"
	xinxi += "md5加密: 202cb962ac59075b964b07152d234b70\n"
	xinxi += "ascii编码: 104 97 104 97 104 97 33\n"
	print(xinxi)


def start():
	xinxi = "选项:\n"
	xinxi += "=[0] 编码对比查看=\n"
	xinxi += "=[1] base64编码解码=\n"
	xinxi += "=[2] url编码解码=\n"
	xinxi += "=[3] 十六进制=\n"
	xinxi += "=[4] Unicode编码=\n"
	xinxi += "=[5] Html实体字符编码=\n"
	xinxi += "=[6] utf8编码项=\n"
	xinxi += "=[7] md5加密项=\n"
	xinxi += "=[8] sql语句混淆=\n"
	xinxi += "=[9] ascii编码解码=\n"
	xinxi += "=[exit] 退出=\n\n"

	
	print(xinxi)
	xuanxiang = input("请输入处理模块: ")
	xuanxiang = xuanxiang.strip()
	
	return xuanxiang
	

def main():
	#程序入口
	biaoti()
	while True:
		print("======================================\n")
		xuanxiang = start()
		
		if xuanxiang == "exit":
			exit(0)
		elif xuanxiang == "0":
			bmdb()
		elif xuanxiang == "1":
			cj.base64bm.base64bm_main()
		elif xuanxiang == "2":
			cj.urlbm.urlbm_main()
		elif xuanxiang == "3":
			cj.slbm.slbm_main()
		elif xuanxiang == "4":
			cj.unicodebm.unicodebm_main()
		elif xuanxiang == "5":
			cj.htmlbm.htmlbm_main()
		elif xuanxiang == "6":
			cj.utf8bm.utf8bm_main()
		elif xuanxiang == "7":
			cj.md5jm.md5jm_main()
		elif xuanxiang == "8":
			cj.sqlhx.sqlhx_main()
		elif xuanxiang == "9":
			cj.asciibm.asciibm_main()
		else:
			pass
		
if __name__ == "__main__":
	main()	
		
