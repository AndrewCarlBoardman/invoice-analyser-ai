from extract_invoice import extract_invoice_fields

data = extract_invoice_fields("sample_invoices/inv-I2711524-27646848423-2025-05-01_029.PDF")
print(data)