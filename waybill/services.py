from fpdf import FPDF
import os


class WayBillServices:
    def __init__(self):
        pass

    def convert_to_pdf(waybill):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Waybill", ln=1, align="C")
        pdf.cell(
            200, 10, txt="Waybill Number: " + waybill.way_bill_number, ln=1, align="L"
        )
        pdf.cell(
            200, 10, txt="Waybill Label: " + waybill.way_bill_label, ln=1, align="L"
        )
        pdf.cell(200, 10, txt="Carrier: " + waybill.carrier.name, ln=1, align="L")
        pdf.cell(200, 10, txt="Sender: " + waybill.sender.name, ln=1, align="L")
        pdf.cell(200, 10, txt="Receiver: " + waybill.receiver.name, ln=1, align="L")
        pdf.cell(
            200,
            10,
            txt="Shipment: " + waybill.shipment.shipment_number,
            ln=1,
            align="L",
        )
        # add all packages from shipment queryset

        for package in waybill.shipment.packages.all():
            pdf.cell(200, 10, txt="Package: " + str(package.id), ln=1, align="L")
            pdf.cell(
                200, 10, txt="Package weight: " + str(package.weight), ln=1, align="L"
            )
            pdf.cell(
                200,
                10,
                txt="Package description: " + package.description,
                ln=1,
                align="L",
            )
            pdf.cell(
                200, 10, txt="Package type: " + package.package_type, ln=1, align="L"
            )

        return pdf

    def print_waybill(waybill, printer_name):
        pdf = WayBillServices.convert_to_pdf(waybill)
        pdf.output(f"waybill_{waybill.way_bill_number}.pdf", "F")
        os.system(f"lpr -P {printer_name} waybill_{waybill.way_bill_number}.pdf")
        return pdf
