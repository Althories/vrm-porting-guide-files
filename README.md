# vroid-to-gmod-files
Repo to download helpful files for Crowbar compilation and vmt editing. The associated Steam Guide can be found here: https://steamcommunity.com/sharedfiles/filedetails/?id=3079067248
You can download all of these by clicking the green 'Code' button and selecting 'Download ZIP'.
Troubleshooting Q&A for the guide can be found here: https://github.com/Althories/vrm-porting-guide-troubleshooting

1) base.vtf is used by the vmt files for the $lightwarptexture parameter. It's necessary to include this file if you want your model to have the same shading appearance that it does in Vroid Studio.
2) samplea_physics.smd/samplec_physics.smd are physics models from Deadwater's Guide edited by myself to be closer to the default Vroid female/male bodies. Using one of these smds instead of the one provided in Deadwater's guide reduces the overall time needed to edit the physics smd.
3) vmts.txt contains vmt parameters for interpreting each texture of the model for the Source Engine. It includes code defining parameters for the Head, Face, Body, Clothing, and Hair.
4) optional contains two files: faceflexes.txt and physconstraints.txt. For those who wish to include face flexes and jigglebones, these files include parameters that are to be inserted into and edited in your playermodel .qc file.
