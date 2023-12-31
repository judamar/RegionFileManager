from mcdreforged.api.rtext import RTextList, RText, RColor
from region_manager.config import Configure

conf = Configure()
prefix = conf.prefix

help_head = """
==================§b Region File Manager §r==================
"""
help_body = {
    f"§b{prefix}": "§rDisplay help message.",
    f"§b{prefix} save <x> <z> <dimension> <name>": "§rSave the region in a new folder.",
    f"§b{prefix} restore <name>": "§rRestore the specified region.",
    f"§b{prefix} remove <x> <z> <dimension>": "§rRemove the specified region file from world.",
    f"§b{prefix} list": "§rShow a list with the regions saved.",
    f"§b{prefix} del <name>": "§rDelete a region from list.",
    f"§b{prefix} abort": "§rAbort a currently running restoration operation."
}

list_head = """
==================§b Region File List §r==================
"""

def gen_help_message():
    help_message = RTextList(
        RText(help_head),
        RText("Available Commands:", color=RColor.gold),
    )
    for command, description in help_body.items():
        help_message.append(f"\n  {command} - {description}")
    return help_message

def gen_unknown_argument_message():
    unknown_message = RText("Unknown argument.", color=RColor.red)
    return str(unknown_message)

def gen_list_message(json_list):
    list_message = RTextList(
        RText(list_head),
        RText("Saved regions:", color=RColor.yellow),
    )
    list_message.append(json_list)
    return list_message