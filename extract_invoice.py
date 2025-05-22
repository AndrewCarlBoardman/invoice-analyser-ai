import os
from dotenv import load_dotenv
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from io import BytesIO

# Load environment variables
load_dotenv()

endpoint = os.getenv("AZURE_FORM_RECOGNIZER_ENDPOINT")
key = os.getenv("AZURE_FORM_RECOGNIZER_KEY")

if not endpoint or not isinstance(endpoint, str):
    raise ValueError("AZURE_FORM_RECOGNIZER_ENDPOINT is missing or not a valid string.")
if not key or not isinstance(key, str):
    raise ValueError("AZURE_FORM_RECOGNIZER_KEY is missing or not a valid string.")

# Initialize client
document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)


def extract_invoice_fields(file_bytes):
    file_stream = BytesIO(file_bytes)

    # Run prebuilt-invoice model
    invoice_poller = document_analysis_client.begin_analyze_document(
        "prebuilt-invoice", document=file_stream
    )
    invoice_result = invoice_poller.result()

    # Rewind the stream to use it again for layout
    file_stream.seek(0)

    # Run prebuilt-layout model
    layout_poller = document_analysis_client.begin_analyze_document(
        "prebuilt-layout", document=file_stream
    )
    layout_result = layout_poller.result()

    return parse_result(invoice_result, layout_result)


def clean_vendor_name(vendor_name, layout_lines):
    if not vendor_name or len(vendor_name) < 10 or "pietermaritz" in vendor_name.lower():
        for line in layout_lines:
            if "msunduzi municipality" in line.lower():
                return "Msunduzi Municipality"
    return vendor_name


def parse_result(invoice_result, layout_result):
    extracted_data = []

    layout_lines = [
        line.content for page in layout_result.pages for line in page.lines
    ]

    for invoice in invoice_result.documents:
        fields = invoice.fields

        vendor_raw = fields.get("VendorName").value if "VendorName" in fields else None
        vendor_clean = clean_vendor_name(vendor_raw, layout_lines)

        data = {
            "Vendor Name": vendor_clean,
            "Customer Name": fields.get("CustomerName").value if "CustomerName" in fields else None,
            "Invoice Date": fields.get("InvoiceDate").value if "InvoiceDate" in fields else None,
            "Invoice Total": fields.get("InvoiceTotal").value if "InvoiceTotal" in fields else None,
        }
        extracted_data.append(data)

    return extracted_data
