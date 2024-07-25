import tkinter as tk
from tkinter import *
import os


#Dictionnaire des couleurs
couleur = {"nero": "#252726" ,
           "purple": "#800080",
           "white": "#FFFFFF",
           "grey": "#808080",
           "Dodgerblue": "#1E90FF",
           "Royalblue": "#4169E1",
           "Lavender": "#E6E6FA"}

#paramétrage de la fenetre
app = tk.Tk()
app.title("Mon application")
app.config(bg="grey30")
app.geometry("400x600")
app.iconbitmap("C:\\Users\\MAISON INFO\\Documents\\Stage 2\\projet\\logo.ico")

#parametrage Switch
btnEtat = False

#Chargement image Navbar
navIcon = PhotoImage(file=os.path.join("C:\\Users\\MAISON INFO\\Documents\\Stage 2\\projet\\menu.png"))
closeIcon = PhotoImage(file=os.path.join("C:\\Users\\MAISON INFO\\Documents\\Stage 2\\projet\\close.png"))
imgFond = PhotoImage(file=os.path.join("C:\\Users\\MAISON INFO\\Documents\\Stage 2\\projet\\background.png"))


#Top  bar 
topFrame = tk.Frame(app,bg=couleur["Dodgerblue"])
topFrame.pack(side="top", fill=tk.X)

#Texte de top bar
acceuilText = tk.Label(topFrame, text="Java", 
                       font="ExtraCondensed 15", 
                       bg=couleur["Dodgerblue"], 
                       fg="white", height=2, padx=20)
acceuilText.pack(side="right")

#Banner text & Image Fond
can = Canvas(app, width=400, height=600)
can.create_image(0, 0, anchor=NW,
                  image= imgFond )
bannerTexte = tk.Label(app, text="DEVELOPPEMENT \nWEB",
                       font="ExtraCondensed 15",
                       fg=couleur["Royalblue"])
bannerTexte.place(x=100, y=400)
app.mainloop()