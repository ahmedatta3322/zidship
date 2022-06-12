from fpdf import FPDF
import os


class WayBillServices:
    def __init__(self):
        pass

    # Description: Convert waybill to pdf
    def convert_to_pdf(waybill):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Waybill", ln=1, align="C")
        pdf.cell(
            200,
            10,
            txt="Waybill Number: " + str(waybill.way_bill_number),
            ln=1,
            align="L",
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
            txt="Shipment: " + str(waybill.shipment.shipment_number),
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

    # Description: Print waybill
    def print_waybill(waybill, printer_name):
        pdf = WayBillServices.convert_to_pdf(waybill)

        pdf.output(f"waybill_{waybill.way_bill_number}.pdf", "F")
        os.system(f"lpr -P {printer_name} waybill_{waybill.way_bill_number}.pdf")
        return pdf

    def map_shipment_status(shipment):
        # Update shipment object status to shipment.shipment_status
        if shipment.shipment_status == "In Transit":
            shipment.shipment_status = "In Transit"
            shipment.save()
        elif shipment.shipment_status == "Delivered":
            shipment.shipment_status = "Delivered"
            shipment.save()
        elif shipment.shipment_status == "Cancelled":
            shipment.shipment_status = "Cancelled"
            shipment.save()
        return shipment
