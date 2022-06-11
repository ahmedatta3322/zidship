from fpdf import FPDF


class WayBillServices:
    def __init__(self):
        pass

    def convert_to_pdf(self, waybill):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Waybill", ln=1, align="C")
        pdf.cell(200, 10, txt="Shipment: {}".format(waybill.shipment), ln=1, align="C")
        pdf.cell(200, 10, txt="Carrier: {}".format(waybill.carrier), ln=1, align="C")
        pdf.cell(200, 10, txt="Sender: {}".format(waybill.sender), ln=1, align="C")
        pdf.cell(200, 10, txt="Receiver: {}".format(waybill.receiver), ln=1, align="C")
        pdf.cell(200, 10, txt="Packages: {}".format(waybill.packages), ln=1, align="C")
        pdf.output("waybill.pdf")
        return pdf

    def print_waybill(self, waybill):
        pdf = self.convert_to_pdf(waybill)
        pdf.output("waybill.pdf", "F")
        pdf.output("waybill.pdf", "I")
        return pdf
