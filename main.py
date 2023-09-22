import shutil
import time
import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
desktop = desktop.replace('\\', "/")
locations = ["PDFs", "Pictures", "Videos", "Executables", "Archives", "Other"]
imageExtentions = [".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".bmp"]
videoExtentions = [".mp4", ".avi", ".mov", ".flv", ".webm", ".mkv"]

def setup():
    os.chdir(desktop)
    for i in locations:
        if os.path.exists(i) == False:
            os.mkdir(i)
            print("Creating: " + i)
    print("All folders in place, cleaning up desktop now.")
            

def cleanDesktop():
    for file in os.listdir(desktop):
        f = os.path.join(desktop, file)
        split = os.path.splitext(file)
        if split[1].lower() == '.pdf':
            print(file + "->" + locations[0])
            shutil.move(file, locations[0])
        if split[1].lower() == ".exe" or split[1].lower() == ".msi":
            print(file + "->" + locations[3])
            shutil.move(file, locations[3])
        if split[1].lower() == ".rar" or split[1].lower() == ".zip":
            print(file + "->" + locations[4])
            shutil.move(file, locations[4])
        if split[1].lower() == ".json":
            print(file + "->" + locations[5])
            shutil.move(file, locations[5])

        for e in imageExtentions:
            if split[1].lower() == e:
                print(file + "->" + locations[1])
                shutil.move(file, locations[1])
        for e in videoExtentions:
            if split[1].lower() == e:
                print(file + "->" + locations[2])
                shutil.move(file, locations[2])
        

def autoClean():
    print("Auto clean enabled!")
    
    while True:
        cleanDesktop()
        print("Cleaning now... \nLast cleaned at: " + time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime()))
        time.sleep(3600)
        


setup()
cleanDesktop()
while True:
    menu = input("Options:\n 1.) Clean again,\n 2.) Auto Clean (hourly),\n 3.) Exit\n -> ")
    if menu == "1":
        os.system("cls")
        cleanDesktop()
        print("Desktop has been cleaned!")
    elif menu == "2":
        autoClean()
    elif menu == "3":
        quit()
