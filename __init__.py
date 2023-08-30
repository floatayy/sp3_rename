bl_info = {
    "name": "Sp3 Rename",
    "description": "Rename Vertex Groups in ripped Splatoon 3 models to make them compatible with TeenageApple's Splatoon 3 character rigs.",
    "author": "piparkaq (original Sp3 script), Floaty (UI & Sp2 implementation)",
    "version": (2, 0),
    "blender": (3, 0, 0),
    "category": "Object",
    "doc_url": "https://github.com/floatayy/sp3_rename",
}

import bpy

from .rename_obj_3 import RenameVertexGroups_Op_Sp3
from .rename_obj_3 import RenameVertexGroups_Shoes_Sp3
from .rename_obj_2 import RenameVertexGroups_Op_Sp2
from .rename_obj_2 import RenameVertexGroups_Shoes_Sp2
from .rename_3d import RenameVertexGroups_Panel_Sp3
from .rename_3d import RenameVertexGroups_Panel_Sp2


classes = (
    RenameVertexGroups_Op_Sp3,
    RenameVertexGroups_Shoes_Sp3,
    RenameVertexGroups_Op_Sp2,
    RenameVertexGroups_Shoes_Sp2,
    RenameVertexGroups_Panel_Sp3,
    RenameVertexGroups_Panel_Sp2,
)

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()
