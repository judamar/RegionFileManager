from mcdreforged.api.all import *
from region_manager.config import Configure
from region_manager.file_mngr import *
from region_manager.UI import *

conf = Configure
unknown_argument_msg = gen_unknown_argument_message()

def register_command(server: PluginServerInterface):
    def get_literal_node(literal):
        lvl = conf.minimum_permission_level
        return Literal(literal).requires(lambda src: src.has_permission(lvl)).on_error(RequirementNotMet, lambda src: src.reply("Permission denied"), handled=True)

    server.register_command(
        Literal(conf.prefix).
        runs(lambda src: src.reply(gen_help_message())).
        on_error(UnknownArgument, lambda src, _: print_msg(server, unknown_argument_msg), handled=True).
        then(
            get_literal_node('save').
            runs(lambda src: print_msg(server, "hola"))
        ).
        then(
            get_literal_node('restore')
        ).
        then(
            get_literal_node('remove')
        ).
        then(
            get_literal_node('list').
            runs(lambda src: list_regions(src))
        ).
        then(
            get_literal_node('del').
            runs(lambda src: delete_region(src))
        )
    )

def print_msg(server: PluginServerInterface, msg, prefix="[RFM] "):
    msg = RTextList(prefix + msg)
    server.logger.info(msg)
    server.say(msg)

def on_load(server: PluginServerInterface, old):
    global conf
    conf = server.load_config_simple('config.json', target_class=Configure)
    msg = 'Plugin Region File Manager, use {}'.format(conf.prefix) 
    server.logger.info(msg)
    register_command(server)
