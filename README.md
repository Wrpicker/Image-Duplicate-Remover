# Reddit-Image-Downloading-Bot
This script can take up to 5 subreddits and download images from them, saving them into a file.
_______________________________________________________________________________________________

## DEPENDENCIES:

-OS

-Numpy

-Image, ImageFont, ImageDraw from PIL

_______________________________________________________________________________________________

## HOW TO USE:

This project requires only a single file:

-The Main Python Script

_______________________________________________________________________________________________

##### **The Main Python Script:**

For this one, all you have to do is download it. There are no modifications necessary for it to function

To use it, open up the command prompt and just run it from there. It will prompt you to input a mode and a directory

## Mode

You have an option of 1, 2, or 3 for the mode

1 - The script will scan all pixels of all images, making 100% sure they are not the same

2 - The script will scan half of the pixels in all of the images. This will be the left half of all the images. This is quicker, but isn't as thorough if you are dealing with images that are similar

3 - The script will scan a quarter of the pixels in all the images. This will be the upper left corner of pixels. This is even faster than 2, but is less thorough

## Directory

This is the directory with the images you want to scan. It should be something like "C:\Users\JohnDoe\Documents"
