import os
import shutil
import tkinter as tk
import time


window = tk.Tk()

window.title("Automatic File Arranger")

window.geometry("600x580")

#Putting together various extensions
EXT_AUDIOS = ['.wav','.mp3','.raw', '.wma']
EXT_VIDEOS = ['.mp4','.m4a','.m4v','.fav','.f4a','.m4b','.mkv','.m4r','.f4b','.mov','.avi','.wmv','.flv','.3gp','.webm']
EXT_IMAGES = ['.jpg','.jpeg','.png','.svg','.gif','.bmp']
EXT_DOCUMENTS = ['.txt','.pdf','.doc','.docx','.xlsx','.xls','.ppt','pptx','.odt','.html','.csv','.chm','.xlsm']
EXT_COMPRESSED = ['.rar','.zip','iso']
EXT_PROGRAMS = ['.exe','.msi']

DIRS = ['Audios','Videos','Images','Documents','Folders','Programs','Compressed','Others']

directory = os.getcwd()
files = os.listdir()

app_title = tk.Label(text="Automatic File Arranger",font=("Times New Roman",20,"bold"),bd=8,fg="Steel Blue")
app_title.grid(row=0,column=0)


info = tk.Label(text="By Mo Gadaphy\n",font=("Times New Roman",14,"bold"),bd=10)
info.grid(row=1,column=0)


info = tk.Label(text="This program help arrange your files in your \ncurrent directory into some folders for proper organisation \nand quicker acces.You just need to click on the arrange files button \nbelow for all your files to be arranged in their \nrespectives folders which the application will create like \nAudios, Videos, Images, Documents,Compressed, Programs and Others\n",font=("Times New Roman",14,"italic"),bd=10)
info.grid(row=2,column=0)


#Create directory if they don't exist
def createDirectory():
    
    info1 = tk.Label(text="Creating Folders...",font=("Times New Roman",14,"italic"),bd=10)
    info1.grid(row=4,column=0)
    #time.sleep(1)
    for d in DIRS:
        if not os.path.isdir('./{}'.format(d)):
            os.mkdir('./{}'.format(d))
            #info1 = tk.Label(text="{} Folder created.\n".format(d),font=("Times New Roman",14,"italic"),bd=10)
            #info1.grid(row=5,column=0)
            time.sleep(1)
    info1 = tk.Label(text="Done Creating Folders",font=("Times New Roman",12,"italic"),bd=8)
    info1.grid(row=5,column=0)

#Creating the arranger function
def arranger():
    # createDirectory()
    info1 = tk.Label(text="Starting the Automatic Process",font=("Times New Roman",12,"bold"),fg="orange")
    info1.grid(row=6,column=0)
    time.sleep(1)
    for f in files:
        name, extension = os.path.splitext(f)

        if extension in EXT_IMAGES:
        	if not os.path.isdir('./{}'.format(DIRS[2])):
        		os.mkdir('./{}'.format(DIRS[2]))
        	shutil.move(f,"./Images/{}".format(f))
        elif extension in EXT_AUDIOS:
        	if not os.path.isdir('./{}'.format(DIRS[0])):
        		os.mkdir('./{}'.format(DIRS[0]))
        	shutil.move(f,"./Audios/{}".format(f))
        elif extension in EXT_VIDEOS:
        	if not os.path.isdir('./{}'.format(DIRS[1])):
        		os.mkdir('./{}'.format(DIRS[1]))
        	shutil.move(f,"./Videos/{}".format(f))
        elif extension in EXT_DOCUMENTS:
        	if not os.path.isdir('./{}'.format(DIRS[3])):
        		os.mkdir('./{}'.format(DIRS[3]))
        	shutil.move(f,"./Documents/{}".format(f))
        elif extension in EXT_PROGRAMS:
        	if (f.lower() != "automatic file arranger.exe") and (f != "arranger.exe"):
        		if not os.path.isdir('./{}'.format(DIRS[5])):
        			os.mkdir('./{}'.format(DIRS[5]))
        		shutil.move(f,"./Programs/{}".format(f))
            
        elif extension in EXT_COMPRESSED:
        	if not os.path.isdir('./{}'.format(DIRS[6])):
        		os.mkdir('./{}'.format(DIRS[6]))
        	shutil.move(f,"./Compressed/{}".format(f))
        else:
            if os.path.isdir(name):
                if name not in DIRS:
                	if not os.path.isdir('./{}'.format(DIRS[4])):
                		os.mkdir('./{}'.format(DIRS[4]))
                	shutil.move(f,"./Folders/{}".format(f))
            else:
                if  (f != "arranger.py") and (extension != '.lnk')and (extension != '.ini')and (extension != '.db') and  (f != "automatic file arranger.py") and  (f != "file automata.py"):
                	if not os.path.isdir('./{}'.format(DIRS[7])):
                		os.mkdir('./{}'.format(DIRS[7]))
                	shutil.move(f,"./Others/{}".format(f))

    info1 = tk.Label(text="DONE MOVING!!!\n",font=("Times New Roman",14,"bold"),bd=10, fg="green")
    info1.grid(row=9,column=0)
    info1 = tk.Label(text="Verify at \n {}".format(directory),font=("Times New Roman",10,"italic"),bd=8)
    info1.grid(row=10,column=0)
    info1 = tk.Label(text="Developer   Email: mgadaphy1@gmail.com  Tel(+237): 672449521\n",font=("Times New Roman",10,"italic"),bd=8)
    info1.grid(row=11,column=0)
    
    


btn1 = tk.Button(text="ARRANGE FILES",fg="Steel Blue",font=("Times New Roman",12,"bold"),bd=10,command=arranger)
btn1.grid(row=3,column=0)

window.mainloop()
