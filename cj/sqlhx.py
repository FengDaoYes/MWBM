import base64
import random

#=====================函数库===============================
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

#=====================规则库===============================
def gz1(sql):
	# 将空格替换为/**/
	sql = sql.lower()
	sql = sql.replace(' ','/**/')
	return sql

def gz2(sql):
	#将空格替换为+
	sql = sql.lower()
	sql = sql.replace(' ','+')
	return sql

def gz3(sql):
	#将sql语句进行url编码
	sql = sql.lower()
	zfc = ""
	for i in sql:
		zfs = hex(ord(i)).replace("0x","%")
		zfc += zfs
	return zfc

def gz4(sql):
	#将sql语句进行base64编码
	sql = sql.lower()
	try:
		sql = sql.encode('utf-8')
		strsb = base64.encodebytes(sql)
		strsb = strsb.decode('utf-8')
		return strsb
	except:
		print("编码失败，请检查是否有特殊字符")
		return sql

def gz5(sql):
	#添加多个空格
	sql = sql.lower()
	sql = sql.replace(' ','   ')
	return sql

def gz6(sql):
	#关键字双写，如anandd、oorr
	sql = sql.lower()
	sql = sql.replace('and','anandd')
	sql = sql.replace('or','oorr')
	sql = sql.replace('select','seselectlect')
	sql = sql.replace('union','ununionion')
	return sql

def gz7(sql):
	#将空格替换为%0a
	sql = sql.lower()
	sql = sql.replace(' ','%0a')
	return sql

def gz8(sql):
	#将=号替换为like
	sql = sql.lower()
	sql = sql.replace('=','like')

def gz9(sql):
	#将>替换为between
	sql = sql.lower()
	sql = sql.replace('>','between')

def gz10(sql):
	#在每个字符面前添加%
	sql = sql.lower()
	zfc = ""
	for i in sql:
		if i != ' ':
			x = "%"+i
			zfc += x
		else:
			zfc += ' '
	return zfc

def gz11(sql):
	#随机大小写
	sql = sql.lower()
	zfc = ""
	for i in sql:
		sz = random.randint(0,1)
		if str(sz) == "0":
			i = i.lower()
		else:
			i = i.upper()
		zfc += i
	return zfc

def gz12(sql):
	#uniocede编码
	sql = sql.lower()
	sql = unicode_bm(sql)
	return sql

def gz13(sql):
	#将=替换为GREATEST
	sql = sql.lower()
	sql = sql.replace('=','GREATEST')
	return sql

def gz14(sql):
	#将'替换为%00%27
	sql = sql.lower()
	sql = sql.replace("'","%00%27")
	return sql

def gz15(sql):
	#将空格替换为%23%0A
	sql = sql.lower()
	sql = sql.replace(" ","%23%0A")

def gz16(sql):
	#关键字用内敛注释包裹
	sql = sql.lower()
	sql = sql.replace('and','/*!and*/')
	sql = sql.replace('or','/*!or*/')
	sql = sql.replace('select','/*!select*/')
	sql = sql.replace('union','/*!union*/')
	sql = sql.replace('from','/*!from*/')
	sql = sql.replace('concat','/*!concat*/')
	sql = sql.replace('all','/*!all*/')
	sql = sql.replace('char','/*!char*/')
	sql = sql.replace('null','/*!null*/')
	sql = sql.replace('if','/*!if*/')
	return sql

def gz17(sql):
	#替换空格为--%0a
	sql = sql.lower()
	sql = sql.replace(' ','--%0a')
	return sql

def gz18(sql):
	#关键字前加内敛注释包裹2
	sql = sql.lower()
	sql = sql.replace('and','/*!0and*/')
	sql = sql.replace('or','/*!0or*/')
	sql = sql.replace('select','/*!0select*/')
	sql = sql.replace('union','/*!0union*/')
	sql = sql.replace('from','/*!0from*/')
	sql = sql.replace('concat','/*!0concat*/')
	sql = sql.replace('all','/*!0all*/')
	sql = sql.replace('char','/*!0char*/')
	sql = sql.replace('null','/*!0null*/')
	sql = sql.replace('if','/*!0if*/')
	return sql

def gz19(sql):
	#将空格替换为#
	sql = sql.lower()
	sql = sql.replace(' ','#')
	return sql

def gz20(sql):
	#将空格替换为//
	sql = sql.lower()
	sql = sql.replace(" ","//")
	return sql

def gz21(sql):
	#在sql语句末端加入%00
	return sql+"%00"

def gz22(sql):
	#用/**/分割sql语句关键字
	sql = sql.lower()
	sql = sql.replace('and','a/**/nd')
	sql = sql.replace('or','o/**/r')
	sql = sql.replace('select','sel/**/ect')
	sql = sql.replace('union','un/**/ion')
	sql = sql.replace('from','fr/**/om')
	sql = sql.replace('concat','co/**/ncat')
	sql = sql.replace('all','al/**/l')
	sql = sql.replace('char','ch/**/ar')
	sql = sql.replace('null','nu/**/ll')
	sql = sql.replace('if','i/**/f')
	return sql

