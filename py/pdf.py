from fpdf import FPDF

pdf = FPDF(orientation="L", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(40, 10, "Hello World! 40x10")
pdf.cell(50, 50, "Hello World! 50x50")
pdf.cell(75, 75, "Hello World! 75x75")
pdf.cell(95, 75, "Hello World! 95x75")
pdf.cell(95, 25, "Hello World! 95x25")
pdf.output("helloworld.pdf")
