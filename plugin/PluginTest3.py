#-*-coding:utf-8-*-
import plugin
import time
# 文件名和插件类名保持一致
class  PluginTest3(plugin.Plugin):

	name = "PluginTest3"
	dependencies = ["PluginTest"]
	def __init__(self,url):
		self.url = url
		print "init plugin3"
	def exploit(self):
		print "start exploit3"+self.url
		time.sleep(2)
		print "end exploit3"

