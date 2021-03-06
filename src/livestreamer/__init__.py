from livestreamer import plugins

import os.path

RCFILE = os.path.expanduser("~/.livestreamerrc")

def resolve_url(url):
    for name, plugin in plugins.get_plugins().items():
        if plugin.can_handle_url(url):
            return (name, plugin)
    return None

def get_plugins():
    return plugins.get_plugins()

plugins.load_plugins(plugins)
