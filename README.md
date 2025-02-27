# Sp3 Rename
Hello, visitor! Thank you for coming by.

This addon for Blender 3.x allows to rename Vertex Groups to improve compatibility with [TeenageApple's Splatoon 3 character rigs](https://drive.google.com/drive/folders/1GwLTJGT2E3OAJ-XYV2HEyACjJc2gBjaK) (and/or any other applicable Rigify rig!)

## What is this?
In case you wonder what this does and what this means, it's pretty simple! This allows you to use the existing weights of a piece of gear in a Splatoon 3 model ripped from the game files in a way that the rigs by TeenageApple understand. The intent is to make posing for the gear as accurate as possible, while you don't have to massively modify any gear models that you've added. 

## How to install

Installing and enabling the addon is simple! Go to the the Releases tab and download the file that pertains to your Blender version (`4.2` if you're using Blender 4.2 or newer, otherwise `pre-4.2`). It is important to note, __do not extract the zip file__.
- In 4.2 and newer, take the .zip file and drag-and-drop it anywhere in Blender.
- In 4.1 and prior, go to `Edit -> Preferences`. In the Preferences window, go to `Add-ons`, click `Install...`, and locate and install the zip file that you've just downloaded.

Now you should see `Sp3 Rename` among the addons in your list, so enable the checkbox in it.

Alternatively, you can go to `%USERPROFILE%\AppData\Roaming\Blender Foundation\Blender\[version]\scripts\addons\` for pre-4.2 or `%USERPROFILE%\AppData\Roaming\Blender Foundation\Blender\[version]\extensions\user_default\` for 4.2, and extract the `Sp3 Rename` folder of the zip there.

![image](https://github.com/user-attachments/assets/29da5796-c06d-4335-bd2c-c71cf05f976a)


## How to use (clothing)

Now, to actually use the addon, enter Object Mode and add any piece of clothing that you want it, then select it (orange outline). On your keyboard, press N to open the side panel of the viewport if it isn't open already, then look out for a tab labelled `Sp3 Rename`. Click the `Fix Clothes` button to rename all vertex groups in one go, and finally, shift-click the armature/rig and parent it via Armature Deform!

![image](https://github.com/user-attachments/assets/be9cc8bb-83e3-495b-9410-9fea159a3e36)


## How to use (shoes)

There is also a function to prep shoes up too! All you ever need to do is importing the shoe you want to import and select its mesh. Open the N-panel of the viewport, find the `Sp3 Rename` tab, then click the `Fix Shoes` button.
This function not only will fix up Vertex Groups for use with Armature Deform, but it will also automatically position the shoes to the feet of your character (assuming it's all in the origin of the scene's world) and mirror a shoe for the opposite foot.  
And finally, select the shoe's meshes again, shift-click the armature/rig, and parent via Armature Deform! This function will automatically remove the gear from its unnecessary armature.

https://github.com/floatayy/sp3_rename/assets/91428727/d1236251-09e8-45ba-b810-6618f5f5f1e3

## Notes and credits

You may rename all vertex groups for multiple pieces of gear at once, but under the current implementation, this operation must be done in a specific order when you select the objects.
![image](https://github.com/user-attachments/assets/fa5d5236-b902-42bb-9c54-da76a1a6c65a)

This process is not needed for headgear. For headgear, all you do is select the headgear first, shift-click the armature/rig, go to Pose Mode to select the head bone, and parent by Bone.

Compatibility is broken with Splatoon 2 and Sp2 SFM models due to discrepancies caused by differing finger flexes. Please avoid using gloves altogether unless it's Splatoon 3 models or your self-made ones. 

Downloads to the gear models will not be provided.

Script originally written by [piparkaq](https://bsky.app/profile/bankara.ink), side panel implementation by me.
