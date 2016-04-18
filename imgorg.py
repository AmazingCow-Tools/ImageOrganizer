#!/usr/bin/python
#coding=utf8
##----------------------------------------------------------------------------##
##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        imgorg.py                                 ##
##            █ █        █ █        ImageOrganizer                            ##
##             ████████████                                                   ##
##           █              █       Copyright (c) 2015, 2016                  ##
##          █     █    █     █      AmazingCow - www.AmazingCow.com           ##
##          █     █    █     █                                                ##
##           █              █       N2OMatt - n2omatt@amazingcow.com          ##
##             ████████████         www.amazingcow.com/n2omatt                ##
##                                                                            ##
##                  This software is licensed as GPLv3                        ##
##                 CHECK THE COPYING FILE TO MORE DETAILS                     ##
##                                                                            ##
##    Permission is granted to anyone to use this software for any purpose,   ##
##   including commercial applications, and to alter it and redistribute it   ##
##               freely, subject to the following restrictions:               ##
##                                                                            ##
##     0. You **CANNOT** change the type of the license.                      ##
##     1. The origin of this software must not be misrepresented;             ##
##        you must not claim that you wrote the original software.            ##
##     2. If you use this software in a product, an acknowledgment in the     ##
##        product IS HIGHLY APPRECIATED, both in source and binary forms.     ##
##        (See opensource.AmazingCow.com/acknowledgment.html for details).    ##
##        If you will not acknowledge, just send us a email. We'll be         ##
##        *VERY* happy to see our work being used by other people. :)         ##
##        The email is: acknowledgment_opensource@AmazingCow.com              ##
##     3. Altered source versions must be plainly marked as such,             ##
##        and must not be misrepresented as being the original software.      ##
##     4. This notice may not be removed or altered from any source           ##
##        distribution.                                                       ##
##     5. Most important, you must have fun. ;)                               ##
##                                                                            ##
##      Visit opensource.amazingcow.com for more open-source projects.        ##
##                                                                            ##
##                                  Enjoy :)                                  ##
##----------------------------------------------------------------------------##

## Imports ##
import getopt;
import os.path;
import os;
import re;
import shutil;
import sys;

################################################################################
## Don't let the standard import error to users - Instead show a              ##
## 'nice' error screen describing the error and how to fix it.                ##
################################################################################
def __import_error_message_print(pkg_name, pkg_url):
    print "Sorry, "
    print "imgorg depends on {} package.".format(pkg_name);
    print "Visit {} to get it.".format(pkg_url);
    print "Or checkout the README.md to learn other ways to install {}.".format(pkg_name);
    exit(1);


## cowtermcolor ##
try:
    from cowtermcolor import *;
except ImportError, e:
    __import_error_message_print(
        "cowtermcolor",
        "http//opensource.amazingcow.com/cowtermcolor.html");

## pygame ##
try:
    import pygame;
except ImportError, e:
    __import_error_message_print(
        "pygame",
        "http//www.pygame.org");


################################################################################
## Globals                                                                    ##
################################################################################
class Globals:
    verbose        = False;
    start_path     = ".";
    output_path    = "./output";
    sort_by_format = None;
    sort_by_size   = None;


