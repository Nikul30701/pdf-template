from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit = "mm", format="A4" )

df = pd.read_csv("topic1.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times",style="B", size=24)
    pdf.set_text_color(0,0,260)
    pdf.cell(w=0,h=12, txt = row["Topic"], align="L",
         ln=1)
    pdf.line(10,22,200,22)

pdf.output("output.pdf")