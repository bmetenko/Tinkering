import fpdf

pdf = fpdf.FPDF()
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