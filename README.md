# Invoice Analyzer AI

This is a mini-project that uses **Azure Form Recognizer** to extract structured data (e.g., vendor name, customer name, invoice date, and total amount) from uploaded invoice images or PDFs.

Built using **Streamlit**, this tool allows users to:
- Upload one or more invoices
- View extracted data in a user-friendly format
- Export results to CSV
- Handle South African invoices (ZAR currency)

---

## 🔍 Example Output

```json
[
  {
    "Vendor Name": "Msunduzi Municipality",
    "Customer Name": "Ms. GAIL CARLETTE BOARDMAN",
    "Invoice Date": "2025-04-15",
    "Invoice Total": "ZAR 1275.43"
  }
]
```

## 🚀 How to Run

1. Clone the repo
```bash
git clone https://github.com/AndrewCarlBoardman/invoice-analyser-ai.git
cd invoice-analyser-ai

2. Set up a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On macOS/Linux

3. Install dependencies
pip install -r requirements.txt

4. Configure Azure credentials
Create a .env file in the root directory using this format:

AZURE_FORM_RECOGNIZER_ENDPOINT=https://your-resource-name.cognitiveservices.azure.com/
AZURE_FORM_RECOGNIZER_KEY=your-key-here

Or copy from .env.example (included).

5. Run the app
streamlit run app.py

```

## ⚙️ Tech Stack
Python

Streamlit

Azure Form Recognizer

dotenv

##  Project Structure

invoice-analyser-ai/
├── app.py
├── extract_invoice.py
├── .env.example
├── requirements.txt
└── README.md


##  About the Author
This project is part of a portfolio of AI-powered mini apps by Andrew Boardman to demonstrate real-world use of AI and automation.

MIT Licensed.

