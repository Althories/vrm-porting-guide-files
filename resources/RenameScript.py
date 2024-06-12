
#The Original Author of part of this script is Arficial Light. Check out their channel! 
#Channel - https://www.youtube.com/@ArtificialLight

import bpy
from bpy.types import (Panel,Operator)
import math

#Shape key renaming code provided by StackExchange user Leander - https://blender.stackexchange.com/users/30849/leander
#Removes underscores from the shape keys
# get the selected object
selected_object = bpy.context.object

# get its shapekeys
shape_keys = selected_object.data.shape_keys.key_blocks

# loop through shapekeys and replace the names
for key in shape_keys:
    key.name = key.name.replace("_", "F")
#End of Leander code
#The following code has also been edited by steam user @nombremuyoriginal to fit our purposes.
#Steam page - https://steamcommunity.com/profiles/76561199388415699

class Button(bpy.types.Operator):
    """Make Sure to Select the Armature"""
    bl_idname = "rnm.1"
    bl_label = "RENAME"
    
    def execute(self, context):
        context = bpy.context
        obj = context.object

        namelist = [
        ("J_Bip_C_Chest", "ValveBiped.Bip01_Spine2"),
        ("J_Bip_C_UpperChest","ValveBiped.Bip01_Spine4"),
        ("J_Bip_C_Head","ValveBiped.Bip01_Head1"),
        ("J_Bip_C_Neck","ValveBiped.Bip01_Neck1"),
        ("J_Bip_C_Spine","ValveBiped.Bip01_Spine"),
        ("J_Bip_C_Hips","ValveBiped.Bip01_Pelvis"),
        ("J_Bip_L_UpperLeg","ValveBiped.Bip01_L_Thigh"),
        ("J_Bip_R_UpperLeg","ValveBiped.Bip01_R_Thigh"),
        ("J_Bip_L_LowerLeg","ValveBiped.Bip01_L_Calf"),
        ("J_Bip_R_LowerLeg","ValveBiped.Bip01_R_Calf"),
        ("J_Bip_R_Foot","ValveBiped.Bip01_R_Foot"),
        ("J_Bip_L_Foot","ValveBiped.Bip01_L_Foot"),
        ("J_Bip_R_ToeBase","ValveBiped.Bip01_R_Toe0"),
        ("J_Bip_L_ToeBase","ValveBiped.Bip01_L_Toe0"),
        ("J_Bip_L_Shoulder","ValveBiped.Bip01_L_Clavicle"),
        ("J_Bip_R_Shoulder","ValveBiped.Bip01_R_Clavicle"),
        ("J_Bip_L_UpperArm","ValveBiped.Bip01_L_UpperArm"),
        ("J_Bip_R_UpperArm","ValveBiped.Bip01_R_UpperArm"),
        ("J_Bip_L_LowerArm","ValveBiped.Bip01_L_Forearm"),
        ("J_Bip_R_LowerArm","ValveBiped.Bip01_R_Forearm"),
        ("J_Bip_L_Hand","ValveBiped.Bip01_L_Hand"),
        ("J_Bip_R_Hand","ValveBiped.Bip01_R_Hand"),

        ("J_Bip_L_Thumb1","ValveBiped.Bip01_L_Finger0"),
        ("J_Bip_R_Thumb1","ValveBiped.Bip01_R_Finger0"),
        ("J_Bip_L_Thumb2","ValveBiped.Bip01_L_Finger01"),
        ("J_Bip_R_Thumb2","ValveBiped.Bip01_R_Finger01"),
        ("J_Bip_L_Thumb3","ValveBiped.Bip01_L_Finger02"),
        ("J_Bip_R_Thumb3","ValveBiped.Bip01_R_Finger02"),

        ("J_Bip_L_Index1","ValveBiped.Bip01_L_Finger1"),
        ("J_Bip_R_Index1","ValveBiped.Bip01_R_Finger1"),
        ("J_Bip_L_Index2","ValveBiped.Bip01_L_Finger11"),
        ("J_Bip_R_Index2","ValveBiped.Bip01_R_Finger11"),
        ("J_Bip_L_Index3","ValveBiped.Bip01_L_Finger12"),
        ("J_Bip_R_Index3","ValveBiped.Bip01_R_Finger12"),

        ("J_Bip_L_Middle1","ValveBiped.Bip01_L_Finger2"),
        ("J_Bip_R_Middle1","ValveBiped.Bip01_R_Finger2"),
        ("J_Bip_L_Middle2","ValveBiped.Bip01_L_Finger21"),
        ("J_Bip_R_Middle2","ValveBiped.Bip01_R_Finger21"),
        ("J_Bip_L_Middle3","ValveBiped.Bip01_L_Finger22"),
        ("J_Bip_R_Middle3","ValveBiped.Bip01_R_Finger22"),

        ("J_Bip_L_Ring1","ValveBiped.Bip01_L_Finger3"),
        ("J_Bip_R_Ring1","ValveBiped.Bip01_R_Finger3"),
        ("J_Bip_L_Ring2","ValveBiped.Bip01_L_Finger31"),
        ("J_Bip_R_Ring2","ValveBiped.Bip01_R_Finger31"),
        ("J_Bip_L_Ring3","ValveBiped.Bip01_L_Finger32"),
        ("J_Bip_R_Ring3","ValveBiped.Bip01_R_Finger32"),

        ("J_Bip_L_Little1","ValveBiped.Bip01_L_Finger4"),
        ("J_Bip_R_Little1","ValveBiped.Bip01_R_Finger4"),
        ("J_Bip_L_Little2","ValveBiped.Bip01_L_Finger41"),
        ("J_Bip_R_Little2","ValveBiped.Bip01_R_Finger41"),
        ("J_Bip_L_Little3","ValveBiped.Bip01_L_Finger42"),
        ("J_Bip_R_Little3","ValveBiped.Bip01_R_Finger42"),

        ]
        for name, newname in namelist:
            # get the pose bone with name
            pb = obj.pose.bones.get(name)
            # continue if no bone of that name
            if pb is None:
                continue
            # rename
            pb.name = newname

        bpy.ops.object.mode_set(mode='OBJECT') 
        return {'FINISHED'}
            
class Panel(bpy.types.Panel):
    bl_label = "Rename Vroid Bones for ValveBiped"
    bl_idname = "OBJECT_PT_Rename"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "VRM to ValveBiped"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator(Button.bl_idname,text="RENAME", icon='MENU_PANEL')            

from bpy.utils import register_class, unregister_class
_classes=[
        Button,
        Panel
]
def register():
    for cls in _classes:
        register_class(cls)  

def unregister():
    
    for cls in _classes:
        unregister_class(cls)   
if __name__ == "__main__":
    register()