################################################################################
## Constants                                                                  ##
################################################################################
class Constants:
    #Flags
    #Exclusives
    FLAG_HELP         = "h", "help";
    FLAG_VERSION      = "v", "version";
    FLAG_LIST_FORMATS = "l", "list-formats";
    #Optionals
    FLAG_VERBOSE      = "V", "verbose";
    FLAG_OUTPUT_PATH  = "o", "output";
    FLAG_NO_COLORS    = "n", "no-colors";
    FLAG_BY_FORMAT    = "f", "by-format";
    FLAG_BY_SIZE      = "s", "by-size";

    ALL_FLAGS_SHORT = "".join([
        #Exclusives
        FLAG_HELP         [0],
        FLAG_VERSION      [0],
        FLAG_LIST_FORMATS [0],
        #Optionals
        FLAG_VERBOSE      [0],
        FLAG_OUTPUT_PATH  [0] + ":",
        FLAG_NO_COLORS    [0],
        FLAG_BY_FORMAT    [0],
        FLAG_BY_SIZE      [0],
    ]);
    ALL_FLAGS_LONG = [
        #Exclusives
        FLAG_HELP         [1],
        FLAG_VERSION      [1],
        FLAG_LIST_FORMATS [1],
        #Optionals
        FLAG_VERBOSE      [1],
        FLAG_OUTPUT_PATH  [1] + "=",
        FLAG_NO_COLORS    [1],
        FLAG_BY_FORMAT    [1],
        FLAG_BY_SIZE      [1],
    ];

    #Supported Formats
    SUPPORTED_FORMATS = ["png", "jpg", "jpeg", "bmp", "tga"];

    #App
    APP_NAME      = "imgorg";
    APP_VERSION   = "0.2.0";
    APP_AUTHOR    = "N2OMatt <n2omatt@amazingcow.com>"
    APP_COPYRIGHT = "\n".join(("Copyright (c) 2015, 2016 - Amazing Cow",
                               "This is a free software (GPLv3) - Share/Hack it",
                               "Check opensource.amazingcow.com for more :)"));


################################################################################
## Colors                                                                     ##
################################################################################
ColorError      = Color(RED);
ColorOK         = Color(GREEN);
ColorProcessing = Color(YELLOW);
ColorPath       = Color(MAGENTA);
ColorInfo       = Color(BLUE);


################################################################################
## Print Functions                                                            ##
################################################################################
def print_verbose(msg, newline=True):
    if(Globals.verbose):
        print msg,
        if(newline):
            print;


def print_error(msg):
    print ColorError("[ERROR] ") + msg;


def print_fatal(msg):
    print ColorError("[FATAL] ") + msg;
    exit(1);


def print_help(exit_code = -1):
    msg = "Usage:" + """
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
  """;
    print msg;

    if(exit_code != -1):
        exit(exit_code);


def print_version(exit_code = -1):
    print "{} - {} - {}".format(Constants.APP_NAME,
                                Constants.APP_VERSION,
                                Constants.APP_AUTHOR);
    print Constants.APP_COPYRIGHT;
    print;

    if(exit_code != -1):
        exit(exit_code);


def print_formats(exit_code = -1):
    print "{} - {} - {}".format(Constants.APP_NAME,
                                Constants.APP_VERSION,
                                "AmazingCow");

    print "Supported formats: ";
    print "   " + " - ".join(Constants.SUPPORTED_FORMATS);

    if(exit_code != -1):
        exit(exit_code);


def print_run_info():
    print_verbose("Run info");
    print_verbose("  verbose        :" + str(Globals.verbose));
    print_verbose("  start_path     :" + str(Globals.start_path));
    print_verbose("  output_path    :" + str(Globals.output_path));
    print_verbose("  sort_by_format :" + str(Globals.sort_by_format));
    print_verbose("  sort_by_size   :" + str(Globals.sort_by_size));
    print_verbose("");


################################################################################
## Helper Functions                                                           ##
################################################################################
def canonize_path(path):
    return os.path.abspath(os.path.expanduser(path));


