from PIL import Image, ImageTk
import tkinter as tk 


class ImageViewer(tk.Frame):
    
    def __init__(self, master, original_imgs, edited_imgs):
        super().__init__(master)
        self.original_imgs = original_imgs
        self.edited_imgs = edited_imgs
        self.current_image = 0
        self.create_widgets()
    
    def create_widgets(self):
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.prev_button = tk.Button(self, text='Prev', command=self.show_prev_image)
        self.prev_button.pack(side=tk.LEFT)
        
        self.next_button = tk.Button(self, text="Next", command=self.show_next_image)
        self.next_button.pack(side=tk.RIGHT)
        
        self.zoom_scale = tk.Scale(self, from=1, to=10, orient=tk.HORIZONTAL, command=self.zoom_image)
        self.zoom_scale.pack(side=tk.BOTTOM)
        
        self.show_image()
        
    def show_image(self):
        original_img = self.original_imgs[self.current_image]
        edited_img = self.edited_imgs[self.current_image]
        
        original_tk_img = ImageTk.PhotoImage(original_img)
        edited_tk_img = ImageTk.PhotoImage(edited_img)
        
        self.canvas.delete("all")
        
        self.canvas.create_image(0, 0, anchor=tk.NW, image=original_tk_img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=edited_tk_img)
        
    def show_prev_image(self):
        self.current_image