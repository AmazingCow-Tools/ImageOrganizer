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
##        and must notbe misrepresented as being the original software.       ##
##     4. This notice may not be removed or altered from any source           ##
##        distribution.                                                       ##
##     5. Most important, you must have fun. ;)                               ##
##                                                                            ##
##      Visit opensource.amazingcow.com for more open-source projects.        ##
##                                                                            ##
##                                  Enjoy :)                                  ##
##----------------------------------------------------------------------------##


## Imports ##
import os;
import os.path;
import shutil;
import re;
import sys;
import getopt;
import pygame.image;

################################################################################
## Globals                                                                    ##
################################################################################
class Globals:
    verbose     = False;
    start_path  = ".";
    output_path = "./output";

################################################################################
## Constants                                                                  ##
################################################################################
class Constants:
    ##Flags
    FLAG_HELP        = "h", "help";
    FLAG_VERSION     = "v", "version";
    FLAG_OUTPUT_PATH = "o", "output";
    FLAG_VERBOSE     = "V", "verbose";

    ALL_FLAGS_SHORT = "hvo:V";
    ALL_FLAGS_LONG  = ["help","version","output=","verbose"];

    #App
    APP_NAME      = "imgorg";
    APP_VERSION   = "0.1.1";
    APP_AUTHOR    = "N2OMatt <n2omatt@amazingcow.com>"
    APP_COPYRIGHT = "\n".join(("Copyright (c) 2015, 2016 - Amazing Cow",
                               "This is a free software (GPLv3) - Share/Hack it",
                               "Check opensource.amazingcow.com for more :)"));

################################################################################
## Print Functions                                                            ##
################################################################################
def print_verbose(msg):
    if(Globals.verbose):
        print msg;

def print_fatal(msg):
    print "[FATAL]", msg;
    exit(1);

def print_help():
    msg = "Usage:" + """
  imgorg [-hvV] [-o <path>] <start_path>

Options:
 *-h --help          : Show this screen.
 *-v --version       : Show app version and copyright.
  -V --verbose       : Verbose mode, helps to see what it's doing.
  -o --output <path> : Path that the images will be copied.

Notes:
  If <start_path> is not given, the current dir (".") is assumed.
  If <output_path> is not given, the current dir (".") is assumed
  and a folder named ("output") will be created. ("./output")

  Options marked with * are exclusive, i.e. the imgorg will
  run that and exit successfully after the operation.
  """;
    print msg;

def print_version():
    print "{} - {} - {}".format(Constants.APP_NAME,
                            Constants.APP_VERSION,
                            Constants.APP_AUTHOR);
    print Constants.APP_COPYRIGHT;
    print;

def print_run_info():
    print_verbose("Run info");
    print_verbose("  verbose     :" + str(Globals.verbose));
    print_verbose("  start_path  :" + str(Globals.start_path));
    print_verbose("  output_path :" + str(Globals.output_path));
    print_verbose("");

################################################################################
## Run                                                                        ##
################################################################################
def run():
    filenames = os.listdir(Globals.start_path);
    for filename in filenames:
        full_filename = os.path.join(Globals.start_path, filename);

        #Check if filename is not hidden (.somestuff)
        #And ends with png, jpg or jpeg (somestuff.png|jpg|jpeg)
        if(re.search("^[^\.].*(png|jpg|jpeg)", filename) is None):
            print_verbose("({}) {}".format(full_filename,
                                           "doesn't look like a image file."));
            continue;

        #Load the image...
        try:
            surface = pygame.image.load(os.path.abspath(full_filename));
            height  = surface.get_height();
            width   = surface.get_width();
        except Exception, e:
            print_fatal(e);

        #Log.
        print_verbose("Loaded: ({}) size:({}x{})".format(full_filename,
                                                         width,
                                                         height));

        #Create the folder with the size of the image.
        folder_name = "{}x{}".format(width, height);
        folder_path = os.path.join(Globals.output_path, folder_name);
        os.system("mkdir -p {}".format(folder_path));

        #Log.
        print_verbose("Copying: ({}) to folder ({})".format(full_filename,
                                                            folder_path));

        #Copy the image to folder.
        shutil.copy(full_filename, folder_path);

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
        print_fatal(e);

    #Parse the flags.
    for option in options[0]:
        key, value = option;
        key = key.lstrip("-");

        #Help and Version Flags.
        if(key in Constants.FLAG_HELP):
            print_help();
            exit(0);
        if(key in Constants.FLAG_VERSION):
            print_version();
            exit(0);

        #Verbose Flag.
        if(key in Constants.FLAG_VERBOSE):
            Globals.verbose = True;
        #Output Flag.
        if(key in Constants.FLAG_OUTPUT_PATH):
            Globals.output_path = value;

    #Get the start path.
    if(len(options[1]) != 0):
        Globals.start_path = options[1][0];

    #Will print only in verbose mode.
    print_run_info();

    #Start...
    run();

if __name__ == '__main__':
    main();
