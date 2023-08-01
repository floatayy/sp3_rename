bl_info = {
    "name": "Sp3 Rename",
    "description": "Rename Vertex Groups in ripped Splatoon 3 models to make them compatible with TeenageApple's Splatoon 3 character rigs.",
    "author": "piparkaq (original script), Floaty (UI implementation)",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "category": "Object",
    "doc_url": "https://github.com/floatayy/sp3_rename",
}

import bpy

from . rename_obj import RenameVertexGroups_Op
from . rename_3d import RenameVertexGroups_Panel

classes = (RenameVertexGroups_Op, RenameVertexGroups_Panel)

def register():
    print("Hmm")
    bpy.utils.register_class(RenameVertexGroups_Op)
    bpy.utils.register_class(RenameVertexGroups_Panel)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    print("Hm...")


if __name__ == '__main__':
    register()