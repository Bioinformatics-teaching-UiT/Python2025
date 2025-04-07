#Import os module
import os


#Open inputfile
inputfile =  open("demofile.txt", "r")
inputfile.read()
inputfile.close()


#Open outputfile write something and close it
outputfile = open("../demofile2.txt", "a")
outputfile.write("Now the file has more content!")
outputfile.close()



#Print current working directory
print("Current directory:" , os.getcwd())

#Create a new directory
os.mkdir("mydir")

#Change current working directory
os.chdir("mydir")

#Print current working directory
print("Current directory now:" , os.getcwd())