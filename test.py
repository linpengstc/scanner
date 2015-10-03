
# from plugin import *
# def my_import(name):
#     mod = __import__(name)
#     components = name.split('.')
#     for comp in components[1:]:
#         mod = getattr(mod, comp)
#     return mod


# name = "plugin.PluginTest"
# mod = my_import("plugin.PluginTest")
# print dir(a)

from util.pluginUtil import *
createPlugin("PluginTest")

