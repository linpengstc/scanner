#-*-coding:utf-8-*-
from scheduler import Scheduler

if __name__ == '__main__':
	#开始调度
	# from PluginTest import *
	# pluginTest = PluginTest()
	strategy = ["PluginTest2","PluginTest"]
	url = "www.linpeng.com"
	scheduler = Scheduler(strategy,url)
	scheduler.startScan()