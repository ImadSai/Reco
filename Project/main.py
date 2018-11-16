from convertGray import convert_gray_window
import variables
import Tkinter as Tk
import tkFileDialog


def convertion_gray_window():
    convert_gray_window(root, entree.get(), var.get())


def define_path():
    variables.pathTrainingImages = tkFileDialog.askdirectory()
    entree.insert(0, variables.pathTrainingImages)
    print variables.pathTrainingImages


def close_window():
    global stop
    stop = True
    print(' Close ')
    root.destroy()


if __name__ == '__main__':
    root = Tk.Tk()
    root.title(" Reseaux de neurones - Project ")
    root.geometry("750x150")
    root.resizable(0, 0)

    labelFrame = Tk.LabelFrame(root, text=" Training Dataset ", padx=10, pady=10)
    labelFrame.pack()

    Tk.Label(labelFrame, text=" Path training Dataset : ").grid(row=0, column=0)

    entree = Tk.Entry(labelFrame, width=40)
    entree.grid(row=0, column=1)

    button = Tk.Button(labelFrame, text="Select training DataSet", command=define_path)
    button.grid(row=0, column=2)

    var = Tk.IntVar()
    checkbox = Tk.Checkbutton(labelFrame, text="Inverser les couleurs", variable=var)
    checkbox.grid(row=1, column=1)

    button = Tk.Button(labelFrame, text="Convert to Binary", command=convertion_gray_window)
    button.grid(row=2, column=1, sticky=Tk.W)

    button = Tk.Button(labelFrame, text="Train neural networks", command=None)
    button.grid(row=2, column=1, sticky=Tk.E)

    button = Tk.Button(root, text="Close", command=close_window)
    button.pack()

    root.mainloop()