################################################################################
## Run                                                                        ##
################################################################################
def run():
    #Canonize and check the validity of start path.
    full_start_path = canonize_path(Globals.start_path);
    if(not os.path.isdir(full_start_path)):
        print_fatal("Invalid directory - ({})", ColorPath(Globals.start_path));


    #Iterate for all files on the start dir.
    for filename in os.listdir(full_start_path):
        filename      = os.path.join(Globals.start_path, filename);
        full_filename = canonize_path(filename);


        #Check if filename is not hidden (.somestuff)
        #And ends with a supported format (somestuff.png|jpg|jpeg|bmp|tga)
        regex_str = "^[^\.].*({})".format("|".join(Constants.SUPPORTED_FORMATS));
        if(re.search(regex_str, filename, re.I) is None):
            print_verbose("{} ({}) - {}".format(ColorInfo("Skipping"),
                                                ColorPath(full_filename),
                                                "doesn't look like a image file."));
            continue;

        #Load the image...
        try:
            surface = pygame.image.load(full_filename);
            height  = surface.get_height();
            width   = surface.get_width();
            ext     = os.path.splitext(filename)[1].replace(".", "").lower();
        except Exception, e:
            print_error("({}) - {}".format(ColorPath(full_filename), str(e)));
            continue;

        #Log.
        print_verbose("{} ({}) {} ({}x{}) {} ({})".format(
                        ColorProcessing("Loaded  :"),
                        ColorPath(filename),
                        ColorProcessing("size:"),
                        ColorInfo(width),
                        ColorInfo(height),
                        ColorProcessing("format:"),
                        ColorInfo(ext)));

        #Create the folder with the size / format of the image.
        folder_name = "";
        if(Globals.sort_by_size):
            folder_name = os.path.join(folder_name, "{}x{}".format(width, height));
        if(Globals.sort_by_format):
            folder_name = os.path.join(folder_name, ext);

        folder_path      = os.path.join(Globals.output_path, folder_name);
        folder_full_path = canonize_path(folder_path);

        #Create the output folder;
        try:
            os.makedirs(folder_full_path);
        except OSError, e:
            #Prevent the File Exists to be raised.
            if(e.errno != os.errno.EEXIST):
                e.filename = ColorPath(e.filename);
                print_fatal("Errno {} - {} - {}".format(e.errno,
                                                        e.strerror,
                                                        ColorPath(e.filename)));

        #Is Directory?
        if(not os.path.isdir(folder_full_path)):
            print_fatal("Output Dir Path is not a directory - ({})".format(
                        ColorPath(folder_full_path)));
        #Is Write enabled?
        if(not os.access(folder_full_path, os.W_OK)):
            print_fatal("Output Dir Path is not writable - ({})".format(
                        ColorPath(folder_full_path)));


        #Log.
        print_verbose("{} ({}) {} ({})".format(ColorProcessing("Copying :"),
                                               ColorPath(filename),
                                               ColorProcessing("to folder"),
                                               ColorPath(folder_path)),
                      newline=False);

        #Copy the image to folder.
        shutil.copy(full_filename, folder_full_path);

        print_verbose(ColorOK("[OK]"));


################################################################################
## Script initialization                                                      ##
################################################################################
def main():
    #Get the options.
    try:
        options = getopt.gnu_getopt(sys.argv[1:],
                                    Constants.ALL_FLAGS_SHORT,
                                    Constants.ALL_FLAGS_LONG);
    except Exception, e:
        print_fatal(str(e));

    #Parse the flags.
    for option in options[0]:
        key, value = option;
        key = key.lstrip("-");

        #Help / Version / List Formats - EXCLUSIVES
        if(key in Constants.FLAG_HELP         ): print_help   (0);
        if(key in Constants.FLAG_VERSION      ): print_version(0);
        if(key in Constants.FLAG_LIST_FORMATS ): print_formats(0);
        #Verbose / ByFormat / BySize - OPTIONALS
        if(key in Constants.FLAG_VERBOSE   ): Globals.verbose        = True;
        if(key in Constants.FLAG_BY_FORMAT ): Globals.sort_by_format = True;
        if(key in Constants.FLAG_BY_SIZE   ): Globals.sort_by_size   = True;
        #No Colors - OPTIONAL
        if(key in Constants.FLAG_NO_COLORS):
            ColorMode.mode = ColorMode.NEVER;
        #Output - OPTIONAL
        if(key in Constants.FLAG_OUTPUT_PATH):
            Globals.output_path = value;


    #By size is the default so, if neither of sort modes were set by user
    #set the default one.
    if(Globals.sort_by_format is None and Globals.sort_by_size is None):
        Globals.sort_by_size = True;

    #Get the start path.
    if(len(options[1]) != 0):
        Globals.start_path = options[1][0];

    #Will print only in verbose mode.
    print_run_info();

    #Start...
    run();

if __name__ == '__main__':
    main();
