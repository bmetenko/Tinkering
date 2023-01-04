import fpdf

class ExPDF(fpdf.FPDF):
    def footer(self):
        self.set_y(-25)
        self.set_font("helvetica", "I", 16)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="R", new_x="LEFT", new_y=fpdf.YPos.LAST)
        self.cell(0, 10, "Example PDF", align="L")

pdf = ExPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
for x in range(10):
    for y in range(10):
        pdf.cell(
            150, 10, f"Hello World! {x=} by {y=}\n", 
            border=1,
            new_x="LEFT",
            new_y="NEXT"
            )

pdf.output("helloworld.pdf")