import streamlit as st
import zipfile
import img2pdf
import io

# Page Config
st.set_page_config(page_title="Zip to PDF Converter", page_icon="📄")

# Design the UI
st.title("📦 Zip to PDF Converter")
st.write("Upload a Zip file containing images, and I'll turn it into a PDF!")

# File uploader icon/box
uploaded_file = st.file_uploader("Choose a Zip file", type="zip")

if uploaded_file is not None:
    st.success("Zip file uploaded successfully!")
    
    if st.button("Convert to PDF"):
        images = []
        
        # Open the uploaded zip directly from memory
        with zipfile.ZipFile(uploaded_file, 'r') as archive:
            file_list = sorted(archive.namelist())
            
            for file_name in file_list:
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                    images.append(archive.read(file_name))
        
        if images:
            # Create PDF in memory
            pdf_data = img2pdf.convert(images)
            
            # Create a download button
            st.download_button(
                label="📥 Download Your PDF",
                data=pdf_data,
                file_name="converted_images.pdf",
                mime="application/pdf"
            )
            st.balloons() 
        else:
            st.error("No images (JPG/PNG) found inside that Zip file.")