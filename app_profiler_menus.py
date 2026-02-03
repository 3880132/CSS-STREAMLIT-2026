import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="ABIOLA A BABAJIDE (MSc.)", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",["Researcher Profile", "Research Interests", "Professional Experience", "Publications", "Contact"],
)


# Sections based on menu selection

#Researcher Profile
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options") 

    # Collect basic information
    name = "Abiola A. Babajide"
    field = "Biomedical Informatics"
    institution = "University of the Western Cape"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    
    st.image("https://sl.bing.net/duBzFZd95To",
    caption="Biomedical Nitty-Gritty"
)

#Reserch Interests
elif menu == "Research Interests":
    st.title("Research Interests")
    st.sidebar.header("To be uploaded soon")
  
    
#Professional Experience 
elif menu == "Professional Experience":
    st.title("Professional Experience")
    st.sidebar.header("To be uploaded soon")
       
        
#Publications    
elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")
    

    # Upload publications file
    uploaded_file = st.file_uploader("Upload a PDF of Publications", type="pdf")
    if uploaded_file:
        publications = pd.read_pdf(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The PDF does not have a 'Year' column to visualize trends.")
        

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "3880132@myuwc.ac.za"
    st.write(f"You can reach me at {email}.")