def gz23(sql):
	#使用宽字节注入
	if "'" in sql:
		x = sql.find("'")
		zfc = sql[:x]+"%df"+sql[x:]
		return zfc
	else:
		print('没有发现闭合单引号')
		return sql

def gz24(sql):
	#将空格替换为%0d
	sql = sql.lower()
	sql = sql.replace(" ","%0d")
	return sql

def gz25(sql):
	#将空格替换为%09
	sql = sql.lower()
	sql = sql.replace(" ","%09")
	return sql

def gz26(sql):
	#将空格替换为%20
	sql = sql.lower()
	sql = sql.replace(" ","%20")
	return sql

def gz27(sql):
	#将空格代替/*%00*/%23a%0A
	sql = sql.lower()
	sql = sql.replace(" ","/*%00*/%23a%0A")
	return sql

def gz28(sql):
	#将空格随机替换为"/**/", "/*!*/", "/*!safe6*/", "+"
	sql = sql.lower()
	chars2 = ["/**/", "/*!*/", "/*!safe6*/", "+"]
	sql = sql.replace(" ", random.choice(chars2))
	return sql

def gz29(sql):
	#将关键字用随机空白字符包裹
	sql = sql.lower()
	chars1 = ['%01', '%02', '%03', '%04', '%05', '%06', '%07', '%08', '%09', '%0A', '%0B', '%0C', '%0D', '%0E', '%0F','%10', '%11','%12', '%13', '%14', '%15', '%16', '%17', '%18', '%19', '%1A', '%1B', '%1C', '%1D', '%1E', '%1F', '%20']
	v = random.choice(chars1)
	sql = sql.replace("=", v + "=" + v)
	sql = sql.replace("and", v + "and" + v)
	sql = sql.replace("where", v + "where" + v)
	sql = sql.replace("select", v + "select" + v)
	sql = sql.replace("union", v + "union" + v)
	sql = sql.replace("or", v + "or" + v)
	sql = sql.replace("from", v + "from" + v)
	return sql

def gz30(sql):
	#将关键字用uniocede编码
	sql = sql.lower()
	sql = sql.replace("union", "u%u006eion")
	sql = sql.replace("char", "%u0063har")
	sql = sql.replace("select", "se%u006cect")
	sql = sql.replace("from", "%u0066rom")
	return sql

def gz31(sql):
	#将空格替换为"/*%%!asd%%%%*/"
	sql = sql.lower()
	sql = sql.replace(" ", "/*%%!asd%%%%*/")
	return sql
#==============================副程序==================================

def xuanxiang():
	xinxi = "====================================================================================\n"
	xinxi += "规则库:\n"
	xinxi += "[a1]将空格替换为/**/\t\t[a2]将空格替换为+\t\t[a3]将sql语句进行url编码\n"
	xinxi += "[a4]将sql语句进行base64编码\t[a5]添加多个空格\t\t[a6]关键字双写，如anandd、oorr\n"
	xinxi += "[a7]将空格替换为%0a\t\t[a8]将=号替换为like\t\t[a9]将>替换为between\n"
	xinxi += "[b0]在每个字符面前添加%\t\t[b1]随机大小写\t\t\t[b2]uniocede编码\n"
	xinxi += "[b3]将=替换为GREATEST\t\t[b4]将'替换为%00%27\t\t[b5]将空格替换为%23%0A\n"
	xinxi += "[b6]关键字用内联注释包裹\t[b7]替换空格为--%0a\t\t[b8]关键字前加内联注释包裹2\n"
	xinxi += "[b9]将空格替换为#\t\t[c0]将空格替换为//\t\t[c1]在sql语句末端加入%00\n"
	xinxi += "[c2]用/**/分割sql语句关键字\t[c3]使用宽字节注入\t\t[c4]将空格替换为%0d\n"
	xinxi += "[c5]将空格替换为%09\t\t[c6]将空格替换为%20\t\t[c7]将空格代替/*%00*/%23a%0A\n"
	xinxi += "[c8]将空格随机替换\t\t[c9]将关键字用随机空白字符包裹\t[d0]将关键字用uniocede编码\n"
	xinxi += "[d1]将空格替换为/*%%!asd%%%%*/\n"
	xinxi += "===================================================================================="
	print(xinxi)

def xxmcl(xxm):
	xxm = xxm.replace("a",",0")
	xxm = xxm.replace("b",",1")
	xxm = xxm.replace("c",",2")
	xxm = xxm.replace("d",",3")
	return xxm

