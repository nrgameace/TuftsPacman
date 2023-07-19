# Rendition of Pacman
## By:
## Nick Regas, Joe Quinn, Connor Leathe, Alex Maeillo, and Joaquin Kiltz
## Final Project Tufts Coding Academy 2023
### Libraries
#### This code is based off of the python libraries pygame, Random, and Time.  These libraries need to be installed and running the latest version to ensure compatibility.  Anaconda can be used to manage packages effectively and ensure version compatibility.  The links to download instructions for each library are below.

### About the Program
#### This is a very basic recreation of Pacman in python with one level.  Our goal was to make a viable rendition of the classic game to enjoy playing.  This program has its own Graphical User Interface and will display itself when running the program.  Enjoy playing our recreation of Pacman and have fun!
## How to Run
#### Please install each library by navigating to the liks below.  Make sure to clone the repository using the command: 
```
git clone https://github.com/nrgameace/TuftsPacman.git
```
#### After this, run the file main.py by navigating to the directory of which the file main.py is stored in.  Then in your terminal execute: 
```
python main.py
```

### Rules of the Game
#### To play, move Pacman by pressing the arrow keys.  The up arrow moves up, left moves left, right moves right, and down moves down.  The objective is to collect all the white pellets before losing all three of your lives.  At each corner of the map there are larger yellow pellets.  These pellets are powerups that Pacman can eat to grant him immunity for 10 seconds before the consumible wears off.  

### Scoring
- White pellets are worth 10 points
- Yellow powerups are worth 50 points
- Each ghost eaten after the powerup is consumed adds 200 points

### Troubleshooting
#### The code is ready for use as soon as you download it.  However, if you are experiencing issues please make sure to double check these things:
- The directory from which your terminal is running the command '''python main.py'''
- The image files are in the proper directory as shown on the repository
- Anaconda is installed and all libraries were installed using it
- Python is up to date
- Make sure no code has been accidentally commented out or there are any errors
- Lastly make sure you are cloning the right repository and make sure that they contain all the image and python files
### Future Plans
- Allow the ghosts to target and follow Pacman if in a close proximity
- Add multiple levels and maps
- Add a top score that keeps track of the highest score on a device
- Add a main menu to customize options such as colors and input choice
- Add sound effects to movements and actions taken in the game
- Animate the ghosts movement so they look in the direction they are going
- Make the endges smoother rather than blocks 

### Links
#### Anaconda - *If you are adding Anaconda on windows, make sure you add it as a default path:
#### https://www.anaconda.com/download
#### Pygame:
#### https://www.pygame.org/download.shtml
#### Random2:
#### https://pypi.org/project/random2/
#### Time:
#### https://pypi.org/project/python-time/