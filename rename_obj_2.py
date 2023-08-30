import bpy
from bpy.types import Operator

GROUP_DICT_SP2 = {
    'leg1_L': 'DEF-thigh.L',
    'leg1_R': 'DEF-thigh.R',
    'leg1sub_L': 'DEF-thigh.L.001',
    'leg1sub_R': 'DEF-thigh.R.001',
    'leg2_L': 'DEF-shin.L',
    'leg2_R': 'DEF-shin.R',
    'foot_L': 'DEF-foot.L',
    'foot_R': 'DEF-foot.R',
    'leg2sub_L': 'DEF-shin.L.001',
    'leg2sub_R': 'DEF-shin.R.001',
    'toe_L': 'DEF-toe.L',
    'toe_R': 'DEF-toe.R',
    'hip': 'DEF-spine',
    'spine1': 'DEF-spine.001',
    'spine2': 'DEF-spine.002',
    'chest': 'DEF-spine.003',
    'Neck': 'DEF-spine.004',
    'Head': 'DEF-spine.006',
    'shoulder_L': 'DEF-shoulder.L',
    'shoulder_R': 'DEF-shoulder.R',
    'arm1_L': 'DEF-upper_arm.L',
    'arm1_R': 'DEF-upper_arm.R',
    'arm1sub_L': 'DEF-upper_arm.L.001',
    'arm1sub_R': 'DEF-upper_arm.R.001',
    'arm2_L': 'DEF-forearm.L',
    'arm2_R': 'DEF-forearm.R',
    'arm2sub_L': 'DEF-forearm.L.001',
    'arm2sub_R': 'DEF-forearm.R.001',
    'hand_L': 'DEF-hand.L',
    'hand_R': 'DEF-hand.R',
}

SHOE_GROUP_SP2 = {
    "leg2_L": "leg2_R",
    "leg2sub_L": "leg2sub_R",
    "foot_L": "foot_R",
    "toe_L": "toe_R"
}

class RenameVertexGroups_Op_Sp2(Operator):
    """This button does all the magic! (Note: one-at-a-time selections only)"""
    bl_idname = "tentakuruzu.rename_vertex_groups"
    bl_label = "Rename vertex groups"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT":
                return True
        return False

    def execute(self, context):
        groups = context.object.vertex_groups
        lookup_keys = GROUP_DICT_SP2.keys()
        print(lookup_keys)

        for g in groups:
            if g.name in lookup_keys:
                g.name = GROUP_DICT_SP2[g.name]

        return {'FINISHED'}
    
class RenameVertexGroups_Shoes_Sp2(Operator):
    """Only use with shoes!"""
    bl_idname = "tentakuruzu.rename_vertex_groups_shoes"
    bl_label = "Rename and add vertex groups on shoes"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        obj = context.object
        if obj is not None:
            if obj.mode == "OBJECT":
                return True
        return False

    def execute(self, context):
        obj = context.object
        groups = context.object.vertex_groups
        lookup_keys = GROUP_DICT_SP2.keys()
        shoe_keys = SHOE_GROUP_SP2.keys()
        
        for mod in obj.modifiers:
            if mod.type == "MIRROR":
                self.report({"ERROR"}, "Footwear already mirrored and fixed!")
            else:
                bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")
                bpy.ops.object.modifier_remove(modifier="Armature")
                bpy.context.object.rotation_euler = 1.570796, 0, 0
                bpy.context.object.location = 0.101898, 0, 0.382699
                bpy.context.object.scale = 0.126268, 0.126268, 0.126268
                bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
                bpy.ops.object.modifier_add(type="MIRROR")
                bpy.context.object.modifiers["Mirror"].use_mirror_merge = False

        for gc in groups:
            if gc.name in shoe_keys:
                bpy.context.active_object.vertex_groups.new(name=SHOE_GROUP_SP2[gc.name])

        for g in groups:
            if g.name in lookup_keys:
                g.name = GROUP_DICT_SP2[g.name]

        return {'FINISHED'}