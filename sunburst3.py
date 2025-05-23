import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Sunburst Chart: Field → Internships → Starting Salary")

# Upload file
uploaded_file = st.file_uploader("Upload the Excel file", type="xlsx")

if uploaded_file is not None:
    # Load the uploaded Excel file
    df = pd.read_excel(uploaded_file, sheet_name='education_career_success')

    # Categorize salary
    def categorize_salary(salary):
        if salary < 30000:
            return '<30K'
        elif salary < 50000:
            return '30K–50K'
        elif salary < 70000:
            return '50K–70K'
        else:
            return '70K+'

    # Create grouped columns
    df['Salary_Group'] = df['Starting_Salary'].apply(categorize_salary)
    df['Internships_Group'] = pd.cut(df['Internships_Completed'], bins=[-1, 1, 3, 5], labels=['0–1', '2–3', '4–5'])

    # Group for sunburst
    sunburst_data = df.groupby(['Field_of_Study', 'Internships_Group', 'Salary_Group']).size().reset_index(name='Count')

    # Sunburst chart
    fig = px.sunburst(
        sunburst_data,
        path=['Field_of_Study', 'Internships_Group', 'Salary_Group'],
        values='Count',
        title='Field of Study → Internships → Starting Salary'
    )

    st.plotly_chart(fig)
