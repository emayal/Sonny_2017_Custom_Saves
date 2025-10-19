# Sonny (2017) Custom Saves

- [Alternative starting strain](./Alternative_Starting_Strain/README.md)
- [Zone 8](./Zone_8/README.md)

## Important stuff!

*Note: My readmes use font colors which are not visible in Github. Use any editor with markdown support instead if you want to read it locally, for example VS Code.*

This repository contains all my custom save files, which will work on the vanilla base game of Sonny (2017). A save converter in the form of a python script is also included, which will convert it to a more "readable" format. 

- As far as I can tell, these custom saves will only work with the Steam version of the game. The iOS and Itch version uses completely different save formats, and I have no clue how the Android saves work (plus, Android version is dead :skull:)
- In most saves you get different starter abilities, for unit saves it will be their own abilities. You will lose them forever if you remove them or respec, so be careful! Making backups of the save can be a good idea as a replacement for respec.
- I disabled most tutorials in the game, mostly to make the above issue less painful.

### About alternate starting strains specifically

- These saves starts with 2 strains unlocked instead of 1. This is because when opening the "Skill" menu, the game automatically shows the <font color="#ff4242">**Physical**</font> strain. To access other strains, you must use the buttons at the bottom of the strain tree. These are only enabled if you have at least 2 strains unlocked. Not being able to access your chosen strain means that it is impossible to unlock and upgrade abilities from it. This is why I provide multiple saves for the same 1st strain, each with a different 2nd strain.
- Related to above, when picking a strain after beating Corruptor in Zone 2, the picked strain becomes the 3rd strain temporarily. After beating Celestia in Zone 5, you will pick a strain again. The picked strain will replace your first pick after Zone 2 as the new 3rd strain, rather than becoming a 4th strain. This is because the game hard codes the player's maximum amount of strains to 3, and in cases such as this the game simply replaces the latest strain pick. To avoid issues, do not learn abilities from the 3rd strains between Zone 3-5, since your "true" 3rd strain will be picked after Zone 5 as normal.

### About unit saves specifically (Zone 8)

- You start with Zone 0 items equipped, because most units except Sonny have poor stats at level 1. Without them, most saves wouldn't be able to beat the very first stage! Starting cash has been reduced ($100 -> $25) to compensate for this.
- I added Sonny to the party list, because you need to have Sonny active in order to trigger the autowin cutscene against Vendara 1 in Zone 1. Trying to beat the stage normally would otherwise be extremely difficult. Unfortunately, Sonny has no abilities coded as an A.I. unit, so they are useless outside of Vendara 1.
- Evolution will most likely be disabled on unit saves. It is basically hard coded in the game that only Sonny can use Evolution.

## Instructions

### Download

Clone this repo, or use the "Download ZIP" option from the green "Code" button.

### Find the save folder

1. Find where your Steam base folder (not install folder!) is located. ([Source](https://www.pcgamingwiki.com/wiki/Glossary:Game_data#Steam_client))
    - 64-bit Windows: `C:\Program Files (x86)\Steam`
    - 32-bit Windows: `C:\Program Files\Steam`
    - macOS: `~/Library/Application Support/Steam/`
    - Linux: Typically `~/.local/share/Steam`
2. (*If multiple Steam users have logged in on your PC*) Find out your Steam user ID (*steamID64* or *steamID3*). ([Source](https://www.pcgamingwiki.com/wiki/Glossary:Game_data#User_ID))
    1. On the Steam client, click on your profile at the top right corner.
    2. Select "Account Details"
    3. Your *steamID64* is directly under your account name
    4. Typically you are looking for your *steamID64*, but for some (including me) it is *steamID3* instead. In that case, use [STEAMID I/O](https://steamid.io/) and search with your steamID64.
3. The saves are stored in this folder: `<STEAM-FOLDER>/userdata/<USER-ID>/586750/remote`, where `<STEAM-FOLDER>` is your Steam folder and `<USER-ID>` is your Steam user ID. If only one Steam user has logged in to your PC, then there will only be one `<USER-ID>` folder in `userdata`.
4. (*Optional*) Save `<STEAM-FOLDER>/userdata/<USER-ID>/586750/remote` as a shortcut somewhere on your PC for easier access.

*Note: 586750 is the game ID for Sonny (2017)*

### Installing the custom saves

After picking the save file you wanna play:

1. Copy and paste the custom save into the save folder.
2. Rename the save file to "SN1_", "SN2_" or "SN3_", this corresponds to each save slot. If necessary, delete or rename the old saves.

The custom saves can be uninstalled by simply deleting them, which can also be done from the in-game menu.

### How to use the save converter

*SAVE CONVERTER IS NOT FINISHED!*

You need to have python installed to use the save converter. To check if you have it installed, open up a terminal and execute this command: `python --version`. If no version number pops up, python is not installed. In that case, download the latest version [here](https://www.python.org/) (Windows & macOS). Python should be pre-installed on most Linux distros, if not then use the distros package manager. 

1. Place the save file (ex. `SN1_Spartan`) you want to convert in the same folder as the python script `save_reader.py`
2. Open the script with any editor and change the value of `SAVENAME` to the name of the save file you want to convert (ex. `FILENAME = "SN1_Spartan"`). Do not forget the quotation symbols! (`""`)
3. Save the script. Then, run the it using the terminal: `python save_reader.py`.
4. The save file's contents is written to a new file, `Sonny_2017_Save.txt`, in a more "readable" format.

*Note: Converter only goes one way, the other way will be added in a future update*

## (Bonus) Hex colors

| Attribute | HEX code |
| :-------- | :------- |
| <font color="#f07e7e">**Power**</font>        | <font color="#f07e7e">#f07e7e</font> |
| <font color="#56abe1">**Defense**</font>      | <font color="#56abe1">#56abe1</font> |
| <font color="#f1c45b">**Speed**</font>        | <font color="#f1c45b">#f1c45b</font> |
| <font color="#52de80">**Vitality**</font>     | <font color="#52de80">#52de80</font> |
| <font color="#d8ffce">**Special Stat**</font> | <font color="#d8ffce">#d8ffce</font> |
| <font color="#ff4242">**Physical**</font>     | <font color="#ff4242">#ff4242</font> |
| <font color="#ffba26">**Fire**</font>         | <font color="#ffba26">#ff4242</font> |
| <font color="#16cc54">**Nature**</font>       | <font color="#16cc54">#16cc54</font> |
| <font color="#60fff9">**Frost**</font>        | <font color="#60fff9">#60fff9</font> |
| <font color="#fff7bc">**Lightning**</font>    | <font color="#fff7bc">#fff7bc</font> |
| <font color="#ce8cd6">**Shadow**</font>       | <font color="#ce8cd6">#ce8cd6</font> |
| <font color="#ffb561">**Damage**</font>       | <font color="#ffb561">#ffb561</font> |
| <font color="#9dff61">**Heal**</font>         | <font color="#9dff61">#9dff61</font> |
| <font color="#14b1ff">**Focus**</font>        | <font color="#14b1ff">#14b1ff</font> |

Other colors
- <font color="#000000">#000000</font>	
- <font color="#ffffff">#ffffff</font>
- <font color="#e8f086">#e8f086</font>
- <font color="#6fde6e">#6fde6e</font>
- <font color="#ff4242">#ff4242</font>
- <font color="#a691ae">#a691ae</font>
- <font color="#235fa4">#235fa4</font>
- <font color="#0a284b">#0a284b</font>
