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
    dst_path: str = './regions_folder/'
    dst_path_over: str = './regions_folder/overworld/'
    dst_path_nether: str = './regions_folder/nether/'
    dst_path_end: str = './regions_folder/end/'
    minimum_permission_level: int = 3