def xxmzx(xxms,sqlyj):
	for i in xxms:
		i = i.strip()
		if len(i) != 2:
			print('规则: '+i+" 处理失败!!")
			continue
		if i == "01":
			sqlyj = gz1(sqlyj)

		if i == "02":
			sqlyj = gz2(sqlyj)

		if i == "03":
			sqlyj = gz3(sqlyj)

		if i == "04":
			sqlyj = gz4(sqlyj)

		if i == "05":
			sqlyj = gz5(sqlyj)

		if i == "06":
			sqlyj = gz6(sqlyj)

		if i == "07":
			sqlyj = gz7(sqlyj)

		if i == "08":
			sqlyj = gz8(sqlyj)

		if i == "09":
			sqlyj = gz9(sqlyj)

		if i == "10":
			sqlyj = gz10(sqlyj)

		if i == "11":
			sqlyj = gz11(sqlyj)

		if i == "12":
			sqlyj = gz12(sqlyj)

		if i == "13":
			sqlyj = gz13(sqlyj)

		if i == "14":
			sqlyj = gz14(sqlyj)

		if i == "15":
			sqlyj = gz15(sqlyj)

		if i == "16":
			sqlyj = gz16(sqlyj)

		if i == "17":
			sqlyj = gz17(sqlyj)

		if i == "18":
			sqlyj = gz18(sqlyj)

		if i == "19":
			sqlyj = gz19(sqlyj)

		if i == "20":
			sqlyj = gz20(sqlyj)

		if i == "21":
			sqlyj = gz21(sqlyj)

		if i == "22":
			sqlyj = gz22(sqlyj)

		if i == "23":
			sqlyj = gz23(sqlyj)

		if i == "24":
			sqlyj = gz24(sqlyj)

		if i == "25":
			sqlyj = gz25(sqlyj)

		if i == "26":
			sqlyj = gz26(sqlyj)

		if i == "27":
			sqlyj = gz27(sqlyj)

		if i == "28":
			sqlyj = gz28(sqlyj)
		
		if i == "29":
			sqlyj = gz29(sqlyj)
		
		if i == "30":
			sqlyj = gz30(sqlyj)

		if i == "31":
			sqlyj = gz31(sqlyj)

	return sqlyj

def ddzx(i,sqlyj):
	if i == "01":
		sqlyj = gz1(sqlyj)

	if i == "02":
		sqlyj = gz2(sqlyj)

	if i == "03":
		sqlyj = gz3(sqlyj)

	if i == "04":
		sqlyj = gz4(sqlyj)

	if i == "05":
		sqlyj = gz5(sqlyj)

	if i == "06":
		sqlyj = gz6(sqlyj)

	if i == "07":
		sqlyj = gz7(sqlyj)

	if i == "08":
		sqlyj = gz8(sqlyj)

	if i == "09":
		sqlyj = gz9(sqlyj)

	if i == "10":
		sqlyj = gz10(sqlyj)

	if i == "11":
		sqlyj = gz11(sqlyj)

	if i == "12":
		sqlyj = gz12(sqlyj)

	if i == "13":
		sqlyj = gz13(sqlyj)

	if i == "14":
		sqlyj = gz14(sqlyj)

	if i == "15":
		sqlyj = gz15(sqlyj)

	if i == "16":
		sqlyj = gz16(sqlyj)

	if i == "17":
		sqlyj = gz17(sqlyj)

	if i == "18":
		sqlyj = gz18(sqlyj)

	if i == "19":
		sqlyj = gz19(sqlyj)

	if i == "20":
		sqlyj = gz20(sqlyj)

	if i == "21":
		sqlyj = gz21(sqlyj)

	if i == "22":
		sqlyj = gz22(sqlyj)

	if i == "23":
		sqlyj = gz23(sqlyj)

	if i == "24":
		sqlyj = gz24(sqlyj)

	if i == "25":
		sqlyj = gz25(sqlyj)

	if i == "26":
		sqlyj = gz26(sqlyj)

	if i == "27":
		sqlyj = gz27(sqlyj)

	if i == "28":
		sqlyj = gz28(sqlyj)
		
	if i == "29":
		sqlyj = gz29(sqlyj)
		
	if i == "30":
		sqlyj = gz30(sqlyj)

	if i == "31":
		sqlyj = gz31(sqlyj)

	return sqlyj

#==============================主程序=================================

def sqlhx_main():
	print("==========================进入SQL语句混淆项=============================")
	pddd = input("请问是否使用断点处理(y)否则使用选项码一次性处理: ")
	pddd = pddd.strip()
	if pddd and pddd == "y":
		sqlyj = input("输入待混淆的sql语句: ")
		while True:
			xuanxiang()	
			xx = input("请输入待处理的值(q则退出): ")
			xx = xx.strip()
			if xx == "q":
				break
			xx = xxmcl(xx)
			xx = xx.replace(',','')
			sqlyj = ddzx(xx,sqlyj)
			print("=====处理结果如下=====")
			print(sqlyj)
	else:
		xuanxiang()
		sqlyj = input("输入待混淆的sql语句: ")
		xxm = input("请输入需要处理的选项码(例如:c7b6b1): ")
		xxm = xxm.strip()
		xxm = xxmcl(xxm)
		xxms = xxm.split(',')
		del(xxms[0])
		sqlyj = xxmzx(xxms,sqlyj)
	print("======================处理完成============================\n")
	print(sqlyj)
	print("\n======================SQL语句混淆项处理结束========================\n")
	