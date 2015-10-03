#-*-coding:utf-8-*-
pluginDir = "plugin" 
def createPlugin(name):
	modname = pluginDir+"."+name
    mod = __import__(modname)
    components = modname.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    clazz = getattr(mod,name)
    return clazz()
