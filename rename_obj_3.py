import bpy
from bpy.types import Operator

GROUP_DICT_SP3 = {
    'Leg_1_L': 'DEF-thigh.L',
    'Leg_1_R': 'DEF-thigh.R',
    'Leg_Assist_L': 'DEF-thigh.L.001',
    'Leg_Assist_R': 'DEF-thigh.R.001',
    'Leg_2_L': 'DEF-shin.L',
    'Leg_2_R': 'DEF-shin.R',
    'Ankle_L': 'DEF-foot.L',
    'Ankle_R': 'DEF-foot.R',
    'Ankle_Assist_L': 'DEF-shin.L.001',
    'Ankle_Assist_R': 'DEF-shin.R.001',
    'Toe_L': 'DEF-toe.L',
    'Toe_R': 'DEF-toe.R',
    'Waist': 'DEF-spine',
    'Spine_1': 'DEF-spine.001',
    'Spine_2': 'DEF-spine.002',
    'Spine_3': 'DEF-spine.003',
    'Neck': 'DEF-spine.004',
    'Head': 'DEF-spine.006',
    'Clavicle_L': 'DEF-shoulder.L',
    'Clavicle_R': 'DEF-shoulder.R',
    'Arm_Assist_L': 'DEF-upper_arm.L',
    'Arm_Assist_R': 'DEF-upper_arm.R',
    'Arm_1_L': 'DEF-upper_arm.L.001',
    'Arm_1_R': 'DEF-upper_arm.R.001',
    'Arm_2_L': 'DEF-forearm.L',
    'Arm_2_R': 'DEF-forearm.R',
    'Wrist_Assist_L': 'DEF-forearm.L.001',
    'Wrist_Assist_R': 'DEF-forearm.R.001',
    'Wrist_L': 'DEF-hand.L',
    'Wrist_R': 'DEF-hand.R',
    'Finger_A_1_L': 'DEF-thumb.01.L',
    'Finger_A_2_L': 'DEF-thumb.02.L',
    'Finger_A_3_L': 'DEF-thumb.03.L',
    'Finger_A_1_R': 'DEF-thumb.01.R',
    'Finger_A_2_R': 'DEF-thumb.02.R',
    'Finger_A_3_R': 'DEF-thumb.03.R',
    'Finger_B_1_L': 'DEF-f_index.01.L',
    'Finger_B_2_L': 'DEF-f_index.02.L',
    'Finger_B_3_L': 'DEF-f_index.03.L',
    'Finger_B_1_R': 'DEF-f_index.01.R',
    'Finger_B_2_R': 'DEF-f_index.02.R',
    'Finger_B_3_R': 'DEF-f_index.03.R',
    'Finger_C_1_L': 'DEF-f_middle.01.L',
    'Finger_C_2_L': 'DEF-f_middle.02.L',
    'Finger_C_3_L': 'DEF-f_middle.03.L',
    'Finger_C_1_R': 'DEF-f_middle.01.R',
    'Finger_C_2_R': 'DEF-f_middle.02.R',
    'Finger_C_3_R': 'DEF-f_middle.03.R',
    'Finger_D_1_L': 'DEF-f_ring.01.L',
    'Finger_D_2_L': 'DEF-f_ring.02.L',
    'Finger_D_3_L': 'DEF-f_ring.03.L',
    'Finger_D_1_R': 'DEF-f_ring.01.R',
    'Finger_D_2_R': 'DEF-f_ring.02.R',
    'Finger_D_3_R': 'DEF-f_ring.03.R',
    'Finger_E_1_L': 'DEF-f_pinky.01.L',
    'Finger_E_2_L': 'DEF-f_pinky.02.L',
    'Finger_E_3_L': 'DEF-f_pinky.03.L',
    'Finger_E_1_R': 'DEF-f_pinky.01.R',
    'Finger_E_2_R': 'DEF-f_pinky.02.R',
    'Finger_E_3_R': 'DEF-f_pinky.03.R',
}

SHOE_GROUP_SP3 = {
    "Leg_2_L": "Leg_2_R",
    "Ankle_Assist_L": "Ankle_Assist_R",
    "Ankle_L": "Ankle_R",
    "Toe_L": "Toe_R"
}

RIGHT_ELBOW = {
    "DEF-upper_arm.R.001": "Elbow_R"
}
LEFT_ELBOW = {
    "DEF-upper_arm.L.001": "Elbow_L"
}
RIGHT_KNEE = {
    "DEF-thigh.R.001": "Knee_R"
}
LEFT_KNEE = {
    "DEF-thigh.L.001": "Knee_L"
}

