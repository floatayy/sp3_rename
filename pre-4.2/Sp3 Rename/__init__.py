bl_info = {
    "name": "Sp3 Rename",
    "description": "Rename Vertex Groups in ripped Splatoon 3 models to make them compatible with TeenageApple's Splatoon 3 character rigs.",
    "author": "piparkaq (original Sp3 script), Floaty (UI & Sp2 implementation)",
    "version": (3, 0, 0),
    "blender": (3, 0, 0),
    "category": "Object",
    "doc_url": "https://github.com/floatayy/sp3_rename",
}

import bpy

from bpy.types import Panel, Operator, PropertyGroup, EnumProperty

# For the "Splat 3" checks
GROUP_DICT_SP3 = {
    "Leg_1_L": "DEF-thigh.L",
    "Leg_1_R": "DEF-thigh.R",
    "Leg_Assist_L": "DEF-thigh.L.001",
    "Leg_Assist_R": "DEF-thigh.R.001",
    "Leg_2_L": "DEF-shin.L",
    "Leg_2_R": "DEF-shin.R",
    "Ankle_L": "DEF-foot.L",
    "Ankle_R": "DEF-foot.R",
    "Ankle_Assist_L": "DEF-shin.L.001",
    "Ankle_Assist_R": "DEF-shin.R.001",
    "Toe_L": "DEF-toe.L",
    "Toe_R": "DEF-toe.R",
    "Waist": "DEF-spine",
    "Spine_1": "DEF-spine.001",
    "Spine_2": "DEF-spine.002",
    "Spine_3": "DEF-spine.003",
    "Neck": "DEF-spine.004",
    "Head": "DEF-spine.006",
    "Clavicle_L": "DEF-shoulder.L",
    "Clavicle_R": "DEF-shoulder.R",
    "Arm_Assist_L": "DEF-upper_arm.L",
    "Arm_Assist_R": "DEF-upper_arm.R",
    "Arm_1_L": "DEF-upper_arm.L.001",
    "Arm_1_R": "DEF-upper_arm.R.001",
    "Arm_2_L": "DEF-forearm.L",
    "Arm_2_R": "DEF-forearm.R",
    "Wrist_Assist_L": "DEF-forearm.L.001",
    "Wrist_Assist_R": "DEF-forearm.R.001",
    "Wrist_L": "DEF-hand.L",
    "Wrist_R": "DEF-hand.R",
    "Finger_A_1_L": "DEF-thumb.01.L",
    "Finger_A_2_L": "DEF-thumb.02.L",
    "Finger_A_3_L": "DEF-thumb.03.L",
    "Finger_A_1_R": "DEF-thumb.01.R",
    "Finger_A_2_R": "DEF-thumb.02.R",
    "Finger_A_3_R": "DEF-thumb.03.R",
    "Finger_B_1_L": "DEF-f_index.01.L",
    "Finger_B_2_L": "DEF-f_index.02.L",
    "Finger_B_3_L": "DEF-f_index.03.L",
    "Finger_B_1_R": "DEF-f_index.01.R",
    "Finger_B_2_R": "DEF-f_index.02.R",
    "Finger_B_3_R": "DEF-f_index.03.R",
    "Finger_C_1_L": "DEF-f_middle.01.L",
    "Finger_C_2_L": "DEF-f_middle.02.L",
    "Finger_C_3_L": "DEF-f_middle.03.L",
    "Finger_C_1_R": "DEF-f_middle.01.R",
    "Finger_C_2_R": "DEF-f_middle.02.R",
    "Finger_C_3_R": "DEF-f_middle.03.R",
    "Finger_D_1_L": "DEF-f_ring.01.L",
    "Finger_D_2_L": "DEF-f_ring.02.L",
    "Finger_D_3_L": "DEF-f_ring.03.L",
    "Finger_D_1_R": "DEF-f_ring.01.R",
    "Finger_D_2_R": "DEF-f_ring.02.R",
    "Finger_D_3_R": "DEF-f_ring.03.R",
    "Finger_E_1_L": "DEF-f_pinky.01.L",
    "Finger_E_2_L": "DEF-f_pinky.02.L",
    "Finger_E_3_L": "DEF-f_pinky.03.L",
    "Finger_E_1_R": "DEF-f_pinky.01.R",
    "Finger_E_2_R": "DEF-f_pinky.02.R",
    "Finger_E_3_R": "DEF-f_pinky.03.R",
}
SHOE_GROUP_SP3 = {
    "Leg_2_L": "Leg_2_R",
    "Ankle_Assist_L": "Ankle_Assist_R",
    "Ankle_L": "Ankle_R",
    "Toe_L": "Toe_R",
}

