#-*-coding:utf-8-*-
import threading
import plugin
from util.pluginUtil import *

class Job(object):

	def __init__(self,pluginName,jobs,url):
		super(PluginThread,self).__init__()
		self.pluginName = pluginName
		self.plugin = createPluginClazz(pluginName)
		self.jobs = jobs
		self.url = url
	def run(self):
		# 运行时创建对象
		# for d in self.plugin.dependencies:
		# 	self.threads[d].join()
		# self.plugin().exploit(self.url)
		pass
	def getName(self):
		return self.name

	def getDependencies(self):
		return self.plugin.dependencies