class RenameVertexGroups_Op_Sp3(Operator):
    """This button does all the magic! (Note: one-at-a-time selections only)"""
    bl_idname = "surimi.rename_vertex_groups"
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
        obj = context.object

        groups = context.object.vertex_groups
        lookup_keys = GROUP_DICT_SP3.keys()
        right_elbow = RIGHT_ELBOW.keys() 
        left_elbow = LEFT_ELBOW.keys()
        right_knee = RIGHT_KNEE.keys()
        left_knee = LEFT_KNEE.keys()
        
        bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")

    
        for g in groups:
            if g.name in lookup_keys:
                g.name = GROUP_DICT_SP3[g.name]


        for mod in obj.modifiers:
            if mod.type == "VERTEX_WEIGHT_MIX":
                return {"FINISHED"}
            else:
                for re in groups:
                    if re.name in right_elbow:
                        obj.modifiers.new(name="Right Elbow Fix", type="VERTEX_WEIGHT_MIX")
                        obj.modifiers["Right Elbow Fix"].vertex_group_a = "DEF-forearm.R.001"
                        obj.modifiers["Right Elbow Fix"].vertex_group_b = "Elbow_R"
                        obj.modifiers["Right Elbow Fix"].mix_set = "ALL"
                        obj.modifiers["Right Elbow Fix"].mix_mode = "ADD"
                        while obj.modifiers[0].name != "Right Elbow Fix":
                            bpy.ops.object.modifier_move_up(modifier="Right Elbow Fix")

                for le in groups:
                    if le.name in left_elbow:
                        obj.modifiers.new(name="Left Elbow Fix", type="VERTEX_WEIGHT_MIX")
                        obj.modifiers["Left Elbow Fix"].vertex_group_a = "DEF-forearm.L.001"
                        obj.modifiers["Left Elbow Fix"].vertex_group_b = "Elbow_L"
                        obj.modifiers["Left Elbow Fix"].mix_set = "ALL"
                        obj.modifiers["Left Elbow Fix"].mix_mode = "ADD"
                        while obj.modifiers[0].name != "Left Elbow Fix":
                            bpy.ops.object.modifier_move_up(modifier="Left Elbow Fix")

                for rk in groups:
                    if rk.name in right_knee:
                        obj.modifiers.new(name="Right Knee Fix", type="VERTEX_WEIGHT_MIX")
                        obj.modifiers["Right Knee Fix"].vertex_group_a = "DEF-forearm.R.001"
                        obj.modifiers["Right Knee Fix"].vertex_group_b = "Knee_R"
                        obj.modifiers["Right Knee Fix"].mix_set = "ALL"
                        obj.modifiers["Right Knee Fix"].mix_mode = "ADD"
                        while obj.modifiers[0].name != "Right Knee Fix":
                            bpy.ops.object.modifier_move_up(modifier="Right Knee Fix")

                for lk in groups:
                    if lk.name in left_knee:
                        obj.modifiers.new(name="Left Knee Fix", type="VERTEX_WEIGHT_MIX")
                        obj.modifiers["Left Knee Fix"].vertex_group_a = "DEF-forearm.L.001"
                        obj.modifiers["Left Knee Fix"].vertex_group_b = "Knee_L"
                        obj.modifiers["Left Knee Fix"].mix_set = "ALL"
                        obj.modifiers["Left Knee Fix"].mix_mode = "ADD"
                        while obj.modifiers[0].name != "Left Knee Fix":
                            bpy.ops.object.modifier_move_up(modifier="Left Knee Fix")

        return {'FINISHED'}
    
class RenameVertexGroups_Shoes_Sp3(Operator):
    """Only use with shoes!"""
    bl_idname = "surimi.rename_vertex_groups_shoes_sp3"
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
        lookup_keys = GROUP_DICT_SP3.keys()
        shoe_keys = SHOE_GROUP_SP3.keys()
        
        for mod in obj.modifiers:
            if mod.type == "MIRROR":
                self.report({"ERROR"}, "Footwear already mirrored and fixed!")
            else:
                bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")
                bpy.ops.object.modifier_remove(modifier="Armature")
                bpy.context.object.rotation_euler = 1.570796, 0, 0
                bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
                bpy.context.object.location = 0.10216, 0, 0.20971
                bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
                bpy.ops.object.modifier_add(type="MIRROR")
                bpy.context.object.modifiers["Mirror"].use_mirror_merge = False

        for gc in groups:
            if gc.name in shoe_keys:
                bpy.context.active_object.vertex_groups.new(name=SHOE_GROUP_SP3[gc.name])

        for g in groups:
            if g.name in lookup_keys:
                g.name = GROUP_DICT_SP3[g.name]

        return {'FINISHED'}