# from pystrich.datamatrix import DataMatrixEncoder
# from fpdf import FPDF
# import csv
#
# count = 1
# pdf = FPDF(orientation='L', format=(20, 70))
#
# with open('order.csv', 'r') as file:
#     reader = csv.reader(file, delimiter='\n')
#     for row in reader:
#         data = row[0]
#         encoder = DataMatrixEncoder(data)
#         encoder.save('datamatrix.jpg')
#         pdf.add_page()
#         pdf.set_font("Arial", size=6)
#         pdf.image('datamatrix.jpg', x=2, y=2, w=15)
#         pdf.set_xy(19, 2)
#         pdf.cell(0, 4, border=1,  txt=data[13: 31], ln=1, align='L')
#         count += 1
#         if count > 10:
#             break
#
# pdf.output("example.pdf")
#
#


from pystrich.datamatrix import DataMatrixEncoder
from fpdf import FPDF
import csv

count = 1
pdf = FPDF(orientation='L', format=(20, 70))

with open('order.csv', 'r') as file:
    reader = csv.reader(file, delimiter='\n')
    for row in reader:
        if count > 10:
            break
        data = row[0]
        encoder = DataMatrixEncoder(data)
        encoder.save(f'datamatrix{count}.jpg')
        pdf.add_page()
        pdf.set_xy(0, 0)
        # pdf.image(f'datamatrix{count}.jpg', x=2, y=2, w=15)
        pdf.image(f'datamatrix{count}.jpg', w=1)
        pdf.set_font("Arial", size=6)
        pdf.set_xy(19, 2)
        pdf.cell(30, 4, border=1, txt=data[13: 14], ln=0, align='L')
        count += 1
pdf.output("example.pdf")