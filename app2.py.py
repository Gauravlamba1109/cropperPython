from PyPDF2 import PdfWriter, PdfReader, PdfMerger
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime
import os
from PIL import Image, ImageTk, ImageDraw

class PdfCropperApp:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF Cropper for Flipkart Label")

        self.master.geometry("440x270") 
        
         # Set style for the window
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#DA291C")
        self.style.configure("TButton",background="#DA291C", foreground="#63666A" ,padding=(10, 8), font=("Futura", 15, "bold"),
                             borderwidth=4, relief="groove", cursor="arrow")
        
        # self.style.map("TButton", background=[('active', '#E56DB1')])
        self.style.configure("TLabel", forground="#C7B2DE",background="#DA291C", font=("Futura", 16,"bold"))
        self.style.configure("TEntry", fieldbackground="#fff")

        self.file_path = tk.StringVar()

        image_path = "balakPluslogo.png"  # Replace with the actual image file path
        self.image = Image.open(image_path)
        self.image = self.image.resize((200, 200))
        self.tk_image = ImageTk.PhotoImage(self.image)
        
        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.master)
        frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        image_label = ttk.Label(frame, image=self.tk_image)
        image_label.grid(row=0, column=0, rowspan=3, padx=10)
       
        # File Selection
        # ttk.Label(frame, text="Select PDF File:", foreground="#C7B2DE").grid(row=0, column=1, pady=10)
        browse_button = ttk.Button(frame, text="Browse PDF", command=self.browse_pdf)
        browse_button.grid(row=1, column=1, padx=10, pady=10)
        
        # # Crop Coordinates
        # ttk.Label(frame, text="Property of SRG Enterprise").grid(row=1, column=1, pady=10, sticky=tk.E)

        # Crop Button
        ttk.Button(frame, text="Crop PDF", command=self.crop_pdf).grid(row=2, column=1, pady=10)

    def browse_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        self.file_path.set(file_path)

    def crop_pdf(self):
        pdf_path = self.file_path.get()

        if not pdf_path:
            tk.messagebox.showerror("Error", "Please select a PDF file.")
            return

        try:
            # lower_left = tuple(map(int, self.lower_left_entry.get().split(',')))
            # upper_right = tuple(map(int, self.upper_right_entry.get().split(',')))

            reader = PdfReader(pdf_path)
            page = reader.pages[0]
            
            with open(pdf_path, 'rb') as in_f:
                input1 = PdfReader(in_f)
                output1 = PdfWriter()
                output2 = PdfWriter()

                for i in range(len(reader.pages)):
                    page1 = reader.pages[i]
                    page1.mediabox.lower_left = (185, 455)
                    page1.mediabox.lower_right = (410, 455)
                    page1.mediabox.upper_left = (185, 820)
                    page1.mediabox.upper_right = (410, 820)
                    output1.add_page(page1)
                    
                    page2 = reader.pages[i]
                    page2.mediabox.lower_left = (50,100)
                    page2.mediabox.lower_right = (550,100)
                    page2.mediabox.upper_left = (50, 455)
                    page2.mediabox.upper_right = (550, 455)
                    output2.add_page(page2)
                    
                
                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                flipkart_folder = os.path.join(desktop_path, "Flipkart")
                
                os.makedirs(flipkart_folder, exist_ok=True)
                date_folder = datetime.now().strftime('%Y-%m-%d')
                output_folder = os.path.join(flipkart_folder, date_folder)
                os.makedirs(output_folder, exist_ok=True)
                
                output_filename1 = datetime.now().strftime('%Y%m%d_%H%M%S') + "_label.pdf"
                output_filename2 = datetime.now().strftime('%Y%m%d_%H%M%S') + "_invoice.pdf"
                
                output_path1 = os.path.join(output_folder, output_filename1)
                output_path2 = os.path.join(output_folder, output_filename2)
                with open(output_path1, "wb") as out_f:
                    output1.write(out_f)
                
                with open(output_path2, "wb") as out_f:
                    output2.write(out_f)

            # with open(pdf_path, 'rb') as file:
            #     pdf_reader = PyPDF2.PdfFileReader(file)
            #     pdf_writer = PyPDF2.PdfFileWriter()

            #     for page_number in range(pdf_reader.numPages):
            #         page = pdf_reader.getPage(page_number)
            #         page.cropBox.lowerLeft = lower_left
            #         page.cropBox.upperRight = upper_right
            #         pdf_writer.addPage(page)

            #     output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            #     with open(output_path, 'wb') as output_file:
            #         pdf_writer.write(output_file)

                tk.messagebox.showinfo("Success", "PDF cropped successfully.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PdfCropperApp(root)
    root.mainloop()




# from PyPDF2 import PdfWriter, PdfReader, PdfMerger
# from datetime import datetime

# reader = PdfReader("c.pdf")
# page = reader.pages[0]
# # print(page.cropbox.lower_left)
# # print(page.cropbox.lower_right)
# # print(page.cropbox.upper_left)
# # print(page.cropbox.upper_right)

# # Given coordinates for the scaled-down version
# # scaled_coordinates = {
# #     'lower_left': (97, 13),
# #     'lower_right': (210, 13),
# #     'upper_left': (97, 198),
# #     'upper_right': (210, 198)
# # }

# # Dimensions of the scaled-down version
# # scaled_width = 303
# # scaled_height = 428

# # # Dimensions of the unscaled version
# # unscaled_width = 595
# # unscaled_height = 842

# # # Calculate scaling factors
# # scaling_factor_x = unscaled_width / scaled_width
# # scaling_factor_y = unscaled_height / scaled_height

# # # Scale the coordinates for the unscaled version
# # resulting_coordinates = {
# #     'lower_left': (
# #         int(scaled_coordinates['lower_left'][0] * scaling_factor_x),
# #         int(scaled_coordinates['lower_left'][1] * scaling_factor_y)
# #     ),
# #     'lower_right': (
# #         int(scaled_coordinates['lower_right'][0] * scaling_factor_x),
# #         int(scaled_coordinates['lower_right'][1] * scaling_factor_y)
# #     ),
# #     'upper_left': (
# #         int(scaled_coordinates['upper_left'][0] * scaling_factor_x),
# #         int(scaled_coordinates['upper_left'][1] * scaling_factor_y)
# #     ),
# #     'upper_right': (
# #         int(scaled_coordinates['upper_right'][0] * scaling_factor_x),
# #         int(scaled_coordinates['upper_right'][1] * scaling_factor_y)
# #     ),
# # }

# # print("Resulting Coordinates:", resulting_coordinates)


# with open("c.pdf", "rb") as in_f:
#     input1 = PdfReader(in_f)
#     output1 = PdfWriter()
#     output2 = PdfWriter()

#     for i in range(len(reader.pages)):
#         page1 = reader.pages[i]
#         page1.mediabox.lower_left = (185, 455)
#         page1.mediabox.lower_right = (410, 455)
#         page1.mediabox.upper_left = (185, 820)
#         page1.mediabox.upper_right = (410, 820)
#         output1.add_page(page1)
        
#         page2 = reader.pages[i]
#         page2.mediabox.lower_left = (50,100)
#         page2.mediabox.lower_right = (550,100)
#         page2.mediabox.upper_left = (50, 455)
#         page2.mediabox.upper_right = (550, 455)
#         output2.add_page(page2)
        
#     with open(datetime.now().strftime('%Y-%m-%d') + "-f-label" + ".pdf", "wb") as out_f:
#         output1.write(out_f)
    
#     with open(datetime.now().strftime('%Y-%m-%d') + "-f-invoice" + ".pdf", "wb") as out_f:
#         output2.write(out_f)