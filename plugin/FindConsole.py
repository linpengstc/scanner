#-*-coding:utf-8-*-

import plugin
import urllib2
from kb.easykb import *
# 文件名和插件类名保持一致
class  FindConsole(plugin.Plugin):

	name = "FindConsole"
	dependencies = []
	path = "/admin.php"
	def __init__(self,url):
		self.url = url
		# print "init plugin"
	def env(self):
		return path
	def result(self):
		value = self.url+FindConsole.path
		set_kb_item("console",value)
		print "[+]FindConsole in "+value
	def exploit(self):
		print "start exploit:"+self.url
		response = urllib2.urlopen(self.url+FindConsole.path)
		if response.getcode():
			self.result()
		print "end exploit"


if __name__ == '__main__':
	p = FindConsole("http://www.rich8.com")
	p.exploit()