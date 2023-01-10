import fpdf
import pandas as pd
import matplotlib.pyplot as plt

TITLE_PAD = 4

data = {"Ounces": [325, 337.5, 350, 362.5], "Cost": [50, 45, 40, 22]}

#load data into a DataFrame object:
df = pd.DataFrame(data)

fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
ax.plot(data["Ounces"], data["Cost"])
fig.savefig('plot.png')   # save the figure to file
plt.close(fig)


class ExPDF(fpdf.FPDF):

    def simple_table(self, headings, rows):
        for heading in headings:
            self.cell(30, 12, heading, 1, align="C")
        self.ln()
        self.set_fill_color(23, 100, 100)
        fill = False
        for row in rows:
            fill = not fill
            self.set_text_color(255 if fill else 0)
            for col in row:
                self.cell(30, 10, col, 1, align="C", fill=fill)
                
            self.ln()
        
        self.ln(20)


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
pdf.simple_table(
    headings=df.columns, 
    rows=[df.iloc[i, :].astype(str).tolist() for i in range(len(df))],
    )
pdf.image(
    "plot.png", 
    pdf.get_x(), pdf.get_y(), 
    50, 0,
    "Plot of cost per ounces",
    "https://github.com/bmetenko"
    )
pdf.ln(50)

pdf.write_html(
"""
html render:
<br>
<b>bolded</b>, <i>italicized</i>,
<u>underlined</u>, and <b><i><u>all three</u></i></b>!
<br><br>
<a href="https://github.com/bmetenko">self.website</a>
<br><br>
Chart linked to the same website because it is clickable.
"""
)
pdf.ln(20)

pdf.set_font("helvetica", "B", 16)
pdf.set_text_color(0)
for x in range(10):
    for y in range(10):
        pdf.cell(
            150, 10, f"Hello World! {x=} by {y=}\n", 
            border=1,
            new_x="LEFT",
            new_y="NEXT"
            )

pdf.output("helloworld.pdf")