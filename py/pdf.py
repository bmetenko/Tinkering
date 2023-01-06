import fpdf

TITLE_PAD = 4

class ExPDF(fpdf.FPDF):
    def footer(self):
        self.set_y(-25)
        self.set_font("helvetica", "I", 16)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="R", new_x="LEFT", new_y=fpdf.YPos.LAST)
        self.cell(0, 10, "Example PDF", align="L")

    def header(self):
        self.set_font("helvetica", "B", 15)
        title_width = self.get_string_width(self.title) + TITLE_PAD
        self.set_x(70)
        self.set_draw_color(0, 34, 123)
        self.set_fill_color(124, 255, 20)
        self.set_text_color(45, 4, 200)
        self.cell(
            title_width,
            10,
            self.title,
            border=1,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
            fill=True,
        )

        self.cell(60, 10, "Example PDF again", border=1, align="C")
        self.ln(20)
        self.cell(60, 10, "Example PDF twice", border=1, align="C")
        self.ln(20)

pdf = ExPDF()
pdf.set_title("Example PDF override")
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