# files-for-vrm-porting-guide
Repo to download helpful files for Crowbar compilation and vmt editing. The associated Steam Guide can be found here: [insert link]
You can download all of these by clicking the green 'Code' button and selecting 'Download ZIP'.

1) basewarp.vtf is used by the vmt files as a sort of base textire and is necesary to correctly display the textures in-game.
2) samplea_physics.smd/samplec_physics.smd are physics models from Deadwater's Guide edited by myself to be closer to the default Vroid female/male bodies. Using one of these smds instead of the one provided in Deadwater's guide reduces the overall time needed to edit the physics smd.
3) vmts.txt contains vmt parameters for each part of a Vroid model. It includes code defining parameters for the Head, Face, Body, Clothing, and Hair.
4) optional contains two files: faceflexes.txt and physconstraints.txt. For those who wish to include face flexes and jigglebones, these files include parameters that are to be inserted into and edited in your playermodel .qc file.
