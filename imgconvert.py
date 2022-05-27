from PIL import Image
import os

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

directory = r'C:\IMLEX\Sem2\DL\Project\3rdPartyCode\monodepth2-master\kitti_data'
#\2011_09_26_drive_0064_sync\2011_09_26\2011_09_26_drive_0064_sync\image_00\data
c=1
#for filename in os.listdir(directory):
#    if filename.endswith(".png"):
#        im = Image.open(directory + "\\" + filename)
#        name='img'+str(c)+'.jpg'
#        rgb_im = im.convert('RGB')
#        rgb_im.save(directory + "\\" + filename.split(".")[0]+".jpg")
#        c+=1
#        print(os.path.join(directory, filename))
#        continue
#    else:
#        continue

for filename in getListOfFiles(directory):
    if filename.endswith(".png"):
        im = Image.open(filename)
        rgb_im = im.convert('RGB')
        rgb_im.save(filename.split(".")[0]+".jpg")
        c+=1
        print(os.path.join(directory, filename))
        continue
    else:
        continue