# This helps determine what Vertex Groups should be assigned for the Weight Vertex Mix modifiers
WEIGHTS_FIX_SLEEVES_SP3 = {
    "Elbow_R": "DEF-upper_arm.R.001",
    "Elbow_L": "DEF-upper_arm.L.001"
    }
WEIGHTS_FIX_KNEES_SP3 = {
    "Knee_R": "DEF-thigh.R.001",
    "Knee_L": "DEF-thigh.L.001"
}

# For the "Splat 2" checks
GROUP_DICT_SP2 = {
    "leg1_L": "DEF-thigh.L",
    "leg1_R": "DEF-thigh.R",
    "leg1sub_L": "DEF-thigh.L.001",
    "leg1sub_R": "DEF-thigh.R.001",
    "leg2_L": "DEF-shin.L",
    "leg2_R": "DEF-shin.R",
    "foot_L": "DEF-foot.L",
    "foot_R": "DEF-foot.R",
    "leg2sub_L": "DEF-shin.L.001",
    "leg2sub_R": "DEF-shin.R.001",
    "toe_L": "DEF-toe.L",
    "toe_R": "DEF-toe.R",
    "hip": "DEF-spine",
    "spine1": "DEF-spine.001",
    "spine2": "DEF-spine.002",
    "chest": "DEF-spine.003",
    "neck": "DEF-spine.004",
    "head": "DEF-spine.006",
    "Neck": "DEF-spine.004",
    "Head": "DEF-spine.006",
    "shoulder_L": "DEF-shoulder.L",
    "shoulder_R": "DEF-shoulder.R",
    "arm1_L": "DEF-upper_arm.L",
    "arm1_R": "DEF-upper_arm.R",
    "arm1sub_L": "DEF-upper_arm.L.001",
    "arm1sub_R": "DEF-upper_arm.R.001",
    "arm2_L": "DEF-forearm.L",
    "arm2_R": "DEF-forearm.R",
    "arm2sub_L": "DEF-forearm.L.001",
    "arm2sub_R": "DEF-forearm.R.001",
    "hand_L": "DEF-hand.L",
    "hand_R": "DEF-hand.R",
}
SHOE_GROUP_SP2 = {
    "leg2_L": "leg2_R",
    "leg2sub_L": "leg2sub_R",
    "foot_L": "foot_R",
    "toe_L": "toe_R",
}


class gameSelector(bpy.types.PropertyGroup):
    gameSelect: bpy.props.EnumProperty(
        items=[
            (
                "Sp2",
                "Splat 2",
                "Convert Splatoon 2 models (asset rips) to rig weights",
                "",
                0,
            ),
            (
                "Sp3",
                "Splat 3",
                "Convert Splatoon 3 models (asset rips) to rig weights",
                "",
                1,
            ),
        ],
        default="Sp3",
    )


class RenameVertexGroups_Panel(Panel):
    bl_idname = "sp3.panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Sp3 Rename"
    bl_category = "Sp3 Rename"

    def draw(self, context):

        layout = self.layout

        col = layout.column(align=True)
        row = col.row(align=True)
        row.label(text="Model Source")
        col2 = layout.column(align=True)
        row2 = col2.row(align=True)
        row2.prop(context.window_manager.interface_vars, "gameSelect", expand=True)
        col3 = layout.column(align=True)
        row3 = col3.row(align=True)
        row3.label(text="Rename All Vertex Groups")
        col4 = layout.column(align=True)
        row4 = col4.row(align=True)
        row4.operator("surimi.rename_vertex_groups", text="Fix Clothes")
        row4.operator("surimi.rename_vertex_shoes", text="Fix Shoes")

    def execute(self, context):
        gameSelected = context.window_manager.interface_vars.gameSelect
        groups = context.object.vertex_groups
        if gameSelected == "Sp2":
            lookup_keys = GROUP_DICT_SP2.keys()
            
        if gameSelected == "Sp3":
            lookup_keys = GROUP_DICT_SP3.keys()

        for g in groups:
            if g.name in lookup_keys:
                g.name = GROUP_DICT_SP3[g.name]

        return {"FINISHED"}


