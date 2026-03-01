

import os
import zipfile
import tkinter as tk
from tkinter import messagebox  
from PIL import Image, ImageTk


class FoodViewerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Food Viewer")
        self.root.geometry("400x300")  

        self.img_frame = tk.Frame(self.root)
        self.img_frame.pack()

        self.rbdBtn_frame = tk.Frame(self.root)
        self.rbdBtn_frame.pack()

        self._ensure_images()


        self.img1 = Image.open("chicken.jpg").resize((400, 300))
        self.imgOne = ImageTk.PhotoImage(self.img1)

        self.img2 = Image.open("pie.jpg").resize((400, 300))
        self.imgTwo = ImageTk.PhotoImage(self.img2)

        self.img3 = Image.open("pizza.jpg").resize((350, 300))
        self.imgThree = ImageTk.PhotoImage(self.img3)

        self.img4 = Image.open("steak.jpg").resize((300, 300))
        self.imgFour = ImageTk.PhotoImage(self.img4)


        self.lbl = tk.Label(self.img_frame, image=self.imgOne)
        self.lbl.pack()

 
        self.var = tk.IntVar()
        self.var.set(1)  

        self.radio_a = tk.Radiobutton(
            self.rbdBtn_frame,
            text="Chicken",
            variable=self.var,
            value=1,
            command=self.on_radio_select
        )
        self.radio_a.pack(side="left", padx=10)

        self.radio_b = tk.Radiobutton(
            self.rbdBtn_frame,
            text="Pie",
            variable=self.var,
            value=2,
            command=self.on_radio_select
        )
        self.radio_b.pack(side="left", padx=10)

        self.radio_c = tk.Radiobutton(
            self.rbdBtn_frame,
            text="Pizza",
            variable=self.var,
            value=3,
            command=self.on_radio_select
        )
        self.radio_c.pack(side="left", padx=10)

        self.radio_d = tk.Radiobutton(
            self.rbdBtn_frame,
            text="Steak",
            variable=self.var,
            value=4,
            command=self.on_radio_select
        )
        self.radio_d.pack(side="left", padx=10)

        self.on_radio_select()

    def _ensure_images(self):
        """If images aren't present, try extracting images.zip from the same folder."""
        needed = ["chicken.jpg", "pie.jpg", "pizza.jpg", "steak.jpg"]
        missing = [f for f in needed if not os.path.exists(f)]
        if not missing:
            return

        if os.path.exists("images.zip"):
            try:
                with zipfile.ZipFile("images.zip", "r") as z:
                    z.extractall(".")
            except Exception as e:
                messagebox.showerror("Error", f"Couldn't extract images.zip:\n{e}")
                raise
        else:
        
            raise FileNotFoundError(
                "Missing image files: "
                + ", ".join(missing)
                + "\nPut chicken.jpg, pie.jpg, pizza.jpg, steak.jpg in the same folder as asn4.py "
                  "(or put images.zip there)."
            )

    def on_radio_select(self):
        """Swap the image on the label based on the selected radiobutton value."""
        choice = self.var.get()

 

        if choice == 1:
            self.lbl.config(image=self.imgOne)
        elif choice == 2:
            self.lbl.config(image=self.imgTwo)
        elif choice == 3:
            self.lbl.config(image=self.imgThree)
        elif choice == 4:
            self.lbl.config(image=self.imgFour)


        self.lbl.image = {
            1: self.imgOne,
            2: self.imgTwo,
            3: self.imgThree,
            4: self.imgFour
        }.get(choice, self.imgOne)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    FoodViewerApp().run()
