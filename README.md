Image Organizer
====
Made with <3 by [Amazing Cow](http://www.amazingcow.com).

## Intro:
With an app named **Photo Totem** that we made for our partners at [Imidiar](http://www.imidiar.com/br) 
a recurring task is organize the images taken by
the Photo Totem into folders to merge them with the Client Frame, since the 
Photo Totem in sake of performance doesn't merge the photos in run time. 
This is needed because the hardware that the software runs is **very** limited.
Up to now this way has been very successful and not cumbersome at all, since we (Imidiar)
just have one Totem. But with the acquisition of other Totems, with multiple camera resolutions
running into the same event, the task of merge the frame with the taken photos has became 
tedious.

For this we created a small utility that grab all photos into folder and copy them 
into folders with the name of the it's resolution. So if a folder has 20 photos of
640x480, 40 of 1280x720 and so on, the output will be 2 folders with the named after 
the resolution with all photos of the resolution copied into it.

The goal is very specific but we hope that you find another good ways to use it.

As usual, you are **very welcomed** to **share** and **hack** it.
 
## Install:
```$ sudo cp -f path/to/imgorg.py /usr/local/bin/imgorg```

or 

```make install```

## Usage:

```
imgorg [-hvV] [-o <path>] <start_path>

Options:
 *-h --help          : Show this screen.
 *-v --version       : Show app version and copyright.
  -V --verbose       : Verbose mode, helps to see what it's doing.
  -o --output <path> : Path that the images will be copied.


```
#####Notes:
  If <start_path> is not given, the current dir ```.``` is assumed.  
  If <output_path> is not given, the current dir ```.``` is assumed
  and a folder named ("output") will be created. ```./output```

  Options marked with * are exclusive, i.e. the ```imgorg``` will
  run that and exit successfully after the operation.

## License:
This software is released under GPLv3.

## TODO:
Check the TODO file.

## Others:
Check our repos and take a look at our [open source site](http://opensource.amazingcow.com).