class RenameVertexGroups_Op(Operator):
    """This button does all the magic!"""

    bl_idname = "surimi.rename_vertex_groups"
    bl_label = "Rename vertex groups"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT":
                return True
        return False

    def execute(self, context):
        
        for obj in context.selected_objects:
            
            groups = obj.vertex_groups
            lookup_keys_sp2 = GROUP_DICT_SP2.keys()
            lookup_keys_sp3 = GROUP_DICT_SP3.keys()

            gameSelected = str(context.window_manager.interface_vars.gameSelect)

            if gameSelected == "Sp2":
                for g in groups:
                    if g.name in lookup_keys_sp2:
                        g.name = GROUP_DICT_SP2[g.name]

                return {"FINISHED"}
            else: pass

            if gameSelected == "Sp3":
                for g in groups:
                    if g.name in lookup_keys_sp3:
                        g.name = GROUP_DICT_SP3[g.name]
                        
# The following checks if the active object has any of the "Elbow" or "Knee" Vertex Groups.
# If such Vertex Group is present, a new "Vertex Weight Mix" modifier which points to one of the newly renamed Vertex Groups to A and the corresponding Elbow/Knee Vertex Group to B will be added.
# If such Vertex Group isn't present, the current check will be passed to the next check, and so on until all checks are complete.
# To ensure the best of functionality, all applicable "Vertex Weight Mix" modifiers will be moved to the top of the stack.
# In case of a multi-object operation, the modifiers will only be added to the active object (aka the last selected object) as a countermeasure against Blender freezing and seemingly crashing if "obj" were to be referred. To compensate, "obj1" is used to refer to the active object instead.
            obj1 = context.object
            groups1 = context.object.vertex_groups
            print(groups1.keys())

            if "Knee_R" in groups1.keys():
                obj1.modifiers.new(name="Right Knee Fix", type="VERTEX_WEIGHT_MIX")
                obj1.modifiers["Right Knee Fix"].vertex_group_a = ("DEF-thigh.R.001")
                obj1.modifiers["Right Knee Fix"].vertex_group_b = "Knee_R"
                obj1.modifiers["Right Knee Fix"].mix_set = "ALL"
                obj1.modifiers["Right Knee Fix"].mix_mode = "ADD"
                while obj1.modifiers[0].name != "Right Knee Fix":
                    bpy.ops.object.modifier_move_up(modifier="Right Knee Fix")
            else: pass

            if "Knee_L" in groups1.keys():
                obj1.modifiers.new(name="Left Knee Fix", type="VERTEX_WEIGHT_MIX")
                obj1.modifiers["Left Knee Fix"].vertex_group_a = ("DEF-thigh.L.001")
                obj1.modifiers["Left Knee Fix"].vertex_group_b = "Knee_L"
                obj1.modifiers["Left Knee Fix"].mix_set = "ALL"
                obj1.modifiers["Left Knee Fix"].mix_mode = "ADD"
                while obj1.modifiers[0].name != "Left Knee Fix":
                    bpy.ops.object.modifier_move_up(modifier="Left Knee Fix")
            else: pass

            if "Elbow_R" in groups1.keys():
                obj1.modifiers.new(name="Right Elbow Fix", type="VERTEX_WEIGHT_MIX")
                obj1.modifiers["Right Elbow Fix"].vertex_group_a = ("DEF-forearm.R.001")
                obj1.modifiers["Right Elbow Fix"].vertex_group_b = "Elbow_R"
                obj1.modifiers["Right Elbow Fix"].mix_set = "ALL"
                obj1.modifiers["Right Elbow Fix"].mix_mode = "ADD"
                while obj1.modifiers[0].name != "Right Elbow Fix":
                    bpy.ops.object.modifier_move_up(modifier="Right Elbow Fix")
            else: pass

            if "Elbow_L" in groups1.keys():
                obj1.modifiers.new(name="Left Elbow Fix", type="VERTEX_WEIGHT_MIX")
                obj1.modifiers["Left Elbow Fix"].vertex_group_a = ("DEF-forearm.L.001")
                obj1.modifiers["Left Elbow Fix"].vertex_group_b = "Elbow_L"
                obj1.modifiers["Left Elbow Fix"].mix_set = "ALL"
                obj1.modifiers["Left Elbow Fix"].mix_mode = "ADD"
                while obj1.modifiers[0].name != "Left Elbow Fix":
                    bpy.ops.object.modifier_move_up(modifier="Left Elbow Fix")
            else: pass

        return {"FINISHED"}
                


