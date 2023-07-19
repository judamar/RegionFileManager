from mcdreforged.api.all import *

def copy_region():
    pass

def delete_region():
    pass

def print_msg(server: PluginServerInterface, msg, prefix="[RFM]"):
    msg = RTextList(prefix + msg)
    server.logger.info(msg)
    server.say(msg)