from mcdreforged.api.utils.serializer import Serializable

class Configure(Serializable):
    command: str = '!!rfm'
    recognized_cmds : str = {'export', 'remove'}
    regions_path_over: str = './server/world/region/'
    regions_path_nether: str = './server/world/DIM-1/region/'
    regions_path_end: str = './server/world/DIM1/region/'
    permission: int = 3