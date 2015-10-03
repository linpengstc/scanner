#-*-coding:utf-8-*-
import time
# 文件名和插件类名保持一致
class  PluginTest():

	name = "PluginTest"
	dependencies = []
	def exploit(self):
		print "start exploit"
		time.sleep(5)
		print "end exploit"

