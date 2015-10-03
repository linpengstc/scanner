#-*-coding:utf-8-*-
pluginDir = "plugin" 
def createPluginClazz(name):
	modname = pluginDir+"."+name
	mod = __import__(modname)
	components = modname.split('.')
	for comp in components[1:]:
		mod = getattr(mod, comp)
	return getattr(mod,name)
