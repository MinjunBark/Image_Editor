from PIL import Image, ImageEnhance, ImageFilter
import os
import matplotlib.pyplot as plt

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
    
    
def show_image(original_imgs, edited_imgs):
    num_images = len(original_imgs)
    fig, ax = plt.subplots(2, num_images, figsize=(12, 6))
    
    for i , (original_img, edited_img) in enumerate(zip(original_imgs, edited_imgs)):
        ax[0,i].imshow(original_img)
        ax[0,i].set_title(f'Original Image')
        ax[0,i].set_xticks([])
        ax[0,i].set_yticks([])
        
        ax[1,i].imshow(edited_img)
        ax[1,i].set_title(f'Edited Image')
        ax[1,i].set_xticks([])
        ax[1,i].set_yticks([])
    plt.tight_layout()
    plt.show()

def process_image():
    original_imgs = []
    edited_imgs = []
    for file in os.listdir(path):
        original_img = open_image(file)
        sharpened_img = adjust_sharpness(original_img, file)
        edited_imgs.append(sharpened_img)
        # brightened_img =adjust_brightness(sharpened_img, file)
        # contrasted_img = adjust_contrast(brightened_img, file)
        original_imgs.append(original_img)
        # edited_imgs.append(contrasted_img)
    
    
    show_image(original_imgs, edited_imgs)


if __name__ == '__main__':
    process_image()
    