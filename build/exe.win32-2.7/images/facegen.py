from Tkinter import *
from PIL import ImageTk, Image
from random import randint

def newName(pattern):
    VOWELS = "AEIOU"
    CONSONANTS = "BCDFGHJKLMNPQRSTVWXYZ"

    name = ""

    for i in range(0, len(pattern)):
        if (pattern[i] == 'V'):
            name += (VOWELS[randint(0, len(VOWELS)-1)])
        elif (pattern[i] == 'C'):
            name += (CONSONANTS[randint(0, len(CONSONANTS)-1)])
        else:
            name += (" ")

    return name


def newFace():
    
    pathA = ["skin",
         "eyes",
         "eyecolour",
         "mouth",
         "nose",
         "eyebrow",
         "feature", 
         "hair",
         "fhair"]

    count = [7, 1, 4, 4, 4, 4, 5, 4, 6]

    imageBg   = Image.open('bg.png');
    imageBase = Image.open('base.png')
    imageBg.paste(imageBase, (0,0), imageBase)

    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    for i in range(0, len(pathA)):
        thisImage = Image.open(pathA[i] + str(randint(1, count[i])) + ".png")
        imageBg.paste(thisImage, (0,0), thisImage)

    img = ImageTk.PhotoImage(imageBg)
    return img

def packWindow(face, name, b, pattern):

    # pack the window, starting with the lowest element
    pattern.tag_configure("center", justify='center')
    pattern.tag_add("center", 1.0, "end")
    pattern.pack(side = "bottom", fill = "both", expand = "no")
    
    name.pack(side = "bottom", fill = "both", expand = "no")

    #The Pack geometry manager packs widgets in rows or columns.
    face.pack(side = "bottom", fill = "both", expand = "yes")

    b.pack(side = "bottom", fill = "both", expand = "yes")

def randomize(face, nameVolitile, pattern):
    nameVolitile.set(newName(pattern))

    faceImage = newFace()
    face.configure(image=faceImage)
    face.image = faceImage

def main():
    
    #This creates the main window of an application
    window = Tk()
    window.title("FACEGEN")
    window.geometry("200x200")
    window.configure(background='grey')
    
    #The Label widget is a standard Tkinter widget used to display a text or image on the screen
    face = Label(window, image = newFace())
    nameVolitile = StringVar()
    name = Label(window, textvariable=nameVolitile)
    pattern = Text(window, height=2, width=30)
    pattern.insert(END, 'VCVCV CVVCVVC')
    randomize(face, nameVolitile, pattern.get(1.0,END)[:-1])
    b = Button(window, text="R4ND0M1ZE!", command = lambda: randomize(face, nameVolitile, pattern.get(1.0,END)[:-1]))
    
    packWindow(face, name, b, pattern)
    #Start the GUI
    window.mainloop()

main()

