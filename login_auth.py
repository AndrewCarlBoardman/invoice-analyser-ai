# login_auth.py
import streamlit as st
import msal
import os
from dotenv import load_dotenv
import logging

# Set logging level
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()

# Azure AD App settings
CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
TENANT_ID = os.getenv("AZURE_TENANT_ID")
REDIRECT_URI = os.getenv("AZURE_REDIRECT_URI")  # Must match exactly in Azure portal
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["User.Read"]

# Create MSAL app
def get_msal_app():
    return msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )

# Authentication flow
def login_flow():
    st.sidebar.title("🔐 Login with Microsoft")

    if "token" not in st.session_state:
        msal_app = get_msal_app()
        auth_url = msal_app.get_authorization_request_url(SCOPE, redirect_uri=REDIRECT_URI)

        st.sidebar.markdown(f"[Click here to login with Microsoft]({auth_url})")

        # Read authorization code from URL
        auth_code = st.query_params.get("code")
        if isinstance(auth_code, list):
            auth_code = auth_code[0]

        if auth_code:
            try:
                result = msal_app.acquire_token_by_authorization_code(
                    auth_code,
                    scopes=SCOPE,
                    redirect_uri=REDIRECT_URI
                )

                if "access_token" in result:
                    st.session_state.token = result["access_token"]
                    st.session_state.username = result.get("id_token_claims", {}).get("name", "User")
                    st.rerun()
                else:
                    st.sidebar.error(f"Authentication failed: {result.get('error_description', str(result))}")
            except Exception as e:
                st.sidebar.error("Authentication error. Please try again.")
                logging.error(f"Exception during token acquisition: {e}")

    else:
        st.sidebar.success(f"✅ Logged in as {st.session_state.username}")
        if st.sidebar.button("Logout"):
            for key in ["token", "username"]:
                st.session_state.pop(key, None)
            st.rerun()
