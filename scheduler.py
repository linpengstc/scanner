#-*-coding:utf-8-*-

from pluginThread import PluginThread
#
#根据策略，启动插件，就是启动一个线程跑插件
#插件运行完后会返回一个状态
#用一个链表表示一条任务，线程之间的关系怎么解决？
#比如一个插件依赖另两个插件，利用锁，线程之间的关系用锁来表示
#一个scheduler可以对应一系列settings
#解析策略表，策略表示这样一个结构url-->策略，现在开发阶段，先假设只有一个url，对应一些列策略

#plugin表示基本的插件信息
#PluginThread表示将插件包装成线程的类
#p表示线程对象
class Scheduler(object):
	def __init__(self,strategy,settings):
		self.strategy = strategy#strategy是map里面都是plug对象，plug对象之间有依赖关系
		self.jobs= {}
		#插件有个堆栈关系
		self.priority = []
		self.settings = settings
		# self.plevel = {}
	#解析任务，将任务和任务的依赖都加进来
	def parseJob(self,pluginName):#plugin中需要有name属性和dependecies属性
		#启动线程，解决依赖关系
		#如果这个线程在threads表中，那么就不用做什么了
		if pluginName in self.jobs:
			return
		p = PluginThread(pluginName,self.jobs,self.settings[pluginName])
		self.jobs[pluginName] = p;
		for dependency in p.getDependencies():	
			#返回表示插件线程正常创建
			#将所有线程先启动起来，至于线程中的依赖等待关系，让插件自己解决,插件不能写threads	
			self.parseJob(dependency)
			#启动线程后等待这个线程
		self.priority.append(p)
			

	def startScan(self):
		#首先解析strategy
		for plugin in self.strategy:
			self.parseJob(plugin)
		for p in self.priority:
			p.start()
	def stopScan(self):
		pass


#有两个结构保存插件的线程 ： 一个是map,一个是priority
#map是为了将插件名和插件线程结合
#priority是为了保存线程的优先级
