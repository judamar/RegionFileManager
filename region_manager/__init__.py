from mcdreforged.api.all import *
from config import *
from file_mngr import *

def on_load(server: PluginServerInterface, old):
    server.logger.info(server.tr('my_plugin.a_message'))
    print_msg(server, "hola")
