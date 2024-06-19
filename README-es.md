[English](README.md) | Español
# Region File Manager (RFM)

Este es un plugin para [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) que permite gestionar archivos de región en un servidor Minecraft.

## Descripción

El plugin Region File Manager (RFM) es una herramienta útil para gestionar regiones en tu mundo Minecraft. Te permite realizar tareas como guardar, restaurar, borrar y listar regiones con facilidad.

## Comandos

El plugin RFM añade los siguientes comandos:

- `!!rfm save <x> <z> <dim> <name>`: Guarda una región en una nueva carpeta.
- `!!rfm restore <name>`: Restaura la región especificada.
- `!!rfm remove <x> <z> <dim>`: Elimina del mundo el archivo de región especificado.
- `!!rfm list`: Mostrar una lista de las regiones guardadas.
- `!!rfm del <name>`: Elimina una región de la lista.
- `!!rfm abort`: Abortar una operación de restauración en curso.

`1`: para el end.
`0`: para el overworld.
`-1`: para el nether.

## Configuración

Puedes configurar el comportamiento del plugin en el fichero `config.json` con las siguientes opciones:

- **prefix**: Define el prefijo para los comandos del plugin.
- **recognized_cmds**: Lista de comandos reconocidos por el plugin.
- **regions_path_over**: Ruta a las regiones en el mundo principal (Overworld).
- **regions_path_nether**: Ruta a las regiones del Nether.
- **regions_path_end**: Ruta a las regiones del Fin.
- **dst_path**: Ruta donde se guardan las regiones.
- **dst_path_over**: Ruta para las regiones del Overworld.
- **dst_path_nether**: Ruta para las regiones de Nether.
- **dst_path_end**: Ruta para las regiones End.
- **minimum_permission_level**: Nivel de permiso mínimo necesario para utilizar el plugin.

Asegúrate de que las rutas son correctas en base a la estructura de tu servidor Minecraft.
Debería seguir funcionando sin modificar nada.

### Configuración por defecto:

```json
{
    "prefix": "rfm",
    "recognized_cmds": [
        "save",
        "restore",
        "remove",
        "list",
        "del",
        "abortar"
    ],
    "regions_path_over": "./servidor/mundo/región/",
    "regions_path_nether": "./servidor/mundo/DIM-1/región/",
    "regions_path_end": "./servidor/mundo/DIM1/región/",
    "ruta_dst": "./carpeta_regiones/",
    "dst_path_over": "./carpeta_regiones/sobremundo/",
    "dst_path_nether": "./carpeta_regiones/nether/",
    "dst_path_end": "./carpeta_regiones/final/",
    "minimum_permission_level": 3
}