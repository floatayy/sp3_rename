import bpy
from bpy.types import Operator

GROUP_DICT = {
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

class RenameVertexGroups_Op(Operator):
    """Test"""
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
        groups = context.object.vertex_groups
        lookup_keys = GROUP_DICT.keys()
        print(lookup_keys)

        for g in groups:
            if g.name in lookup_keys:
                g.name = GROUP_DICT[g.name]

        return {'FINISHED'}