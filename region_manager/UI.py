from mcdreforged.api.rtext import *
from region_manager.config import Configure

conf = Configure()
prefix = conf.prefix

help_head = """================== §b Region File Manager §r=================="""
help_body = {
    f"§b{prefix}": "§rDisplay this help message.",
    f"§b{prefix} export <x> <z> <dimension>": "§rShow the list of region files.",
    f"§b{prefix} remove <x> <z> <dimension>": "§rRemove the specified region file.",
}

def gen_help_message():
    help_message = RTextList(
        RText(help_head),
        RText("Available Commands:"))
    for command, description in help_body.items():
        help_message.append(f"\n  {command} - {description}")
    return help_message