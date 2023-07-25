from mcdreforged.api.utils.serializer import Serializable

class Configure(Serializable):
    prefix: str = '!!rfm'
    recognized_cmds : list =  [
        "save",
        "restore",
        "remove",
        "list",
        "del",
        "abort"
    ]
    regions_path_over: str = './server/world/region/'
    regions_path_nether: str = './server/world/DIM-1/region/'
    regions_path_end: str = './server/world/DIM1/region/'
    do_backup_before_something: bool = False
    minimum_permission_level: int = 3