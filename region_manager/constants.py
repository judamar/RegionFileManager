from mcdreforged.api.utils.serializer import Serializable

class Configure(Serializable):
    command: str = '!!rfm'
    source_path: str = './server/world/regions/'
    permission: int = 0