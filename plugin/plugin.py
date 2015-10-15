#-*-coding:utf-8-*-
#由这个模块导入一些必要的变量，因为这个插件肯定会跑
import sys
sys.path.append("..")

class Plugin():

	def exploit(self,url):
		print "Plugin Exploit"
	def help(self):
		print "there is no help"

print len("Administrators")