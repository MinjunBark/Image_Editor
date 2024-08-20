# from PIL import Image, ImageTk
# import tkinter as tk 

# class ImageViewer(tk.Frame):
    
#     def __init__(self, master, original_imgs, edited_imgs):
#         super().__init__(master)
#         self.original_imgs = original_imgs
#         self.edited_imgs = edited_imgs
#         self.current_image = 0
        
#         self.create_gui()
        
#     def create_gui(self):
#         self.master.title("Image Viewer")
        
#         self.show_image()
        
#         self.prev_button = tk.Button(self, text='Prev', command=self.show_prev_image)
#         self.prev_button.pack(side=tk.LEFT)
        
#         self.next_button = tk.Button(self, text="Next", command=self.show_next_image)
#         self.next_button.pack(side=tk.RIGHT)
        
#         self.zoom_scale = tk.Scale(self, from_=1, to=10, orient=tk.HORIZONTAL, command=self.zoom_image)
#         self.zoom_scale.pack(side=tk.BOTTOM)
        
#         self.pack()
        
#     def show_image(self):
#         try:
#             original_img = Image.open(self.original_imgs[self.current_image])
#             edited_img = Image.open(self.edited_imgs[self.current_image])
            
#             original_tk_img = ImageTk.PhotoImage(original_img)
#             edited_tk_img = ImageTk.PhotoImage(edited_img)
            
#             self.original_label = tk.Label(self, image=original_tk_img)
#             self.original_label.image = original_tk_img
#             self.original_label.pack()
            
#             self.edited_label = tk.Label(self, image=edited_tk_img)
#             self.edited_label.image = edited_tk_img
#             self.edited_label.pack()
#         except FileNotFoundError:
#             print("Error: File not found.")
#         except Exception as e:
#             print(f"An error occurred: {e}")
        
#     def show_prev_image(self):
#         self.original_label.pack_forget()
#         self.edited_label.pack_forget()
        
#         self.current_image = (self.current_image -1) % len(self.original_imgs)
#         self.show_image()
        
#     def show_next_image(self):
#         self.original_label.pack_forget()
#         self.edited_label.pack_forget()
        
#         self.current_image = (self.current_image  + 1) % len(self.original_imgs)
#         self.show_image()
    
#     def zoom_image(self, value):
#         self.original_label.pack_forget()
#         self.edited_label.pack_forget()
        
#         original_img = Image.open(self.original_imgs[self.current_image])
#         edited_img = Image.open(self.edited_imgs[self.current_image])
        
#         value = int(value)
        
#         original_tk_img = ImageTk.PhotoImage(original_img.resize((int(original_img.width * value / 10), int(original_img.height * value / 10))))
#         edited_tk_img = ImageTk.PhotoImage(edited_img.resize((int(edited_img.width * value / 10), int(edited_img.height * value / 10))))
        
#         self.original_label = tk.Label(self, image=original_tk_img)
#         self.original_label.image = original_tk_img
#         self.original_label.pack()
        
#         self.edited_label = tk.Label(self, image=edited_tk_img)
#         self.edited_label.image = edited_tk_img
#         self.edited_label.pack()

# root = tk.Tk()
# original_imgs = ["path/to/original/image1.jpg", "path/to/original/image2.jpg"]
# edited_imgs = ["path/to/edited/image1.jpg", "path/to/edited/image2.jpg"]

# viewer = ImageViewer(root, original_imgs, edited_imgs)
# root.mainloop()