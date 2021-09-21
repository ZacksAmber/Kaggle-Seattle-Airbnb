PLUGINS = dict()

def plugin_register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func