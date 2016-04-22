# Image Converter

**Made with <3 by [Amazing Cow](http://www.amazingcow.com).**



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Description:

```imgorg``` - Organize your images nicely.

```imgorg``` is a small tool to organize your images into structured 
directories sorted by the images' sizes and/or format.     
The images (the input and output) must be in any image format supported by 
[pygame](http://www.pygame.org). 


<br>

As usual, you are **very welcomed** to **share** and **hack** it.



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Usage:

``` 
  imgorg -h | -v | -l
  imgorg [-V] [-n] [-f] [-s] [-o <path>] <start_path>

Options:
 *-h --help          : Show this screen.
 *-v --version       : Show app version and copyright.
 *-l --list-formats  : Show the supported image formats.

  -V --verbose   : Verbose mode, helps to see what it's doing.
  -n --no-colors : Print the output without colors.

  -f --by-format : Sort the output images by format.
  -s --by-size   : Sort the output images by size.

  -o --output <path> : Path that the images will be copied.

Notes:
  If <start_path> is not given, the current dir (".") is assumed.
  If <output_path> is not given, the current dir (".") is assumed
  and a folder named ("output") will be created. ("./output")

  --by-format and --by-size can be used together.
  If none is specified the --by-size is assumed as default.

  Options marked with * are exclusive, i.e. the imgorg will
  run that and exit successfully after the operation.
```


<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Install:

Use the Mafefile.

``` bash
    make install
```

Or to uninstall

``` bash
    make uninstall
```



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Dependencies:

This project uses / depends on:

* Amazing Cow's 
[cowtermcolor](http://www.github.com/AmazingCow-Libs/cowtermcolor_py)
package to coloring the terminal.

* [pygame](http://www.pygame.org) as a backend to image manipulations.



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Environment and Files: 

```imgorg``` do not create / need any other files or environment vars.



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## License:

This software is released under GPLv3.



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## TODO:

Check the TODO file for general things.

This projects uses the COWTODO tags.   
So install [cowtodo](http://www.github.com/AmazingCow-Tools/COWTODO) and run:

``` bash
$ cd path/for/the/project
$ cowtodo 
```

That's gonna give you all things to do :D.



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## BUGS:

We strive to make all our code the most bug-free as possible - But we know 
that few of them can pass without we notice ;).

Please if you find any bug report to [bugs_opensource@amazingcow.com]() 
with the name of this project and/or create an issue here in Github.



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Source Files:

* AUTHORS.txt
* CHANGELOG.txt
* COPYING.txt
* imgorg.py
* Makefile
* OLDREADME.md
* README.md
* TODO.txt



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Others:
Check our repos and take a look at our [open source site](http://opensource.amazingcow.com).
