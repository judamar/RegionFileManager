from mcdreforged.api.all import *
from region_manager.config import Configure
from region_manager.file_mngr import *
from region_manager.UI import *

conf = Configure

def print_msg(server: PluginServerInterface, msg, prefix="[RFM]"):
    msg = RTextList(prefix + msg)
    server.logger.info(msg)
    server.say(msg)

def on_load(server: PluginServerInterface, old):
    conf = server.load_config_simple('config.json', target_class=Configure)
    msg = 'Plugin Region File Manager, use {}'.format(conf.prefix) 
    server.logger.info(msg)
    help_message = gen_help_message()
    server.register_command(Literal(conf.prefix).runs(lambda src: src.reply(help_message)))
