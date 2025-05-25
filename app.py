import streamlit as st
from extract_invoice import extract_invoice_fields
import pandas as pd
from login_auth import login_flow

st.set_page_config(page_title="Invoice Analyzer AI")
st.title("📄 Invoice Analyzer AI")
st.write("Upload one or more invoices (PDF or image)")

login_flow()

if "token" not in st.session_state:
    st.stop()

if "username" in st.session_state:
    st.success(f"✅ Logged in as: {st.session_state.username}")

if "token" not in st.session_state:
    st.stop()

# Accept multiple file uploads
uploaded_files = st.file_uploader(
    "Upload invoices", type=["pdf", "png", "jpg", "jpeg"], accept_multiple_files=True
)

if uploaded_files:
    all_data = []

    for uploaded_file in uploaded_files:
        st.write(f"Processing: {uploaded_file.name}")
        file_bytes = uploaded_file.read()
        invoice_data = extract_invoice_fields(file_bytes)

        for invoice in invoice_data:
            invoice["File Name"] = uploaded_file.name  # Add file name for context
            all_data.append(invoice)

    # Display results
    df = pd.DataFrame(all_data)
    st.subheader("📊 Extracted Invoice Data")
    st.dataframe(df)

    # Prepare for export
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="extracted_invoice_data.csv",
        mime="text/csv",
    )
