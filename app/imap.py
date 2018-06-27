
# imap.py
# Class file for handling application logic and building interface.

import os
import csv
import meta
import tkinter as tk
from model import Image
from tkinter import messagebox
from tkinter import filedialog

class iMap(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.setup_widgets()
        self.pack(padx=20, pady=20)

    # Creates widgets for the interface.
    def create_widgets(self):
        self.img_folder_label = tk.Label(self,text='Image Folder')
        self.img_folder = tk.Entry(self, width=30)
        self.img_folder_btn = tk.Button(self, text="Browse", command=self.browse_image_folder)
        self.export_folder_label = tk.Label(self, text='Export Folder')
        self.export_folder = tk.Entry(self, width=30)
        self.export_folder_btn = tk.Button(self, text="Browse", command=self.browse_export_folder)
        self.export_btn = tk.Button(self, width=20, text="Export", command=self.export)
    
    # Places widgets on the interface in a grid layout.
    def setup_widgets(self):
        self.img_folder_label.grid(row=0, column=1, padx=10, pady=0, sticky='W')
        self.img_folder.grid(row=1, column=1, padx=10, pady=10, sticky='W')
        self.img_folder_btn.grid(row=1, column=2, padx=10, pady=10)
        self.export_folder_label.grid(row=2, column=1, padx=10, pady=0, sticky='W')
        self.export_folder.grid(row=3, column=1, padx=10, pady=10, sticky='W')
        self.export_folder_btn.grid(row=3, column=2, padx=10, pady=10)
        self.export_btn.grid(row=4, columnspan=3, pady=10)

    # Handles folder selection for the image folder and sets
    # entry field to the folder path selected by the user.
    def browse_image_folder(self):
        file_path = filedialog.askdirectory()
        if (file_path):
            if (self.has_images(file_path)):
                self.img_folder.delete(0, 'end')
                self.img_folder.insert(0, file_path)
            else:
                messagebox.showwarning(title="Folder Error", message="The folder you selected does " 
                                             + "not contain the proper file types. Please try again.")

    # Handles folder selection for the export folder and sets 
    # entry field to the folder path selected by the user.
    def browse_export_folder(self):
        file_path = filedialog.askdirectory()
        if (file_path):
            self.export_folder.delete(0, 'end')
            self.export_folder.insert(0, file_path)

    # Checks if the specified path contains images (.jpg images only)
    def has_images(self, path):
        for item in os.listdir(path):
            if item[0] == '.':
                continue
            if (not item.endswith('.jpg')):
                return False
        return True

    # Extracts meta data from image and stores them
    # in an image object.
    def process_image(self, image_path, export_path, name):
        image = Image()
        date = str(meta.get_date(image_path + name))
        lat, lon = meta.get_gps(image_path + name)
        address = meta.reverse_geocode(lat, lon)
        new_name = meta.create_new_name(address, date)

        if (date, lat, lon, address, new_name):
            with open(export_path + new_name, 'wb') as img1:
                data = ''
                with open(image_path + name, 'rb') as img2:
                    data = img2.read()
                img1.write(data)

            image.set_date_created(date)
            image.set_original_name(name)
            image.set_lat(lat)
            image.set_lon(lon)
            image.set_address(address)
            image.set_new_name(new_name)

            return image
        else:
            messagebox.showerror(title="Image Error", message="An error occured while trying to process "
                                                + "your images. Please check to make sure they contain meta "
                                                + "data/GPS info. It is also possible that Google's geocoding "
                                                + "service was unable to process your images' information.")

    # Looks through selected directories, processes each image, and exports
    # renamed images and a csv file with all the meta data for each image. 
    def export(self):
        images = []
        image_folder_path = self.img_folder.get() + '/'
        export_folder_path = self.export_folder.get() + '/'

        if (self.img_folder.get() and self.export_folder.get()):
            if (os.path.isdir(self.img_folder.get()) and os.path.isdir(self.export_folder.get())):
                messagebox.showinfo(title="Geocoding Started!", message="Your images are now being geocoded! "
                                                        + "Please wait for a confirmation message stating that "
                                                        + "the process has finished.") 

                for img in os.listdir(image_folder_path):
                    if (not img.startswith('.')):
                        img = self.process_image(image_folder_path, export_folder_path, img)
                        images.append(img)

                data = [['date_created', 'original_name', 'lat', 'lon', 'address', 'new_name']]

                for img in images:
                    obj = []
                    obj.append(img.get_date_created())
                    obj.append(img.get_original_name())
                    obj.append(img.get_lat())
                    obj.append(img.get_lon())
                    obj.append(img.get_address())
                    obj.append(img.get_new_name())
                    data.append(obj)

                with open(export_folder_path + 'data.csv', 'w') as f:
                    writer = csv.writer(f)
                    writer.writerows(data)

                messagebox.showinfo(title="Success!", message="Your images have been geocoded and exported! "
                                        + "Please check your export folder to view your new images and csv file.") 
            else:
                messagebox.showerror(title="Path Error", message="One or both of your folder paths are incorrect. "
                                        + "Please ensure that the folder paths you entered exist on your computer "
                                        + "before you try to export.") 
        else:
            messagebox.showerror(title="Folder Error", message="Please make sure you have an "
                                    + "image folder and export folder selected before exporting.")
        

    

