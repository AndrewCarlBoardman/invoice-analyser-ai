from extract_invoice import extract_invoice_fields

# Change this to your sample invoice path
file_path = "sample_invoices/inv-I2711524-27646848423-2025-05-01_029.PDF"

data = extract_invoice_fields(file_path)
print("Extracted Data:")
for item in data:
    for k, v in item.items():
        print(f"{k}: {v}")
    print("---")
