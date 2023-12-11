from PyPDF2 import PdfWriter, PdfReader, PdfMerger
from datetime import datetime

reader = PdfReader("c.pdf")
page = reader.pages[0]
# print(page.cropbox.lower_left)
# print(page.cropbox.lower_right)
# print(page.cropbox.upper_left)
# print(page.cropbox.upper_right)

# Given coordinates for the scaled-down version
# scaled_coordinates = {
#     'lower_left': (97, 13),
#     'lower_right': (210, 13),
#     'upper_left': (97, 198),
#     'upper_right': (210, 198)
# }

# Dimensions of the scaled-down version
# scaled_width = 303
# scaled_height = 428

# # Dimensions of the unscaled version
# unscaled_width = 595
# unscaled_height = 842

# # Calculate scaling factors
# scaling_factor_x = unscaled_width / scaled_width
# scaling_factor_y = unscaled_height / scaled_height

# # Scale the coordinates for the unscaled version
# resulting_coordinates = {
#     'lower_left': (
#         int(scaled_coordinates['lower_left'][0] * scaling_factor_x),
#         int(scaled_coordinates['lower_left'][1] * scaling_factor_y)
#     ),
#     'lower_right': (
#         int(scaled_coordinates['lower_right'][0] * scaling_factor_x),
#         int(scaled_coordinates['lower_right'][1] * scaling_factor_y)
#     ),
#     'upper_left': (
#         int(scaled_coordinates['upper_left'][0] * scaling_factor_x),
#         int(scaled_coordinates['upper_left'][1] * scaling_factor_y)
#     ),
#     'upper_right': (
#         int(scaled_coordinates['upper_right'][0] * scaling_factor_x),
#         int(scaled_coordinates['upper_right'][1] * scaling_factor_y)
#     ),
# }

# print("Resulting Coordinates:", resulting_coordinates)


with open("c.pdf", "rb") as in_f:
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
        
    with open(datetime.now().strftime('%Y-%m-%d') + "-f-label" + ".pdf", "wb") as out_f:
        output1.write(out_f)
    
    with open(datetime.now().strftime('%Y-%m-%d') + "-f-invoice" + ".pdf", "wb") as out_f:
        output2.write(out_f)