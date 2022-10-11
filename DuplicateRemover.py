from PIL import Image, ImageFont, ImageDraw
import numpy
import os

def Image_Pixels(filename, a, b):
    '''
    Opens an image file and creates a list of its pixels
    
    Inputs:
        filename: [STRING] The name of the image file
        a, b: [INT] Integers that effect what portion of the files pixels are added to the list
    
    Outputs:
        ImageList: [LIST] A list of the image's pixels
    '''
#Opens the image and loads it
    OpenImg = Image.open(filename)
    OpenImgLoaded = OpenImg.load()
#Sets the x and y of the pixels to be scanned
    x = OpenImg.width/a
    y = OpenImg.height/b
#List for the pixels to be stored in
    ImageList = []
#Loop that gathers all of the pixels
    for i in range(y):
        for j in range(x):
            ImageList.append(OpenImgLoaded[j, i])
#Returns the list
    return ImageList

def RemovalInitiation():
    '''
    Gets input for removal speed and directory, then calls RemovalMain using this input
    
    Inputs:
        None
        
    Outputs:
        None
    '''
#Takes in an input of 1, 2, or 3 that determines how thoroughly images are scanned
    Speed = input(
"Enter type of Removal\n1. Thorough (Scans all pixels and compares them) [SLOW]\n2. Moderate (Scans half of all pixels to compare) [MEDIUM]\n3. Quick (Scans one fourth of all pixels and compares them) [FAST]\n\n>>>")
#Checks to make sure the input is 1, 2, or 3
    while Speed != "1" and Speed != "2" and Speed != "3":
        print("Please enter 1, 2, or 3")
        Speed = input(">>> ")
#While loop that gets the input for the directory and ensures it is the correct directory
    loop = True
    while loop == True:
        Directory = input("Enter the directory to be checked for duplicates: ")
        while os.path.exists(Directory) == False:
            print("That directory does not exist. Please enter a valid directory")
            Directory = input("Directory: ")
        print(f"You entered {Directory}\n\nIs this correct? (Y/N)")
        choice = input(">>> ")
        while choice.lower() != "y" and choice.lower() != "n":
            print("Please enter Y for yes or N for no")
            choice = input(">>> ")
        if choice.lower() == "y":
            loop = False
#Calls to removal main
    RemovalMain(Speed, Directory)

def RemovalMain(Mode, Directory):
    '''
    Accesses the inputted Directory and scans the pixels of each file, deleting any duplicates
    
    Inputs:
        Mode: [STRING] A string of either 1, 2, or 3 that determines how thoroughly files are scanned
        Directory: [STRING] The directory to be accessed

    Outputs:
        None
    '''
    import os
#a and b are variables used to divide the length and width of the image to reduce the pixels to be scanned on quicker modes
    a = 1
    b = 1
    if Mode == "2":
        a = 2
    elif Mode == "3":
        b = 2
        a = 2
#List for each of the images' pixels to be stored in and compared to
    knownPixels = []
#Creates the file list
    FileList = os.listdir(f"{Directory}")
    print("Removal in progress...")
#For loop that gets the pixels from each image and, if they match any in knownPixels, deletes the image. Otherwise it adds the pixels to knownPixels
    for file in FileList:
        pixels = Image_Pixels(f"{Directory}/{file}", a , b)
        if pixels in knownPixels:
            os.remove(f"{Directory}/{file}")
        else:
            knownPixels.append(pixels)
    print("Removal Complete")

#Main function to start the process
def main():
    RemovalInitiation()
    
if __name__ == "__main__":
    main()

