# Missile Command

## Description
Remake of the classic Missile Command game by Atari.  Just for fun and practicing Python / programming.  Comments / feedback welcome.  Keep in mind I'm not a professional and this is a hobby project.

## Story



## How to Play

### Binary
When the game reaches a release state, I'll compile it to binary using some of the Python >> EXE tools available.  I haven't done this before so it may or may not work.

### From Source
The following guide is for downloading the source and running on Linux.  Other platforms have not been tested but should run in a Python 3 environment.

You need to have Git and Python3 installed on your system.

Clone / download files from Github repository

`git clone git://github.com/damianduffy/missile-command.git`

Create a local virtual environment

`python3 -m venv venv`

Activate the environment

`source venv/bin/activate`

Install the dependencies

`pip install -r requirements.txt`

Run the game!!

`python missile-defence.py`

To deactivate the virtual environment

`deactivate`

## Game Controls



## Original Game
Missile Command is a 1980 arcade game developed and published by Atari, Inc. and licensed to Sega for European release. It was designed by Dave Theurer, who also designed Atari's vector graphics game Tempest from the same year. The 1981 Atari 2600 port of Missile Command by Rob Fulop sold over 2.5 million copies and became the third most popular cartridge for the system.

[Wikipedia article](https://en.wikipedia.org/wiki/Missile_Command)

[Flash port of the original game](http://www.arcadedivision.com/classicgame12/shooting/missile-command.html)

## Work in Progress
 - add:load high score file
 - add:update high score
 - add:save high score file
 - update:display cities / destroyed cities
 - update:add new design for intercepter(s)
 - add:add sound effects
 - add:add splash
 - add:add menu / credits
 - fix: overlap on text prompts (e.g. new level/game over ... followed by pause/exit)
 - add:add scoring based on missiles destroyed, cities remain, bonus / multiplier
 - add:tweek gameplay mechanics / play-test
 - add:clean up comments

## Roadmap / Possible Further Improvements
 - add: bomber planes
 - add: satelites / UFOs
 - add: multi-warhead
 - add: colourful explosions
 - add: hilly terrain
 - add: multiple intercepter batteries
 - add: customise controls
 - add: cities that can be partially destroyed (maybe with civilian death count) OR have missiles target specific cities (total destruction on hit, similar to original game)
 - update: explosion on ground creates semi-circle / masked by ground instead of circle
 - optimise: break event handler into seperate class
 - update: consider detonating warhead instead of just removing the missile on destruction
