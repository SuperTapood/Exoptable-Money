# CHANGE LOG


## Version 0.5:
- added main main menu to hold all of the collection games
- updated the money machine's body
- updated the two money machine handles
- updated the small letter
- animated the small letter
- clicking the small letter icon will now make it disapear (this is for later)
- small letter animation is no longer dependent on the frame rate
- fixed issue where the small letter animation would get stopped because of faulty logic
- game will no longer check for letters when there is one already
- all text buttons will now have a little larger rect
- HUD will no longer update the money count if it is the same
- money count's rect has been enlarged to look better

## Version 0.4:
- game will no longer blit objects before they have a value
- added coins
- "added" letters
- further development is on hold due until I make new assets
- added a sprite manager to handle the sprites
- fixed a dumb bug in the data loading function
- shortened loading function using the walrus operator

## Version 0.3:
- added level 0 for the dollars
- added dynamic save system to make sure that saves won't break with updates
- added money machine upgrades
- added level label to the upgrade buttons (design will change later on)
- optimized load function

## Version 0.2:
- added save button
- added load button
- fixed bug with the loading function
- added shop with ability to upgrade the cash
- added button to return to the main screen (the one with the machine)
- scenes will now load during the init of the game
- repositioned title in the title screen
- removed the money machine from the title screen
- repositioned the recolored the resume game button and renamed it
- added global FPS Counter
- repositioned HUD
- added a new game button to the main menu
- added a delete data button (disabled until I add a disclaimer)
- added version number and build state label to the main menu
- fixed buy functions
- updated save function
- changed the way money moves

## Version 0.1:
- added the machine as a complex object
- added the HUD
- added money counter
- added the dollar placeholder
- added falling objects that increase your moneys
- added collision rules
- falling objects that collide with the machine will now bounce off