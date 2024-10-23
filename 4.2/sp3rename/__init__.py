import bpy

from .rename import (RenameVertexGroups_Op, RenameVertexGroups_Shoes, RenameVertexGroups_Panel, gameSelector)


classes = (
    RenameVertexGroups_Op,
    RenameVertexGroups_Shoes,
    RenameVertexGroups_Panel,
    gameSelector)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    bpy.types.WindowManager.interface_vars = bpy.props.PointerProperty(type=gameSelector)


    
def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)    
    del bpy.types.WindowManager.interface_vars

if __name__ == "__main__":
    register()
