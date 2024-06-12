# vroid-to-gmod-files
Repo to download files necessary for reference importing, Crowbar compilation, .vmt editing, etc. The associated Steam Guide can be found here: https://steamcommunity.com/sharedfiles/filedetails/?id=3079067248
You can download all of this in one go by clicking the green 'Code' button and selecting 'Download ZIP'.
Troubleshooting Q&A for the guide can be found here: https://github.com/Althories/vrm-porting-guide-troubleshooting

1) resources contains materials to assist with .qc editing and process automation.
> physconstraints.txt contains parameters to be pasted into the .qc file for jigglebones.
> RenameScript.py is imported into Blender. It renames the Vroid armature bones to ValveBiped counterparts, and removes underscores in shape key names.
> vmts.txt contains vmt parameters for interpreting each texture of the model for the Source Engine. It includes code defining parameters for the Head, Face, Body, Clothing, and Hair.
2) smd references contains .smd files to be imported into blender for use as reference material.
> male_07_reference.smd is imported as a size reference when scaling the Vroid model to standard Garry's Mod size.
> c_arms_citizen.smd and c_arms_citizen_hands.smd are used as references for the optional process of making more accurate viewmodel arms.
3) your_model_pm is a starter template for what will ultimately be inserted into the main Garry's Mod folder for playermodel testing.
> base.vtf is used by the vmt files for the $lightwarptexture parameter. It's necessary to include this file if you want your model to have the same shading appearance that it does in Vroid Studio.
> yourmodel_pm.lua tells Garry's Mod how to treat your model in the playermodel selector.
4) compile folder template contains files necessary for playermodel compilation in Crowbar.
> pm compile.qc is used by Crowbar to compile your model.
> fembase_physics.dmx/mascbase_physics.dmx are physics models from Deadwater's Guide edited by myself to be closer to the default Vroid female/male bodies. Using one of these smds instead of the one provided in Deadwater's guide reduces the overall time needed to edit the physics smd.
5) c carms compile folder template contains the .qc file for making viewmodel arms.
> pm_arms.qc is used by Crowbar to compile the viewmodel arms.
