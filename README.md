# Rendition of Pacman
## Libraries
### This code is based off of the python libraries pygame, Random, and Time.  These libraries need to be installed and running the latest version to ensure compatibility.  Anaconda can be used to manage packages effectively and ensure version compatibility.  The links to download instructions for each library are below.

## About the Program
### This is a very basic recreation of Pacman in python with one level currently.  The ghosts contain basic logic for directions by using random integers.  These are all features that will be implemented later to create a more complete rendition of Pacman.
## How to Run
### Please install each library by navigating to the liks below.  Make sure to clone the repository using the command - 
```
git clone <repository url>
```
### After this, run the file main.py by navigating to the directory of which the file main.py is stored in.  Then in your terminal execute: 
```
python main.py
```

## Rules of the Game
### To play, move Pacman by pressing the arrow keys.  The up arrow moves up, left moves left, right moves right, and down moves down.  The objective is to collect all the white pellets before losing all three of your lives.  At each corner of the map there are larger yellow pellets.  These pellets are powerups that Pacman can eat to grant him immunity for 10 seconds before the consumible wears off.  

## Scoring
- White pellets are worth 10 points
- Yellow powerups are worth 50 points
- Each ghost eaten after the powerup is consumed adds 200 points


## Future Plans
 ### In the future we may update the game by including Pacman and ghosts more close to their original design.  We may also include more levels as well as program the individual ghosts to follow certain strategies.

## Links
### Anaconda - *If you are adding Anaconda on windows, make sure you add it as a default path:
### https://www.anaconda.com/download
### Pygame:
### https://www.pygame.org/download.shtml
### Random2:
### https://pypi.org/project/random2/
### Time:
### https://pypi.org/project/python-time/