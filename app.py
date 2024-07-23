import tkinter as tk
from tkintermapview import TkinterMapView


win = tk.Tk()

gmap_widget = TkinterMapView(win,width=600,height=600)
gmap_widget.pack(fill='both',expand=True)



gmap_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=50)




mrkr = gmap_widget.set_address("m'saken", marker=True)
mrkr.set_text("My Favorite place")
gmap_widget.set_zoom(12)




win.geometry('600x600')
win.title('My First App')
win.resizable(False, False)
win.iconbitmap("C:\\Users\\MAISON INFO\\Documents\\Stage 2\\projet\\logo.ico")
win.mainloop()