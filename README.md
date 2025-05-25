# 📊 Invoice Analyzer (with Microsoft 365 Login)

[![Invoice Analyzer](https://img.shields.io/badge/Streamlit-Invoice%20Analyzer-blue)](https://github.com/AndrewCarlBoardman/invoice-analyzer)

This Streamlit app allows users to securely log in with their Microsoft 365 (Azure Active Directory) credentials and analyze South African invoices using AI. It supports batch uploads, AI extraction, and CSV export — ideal for MSPs or small finance teams.

---

## 🚀 Features

- 🔐 **Microsoft 365 Login (Azure AD)**
- 📁 **Upload multiple invoices (PDFs)**
- 🧠 **AI-powered data extraction**
- 📊 **View and analyze results in a dashboard**
- 📤 **Export to CSV**
- 🇿🇦 **Optimized for South African invoice formats**

---

## 🧰 Tech Stack

- Python
- Streamlit
- MSAL (Microsoft Authentication Library)
- Azure Form Recognizer (optional)
- `dotenv` for environment management

---

##  📁 Project Structure

invoice-analyzer-ai/
├── app.py # Main Streamlit app
├── login_auth.py # Azure AD login logic
├── extract_invoice.py # AI invoice processing
├── test_extract.py # Test cases for invoice extraction
├── test.py # Placeholder/test script
├── requirements.txt # Dependencies
├── .env.example # Sample environment config
└── README.md

---

## 🛠️ Getting Started

1. Clone the Repository

```bash
git clone https://github.com/AndrewCarlBoardman/invoice-analyzer.git
cd invoice-analyzer
```

2. Set Up Environment Variables
Create a .env file in the project root:

AZURE_CLIENT_ID=your-client-id
AZURE_CLIENT_SECRET=your-client-secret
AZURE_TENANT_ID=your-tenant-id
AZURE_REDIRECT_URI=http://localhost:8501

3. Install Requirements
pip install -r requirements.txt

4. Run the App
streamlit run app.py

---

## 🔐 Azure AD Setup

Go to Azure Portal

Register an App → Add Redirect URI: http://localhost:8501

Configure "User.Read" Microsoft Graph permission

Generate a client secret and copy it to your .env

You're ready to log in via Microsoft 365!

---

## 📤 Output Example

A successfully processed invoice CSV will contain:

Invoice No	Date	Vendor	Total (ZAR)	VAT (ZAR)
001	2024-04-10	ABC Corp	1,150.00	150.00

---

## 💼 Use Cases

Internal MSP invoice auditing

Freelancers managing client PDFs

Small business finance automation

AI + Azure portfolio demo

---

## 🧑‍💻 Author

Andrew Boardman
Systems Engineer • AI Developer
🔗 GitHub

---

## 🪪 License

MIT Licensed — free to use and adapt for educational and personal projects.

yaml
Copy
Edit

---

### ✅ Next Steps in GitHub

1. Replace the current `README.md` with the above.
2. Commit and push:
   ```bash
   git add README.md
   git commit -m "Update README with project badge, features, and setup guide"
   git push

