#-*-coding:utf-8-*-
from scheduler import Scheduler
import json


#使用方式：在settings中设置参数
#在strategy中设置需要的扫描插件
if __name__ == '__main__':
	#开始调度
	# from PluginTest import *
	# pluginTest = PluginTest()self.settings[pluginName]
	settings = None
	#文件中为插件的参数
	with open("settings/strategy.json") as f:
		settings = json.load(f)
	strategy = ["WeakPass"]
	scheduler = Scheduler(strategy,settings)
	scheduler.startScan()

