import os
import variables
from PIL import Image, ImageOps, ImageTk
import Tkinter as Tk
import tkMessageBox


def close_window():
    global stop
    stop = True
    print(' Close ')
    fenetre.destroy()


def changeimg(self, inverse):
    print ' - Debut du Traitement'
    directory = os.listdir(variables.pathTrainingImages)
    for file in directory:
        filename, extension = os.path.splitext(file)
        if not stop:
            if extension == '.jpg':
                img = Image.open(variables.pathTrainingImages + '/' + file)
                img_gray = ImageOps.grayscale(img)
                if inverse:
                    img_gray = ImageOps.invert(img_gray)
                photo = ImageTk.PhotoImage(img_gray)
                img_gray.save(variables.pathTrainingImages + '/' + file)
                canvas.itemconfig(self.displayedImg, image=photo)
                canvas.update()
        else:
            break
    print ' - Fin du Traitement'
    close_window()


class convert_gray_window:
    def __init__(self, master, path, inverse):
        global fenetre
        global canvas
        global stop
        variables.pathTrainingImages = path

        fenetre = Tk.Toplevel()
        fenetre.title("conversion")
        stop = False

        canvas = Tk.Canvas(fenetre, width=100, height=100)
        self.displayedImg = canvas.create_image(50, 50, anchor=Tk.CENTER, image=None)
        canvas.pack()

        button = Tk.Button(fenetre, text="Close", command=close_window, width=20)
        button.pack()

        if not os.path.isdir(variables.pathTrainingImages):
            close_window()
            tkMessageBox.showinfo("Error", "Le chemin que vous avez fourni n'est pas valide")
        else:
            changeimg(self, inverse)


