#-*-coding:utf-8-*-
#先执行检测
#再执行探测
#再执行任务（还是设计得单一，插件之间必需有依赖）
#返回一个状态

#插件依赖信息，指定依赖名。返回状态，以扫描出来的信息。扫描出来的信息放到
#负责解析插件基本信息
import threading
import plugin
from util.pluginUtil import *

class PluginThread(threading.Thread):
	#args转换为args,args包含args
	def __init__(self,pluginName,threads,args):
		super(PluginThread,self).__init__()
		self.pluginName = pluginName
		self.plugin = createPluginClazz(pluginName)
		self.threads = threads
		self.args = args
	def run(self):
		# 运行时创建对象
		for d in self.plugin.dependencies:
			self.threads[d].join()
		self.plugin(**self.args).exploit()

	def getName(self):
		return self.name

	def getDependencies(self):
		return self.plugin.dependencies

# if __name__ == '__main__':
	# import 
	# PluginThread()