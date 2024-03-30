import streamlit as st
from app import extract_data, extract_entities

def command(pdf):
    txt = extract_data(pdf)
    name, address, mob, email = extract_entities(txt)

    return name, address, mob, email


def main():
    st.set_page_config(
        page_title="WELCOME",
        page_icon="👋",
    )

    st.title('Resume Parser')
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    NAME = '' 
    ADDRESS = ''
    MOBILE = ''
    EMAIL = ''

    if st.button(label='Submit', type="primary"):
        st.success('File uploaded Successfully')
        NAME, ADDRESS, MOBILE, EMAIL = command(uploaded_file)

        st.write(f"Name:")
        st.text(f"{NAME}")

        st.write("Location:")
        st.text(f"{ADDRESS}")

        st.write("Mobile:")
        st.text(f"{MOBILE}")

        st.write("Email:")
        st.text(f"{EMAIL}")

if __name__ == "__main__":
    main()