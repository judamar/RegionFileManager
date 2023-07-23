from mcdreforged.api.all import *
import os, shutil

def make_region_name(x:int, z:int):
    return "r.{}.{}.mca".format(x,z)

def copy_region(src_path:str, region_name:str, target_path:str):
    try:
        file_src = src_path + region_name
        if not os.path.isdir(target_path):
            return "doesn't exist"
        else:
            #shutil.copy(file_src, target_path)
            return "do something"
    except:
        pass

def delete_region():
    pass

def print_msg(server: PluginServerInterface, msg, prefix="[RFM]"):
    msg = RTextList(prefix + msg)
    server.logger.info(msg)
    server.say(msg)