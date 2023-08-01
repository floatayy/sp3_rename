# Sp3 Rename
Hello, visitor! Thank you for coming by.

This addon for Blender 3.x allows to rename Vertex Groups to improve compatibility with [TeenageApple's Splatoon 3 character rigs](https://drive.google.com/drive/folders/1GwLTJGT2E3OAJ-XYV2HEyACjJc2gBjaK).

## What is this?
In case you wonder what this does and what this means, it's pretty simple! This allows you to use the existing weights of a piece of gear in a Splatoon 3 model ripped from the game files in a way that the rigs by TeenageApple understand. The intent to make posing for the gear as accurate as possible, while you don't have to massively modify any gear models that you've added. 

## How to use

Firstly, install and enable the addon. Download this repo as a zip file (or head to the releases tab, whichever works best for you). It is important to note, __do not extract the zip file__. Open Blender and go to `Edit -> Preferences`. In the Preferences window, go to `Add-ons`, click `Install...`, and locate and install the zip file that you've just downloaded. Now you should see `Sp3 Rename` among the addons in your list, so enable the checkbox in it.

Alternatively, you can go to `%USERPROFILE%\AppData\Roaming\Blender Foundation\Blender\[version]\scripts\addons\` and extract the `Sp3 Rename` folder of the zip there.

![image](https://github.com/floatayy/sp3_rename/assets/91428727/7708265e-2e22-40b7-8401-6c23b267df54)

Now, to actually use the addon, be in Object Mode and add any piece of gear that you want, whether it's clothing or shoes, then select it (orange outline). On your keyboard, press N to open the side panel of the viewport if it isn't open already, then look out for a tab labelled `Sp3 Rename`. Click the `Rename All Vertex Groups` button to rename all vertex groups in one go, and finally, shift-click the armature/rig and parent it via Armature Deform!

![image](https://github.com/floatayy/sp3_rename/assets/91428727/0f644774-673f-4632-91a9-acff6d3163ca)

## Notes and credits

You can only rename all vertex groups for one piece of gear at a time, so you have to click a piece of gear once, click the button, and repeat for the next gear, but it's a pretty quick process so it's only a matter of a few clicks and seconds to get things up and running.

This process is not needed for headgear. For headgear, all you do is select the headgear first, shift-click the armature/rig, go to Pose Mode to select the head bone, and parent by Bone.

Downloads to the gear models will not be provided.

Script originally written by [piparkaq](https://twitter.com/piparkaq), side panel implementation by me.
