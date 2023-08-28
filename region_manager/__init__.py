from time import sleep
from mcdreforged.api.all import *
from region_manager.config import Configure
from region_manager.UI import *
import json, os, shutil

conf = Configure
unknown_argument_msg = gen_unknown_argument_message()
dst_path = conf.dst_path

#|REGIONS MANAGEMENT|
class json_mngr():
#REG IN JSON FILE
    def reg_json(r_name, r_path, r_src_path, r_dim):
        new_data = {
            r_name: {
                "path": r_path,
                "src_path": r_src_path,
                "dim": r_dim
                }
        }
        path_json = f'./{dst_path}/regions.json'
        if os.path.exists(path_json):
            with open(path_json, "r") as archivo:
                data = json.load(archivo)
        else:
            data = {}
        data.update(new_data)
        with open(path_json, "w") as archivo:
            json.dump(data, archivo, indent=4)

    def list_json_file():
        path_json = f'./{dst_path}/regions.json'
        with open(path_json, "r") as archivo:
            data = json.load(archivo)
        result = ""
        for clave, valor in data.items():
            path = valor.get("path")
            dim = valor.get("dim")
            result += (f"\n  §bReg. Name:§r {clave} §bPath:§r {path} §bDimension:§r {dim}")
        return result

    
    def get_value(key, subkey):
        path_json = f'./{dst_path}/regions.json'
        with open(path_json, "r") as archivo:
            data = json.load(archivo)
        value = data.get(key)
        subvalue = value.get(subkey)
        return subvalue

#CHECK IF FOLDERS ARE ALREADY CREATED
def check_folders_created(server: PluginServerInterface):
    dst_path = conf.dst_path
    dst_path_over = conf.dst_path_over
    dst_path_nether = conf.dst_path_nether
    dst_path_end = conf.dst_path_end
    if not os.path.isdir(dst_path):
        os.makedirs(dst_path)
        server.logger.info("dst_path created.")
    if not os.path.isdir(dst_path_over):
        os.makedirs(dst_path_over)
        server.logger.info("dst_path_over created.")
    if not os.path.isdir(dst_path_nether):
        os.makedirs(dst_path_nether)
        server.logger.info("dst_path_nether created.")
    if not os.path.isdir(dst_path_end):
        os.makedirs(dst_path_end)
        server.logger.info("dst_path_end created.")

#MAKE THE REGION NAME
def make_region_name(x:int, z:int):
    return "r.{}.{}.mca".format(x,z)

def rm_file(file_path, server: PluginServerInterface):
    try:
        os.remove(file_path)
    except OSError:
        server.logger.info("Error while removing file")

#SAVE THE REGION
def save_region(server, info, x, z, dim, name):
    if dim=="0":
        src_path = conf.regions_path_over
        dst_path = conf.dst_path_over
    elif dim=="1":
        src_path = conf.regions_path_end
        dst_path = conf.dst_path_end
    elif dim == "-1":
        src_path = conf.regions_path_nether
        dst_path = conf.dst_path_nether
    
    region_name = make_region_name(x, z)
    file_src = src_path + region_name
    
    try:
        server.execute('save-off')
        server.execute('save-all flush')
        server.logger.info("Saving region file.")
        sleep(1)
        shutil.copy(file_src, dst_path)
        json_mngr.reg_json(name, dst_path + region_name, file_src, dim)
        sleep(1)
        server.execute('save-on')
        print_msg(server, "Region saved.")
    except FileNotFoundError:
        print_msg(server, f"Region {region_name} does not exist.")

def restore_region(server, info, name):
    filename = str(json_mngr.get_value(name, "path"))
    src_path = str(json_mngr.get_value(name, "src_path"))

    server.logger.info(f"restore file: {filename}")
    #try:
    server.logger.info(f"Restoring Region {name}")
    rm_file(src_path, server)
    server.logger.info(f"Region {src_path} deleted")
    server.logger.info("Copying region")
    shutil.copy(filename, src_path)
    server.logger.info("Region restored")
    #except Exception as ex:
        #server.logger.info(ex)
    

def remove_region(src_path:str, region_name:str, target_path:str):
    pass

def delete_region_from_saves():
    pass

#|REGISTER COMMANDS|    
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
            then(
                Integer("x").
                then(Integer("z").
                then(Text("dim").
                then(Text("name").runs(lambda src, ctx: save_region(src.get_server(), src, ctx["x"], ctx["z"], ctx["dim"], ctx["name"])))))
                )
            ).
        then(
            get_literal_node('restore').
            then(
                Text("name").runs(lambda src, ctx: restore_region(src.get_server(), src, ctx["name"]))
            )
        ).
        then(
            get_literal_node('remove').
            then(
                Text("name")
            )
        ).
        then(
            get_literal_node('list').
            runs(lambda src: src.reply(gen_list_message(json_mngr.list_json_file())))
        ).
        then(
            get_literal_node('del').
            runs(lambda src: delete_region_from_saves(src))
        )
    )

#|PRINT MESSAGE|
def print_msg(server: PluginServerInterface, msg, prefix="[RFM] "):
    msg = RTextList(prefix + msg)
    server.logger.info(msg)
    server.say(msg)

#|SERVER LOAD|
def on_load(server: PluginServerInterface, old):
    global conf
    conf = server.load_config_simple('config.json', target_class=Configure)
    msg = f"Plugin Region File Manager, use {conf.prefix}"
    check_folders_created(server)
    server.logger.info(msg)
    register_command(server)
