# https://cs50.harvard.edu/python/2022/psets/8/shirtificate/

from fpdf import FPDF
from fpdf.enums import XPos, YPos

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('shirtificate.png', x=25, y=50, w=150, h=150)

        # Arial bold 15
        self.set_font("helvetica", "B", 45)

        # Title
        self.text(30,25, 'CS50 Shirtificate')

    def footer(self):
        self.set_font("helvetica", "B", 25)
        # make white
        self.set_text_color(255,255,255)
        self.text(72, 140, name + " took CS50")

name = input("what's your name? ")
#pdf = PDF()
pdf = PDF(orientation="P", format="A4", unit = "mm")
pdf.add_page()
pdf.output("shirtificate.pdf")

"""

"""