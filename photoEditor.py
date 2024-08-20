from PIL import Image, ImageEnhance, ImageFilter, ImageTk
import os
import tkinter as tk
# from imageViewer import ImageViewer
# import matplotlib.pyplot as plt


path = '/Users/alexbark/Documents/Python_Automation_Projects/Image_Editor/Images'
pathOut = '/Users/alexbark/Documents/Python_Automation_Projects/Image_Editor/editedImgs'



def open_image(file_name):
    try:
        img = Image.open(f"{path}/{file_name}")
        return img
    except FileNotFoundError:
        print(f"{file_name} not found.")
        return None
    except Exception as e:
        print(f"Error opening {file_name}: {e}")
        return None


def adjust_sharpness(img, file_name): #factor value: 0 - 10 
    enhancer = ImageEnhance.Sharpness(img)
    factor = 5.0
    edit = enhancer.enhance(factor)
    return edit

    
    
def adjust_brightness(img, file_name): #factor value: 0 - 10 
    edit = ImageEnhance.Brightness(img)
    factor = 1.2 
    edit = edit.enhance(factor)
    return edit
    
def adjust_contrast(img, file_name): #factor value: 0 - 10 
    edit = ImageEnhance.Contrast(img)
    factor = .9 
    edit = edit.enhance(factor)
    return edit
    
    
def process_image():
    root = tk.Tk()
    original_imgs = []
    edited_imgs = []
    for file in os.listdir(path):
        original_img = open_image(file)
        sharpened_img = adjust_sharpness(original_img, file)
        brightened_img =adjust_brightness(sharpened_img, file)
        contrasted_img = adjust_contrast(brightened_img, file)
        original_imgs.append(original_img)
        edited_imgs.append(contrasted_img)
    
    # Set the maximum width and height for the images
    max_width = 400
    max_height = 300

    # Resize the images
    resized_original_imgs = []
    resized_edited_imgs = []
    for original_img, edited_img in zip(original_imgs, edited_imgs):
        original_img.thumbnail((max_width, max_height))
        edited_img.thumbnail((max_width, max_height))
        resized_original_imgs.append(original_img)
        resized_edited_imgs.append(edited_img)

    # Get the dimensions of the image
    image_width, image_height = resized_original_imgs[0].size

    # Set the size of the GUI window to match the image size with some padding
    root.geometry(f"{image_width+20}x{image_height+20}")

    # Allow the user to resize the window
    root.resizable(True, True)
    
    original_frame = tk.Frame(root)
    original_frame.pack(side=tk.LEFT)

    edited_frame = tk.Frame(root)
    edited_frame.pack(side=tk.LEFT)

    original_label = tk.Label(original_frame, text="Original Images")
    original_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    edited_label = tk.Label(edited_frame, text="Edited Images")
    edited_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    original_img_labels = []
    edited_img_labels = []

    for i, (original_img, edited_img) in enumerate(zip(resized_original_imgs, resized_edited_imgs)):
        original_tk_img = ImageTk.PhotoImage(original_img)
        original_img_label = tk.Label(original_frame, image=original_tk_img)
        original_img_label.image = original_tk_img
        original_img_label.pack()
        original_img_labels.append(original_img_label)

        edited_tk_img = ImageTk.PhotoImage(edited_img)
        edited_img_label = tk.Label(edited_frame, image=edited_tk_img)
        edited_img_label.image = edited_tk_img
        edited_img_label.pack()
        edited_img_labels.append(edited_img_label)

    zoomed = False

    def toggle_zoom():
        nonlocal zoomed
        for i, (original_img, edited_img) in enumerate(zip(resized_original_imgs, resized_edited_imgs)):
            if not zoomed:
                zoomed_original_img = original_img.resize((original_img.width * 2, original_img.height * 2))
                zoomed_edited_img = edited_img.resize((edited_img.width * 2, edited_img.height * 2))
                original_tk_img = ImageTk.PhotoImage(zoomed_original_img)
                original_img_labels[i].config(image=original_tk_img)
                original_img_labels[i].image = original_tk_img
                edited_tk_img = ImageTk.PhotoImage(zoomed_edited_img)
                edited_img_labels[i].config(image=edited_tk_img)
                edited_img_labels[i].image = edited_tk_img
            else:
                original_tk_img = ImageTk.PhotoImage(original_img)
                original_img_labels[i].config(image=original_tk_img)
                original_img_labels[i].image = original_tk_img
                edited_tk_img = ImageTk.PhotoImage(edited_img)
                edited_img_labels[i].config(image=edited_tk_img)
                edited_img_labels[i].image = edited_tk_img
        zoomed = not zoomed

    zoom_button = tk.Button(root, text="Zoom", command=toggle_zoom)
    zoom_button.pack()

    root.mainloop()



if __name__ == '__main__':
    process_image()
    