class RenameVertexGroups_Shoes(Operator):
    """Only use with shoes!"""

    bl_idname = "surimi.rename_vertex_shoes"
    bl_label = "Rename and add vertex groups on shoes"
    bl_options = {"REGISTER", "UNDO"}

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
        lookup_keys_sp3 = GROUP_DICT_SP3.keys()
        shoe_keys_sp3 = SHOE_GROUP_SP3.keys()
        lookup_keys_sp2 = GROUP_DICT_SP2.keys()
        shoe_keys_sp2 = GROUP_DICT_SP2.keys()

# This checks if the name of the selected object starts with "Shs" ("Shoes") or "Base_low" (for those few exceptional cases).
# If both the "Shs" and "Base_low" turn out to be false, the operation will be cancelled and the user will be told to select the other, possibly appropriate, operation instead.
#  
#       isShs = obj.name.startswith("Shs")
#       isBaseLow = obj.name.startswith("Base_low")
#       if (isShs == False) & (isBaseLow == False):
#           self.report({"ERROR"}, "'" + obj.name + "' is not shoes! Did you mean to click 'Fix Clothes'?")
#           return {"CANCELLED"}

# This compares the Vertex Groups of the selected object(s) with the "lookup keys" for both the "Splat 2" and the "Splat 3" checks.
# If both the comparisons fail in that the Vertex Groups don't match with the "loopup keys", the operation will be cancelled and the user will be told to select the other, possibly more appropriate, operation instead.
        for gc in groups:
            if not gc.name in shoe_keys_sp3 and not gc.name in shoe_keys_sp2:
                self.report({"ERROR"}, "'" + obj.name + "' is not shoes! Did you mean to click 'Fix Clothes'?")
                return {"CANCELLED"}

# Is "Splat 3" selected as the Model Source?
        if context.window_manager.interface_vars.gameSelect == "Sp3":
            for gc in groups:
                if gc.name in shoe_keys_sp3:
                    bpy.context.active_object.vertex_groups.new(
                        name=SHOE_GROUP_SP3[gc.name]
                    )
            for g in groups:
                if g.name in lookup_keys_sp3:
                    g.name = GROUP_DICT_SP3[g.name]
        else:
# If not, is "Splat 2" selected?
            if context.window_manager.interface_vars.gameSelect == "Sp2":
                for gc2 in groups:
                    if gc2.name in shoe_keys_sp2:
                        bpy.context.active_object.vertex_groups.new(
                            name=SHOE_GROUP_SP2[gc2.name]
                        )

            for g2 in groups:
                if g2.name in lookup_keys_sp2:
                    g2.name = GROUP_DICT_SP2[g2.name]

# This removes any parenting relations with the original Armature object of the mesh and the pre-added Armature modifier. 
# In exchange, it aligns/applies the mesh to the feet of the character in location and rotation, and it adds a Mirror modifier (if not present) with merging disabled.
# If this is a "Splat 2" fix, it will also scale down the mesh to the correct size in relation to the Splat 3 in-game models.
        for mod in obj.modifiers:
            bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")
            bpy.ops.object.modifier_remove(modifier="Armature")
            bpy.context.object.rotation_euler = 1.570796, 0, 0
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
            bpy.context.object.location = 0.10216, 0, 0.20971
            if context.window_manager.interface_vars.gameSelect == "Sp2": bpy.context.object.scale = 0.126268, 0.126268, 0.126268
            bpy.ops.view3d.snap_cursor_to_center()
            bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
            if mod.type != "MIRROR": bpy.ops.object.modifier_add(type="MIRROR")
            bpy.context.object.modifiers["Mirror"].use_mirror_merge = False

        return {"FINISHED"}

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
