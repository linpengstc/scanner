#-*-coding:utf-8-*-
import plugin
import time
# 文件名和插件类名保持一致
class  PluginTest2(plugin.Plugin):

	name = "PluginTest2"
	dependencies = ["PluginTest","PluginTest3"]
	def __init__(self,url):
		print "init plugin"
		self.url = url
	def exploit(self):
		print "start exploit2"+self.url
		time.sleep(2)
		print "end exploit2"

