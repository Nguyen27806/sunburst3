import pandas as pd

# Reload the data to prepare it for export in grouped format
df = pd.read_excel('/mnt/data/education_career_success.xlsx', sheet_name='education_career_success')

# Group and categorize the data
def categorize_salary(salary):
    if salary < 30000:
        return '<30K'
    elif salary < 50000:
        return '30K–50K'
    elif salary < 70000:
        return '50K–70K'
    else:
        return '70K+'

df['Salary_Group'] = df['Starting_Salary'].apply(categorize_salary)

# Prepare the data for sunburst: Field → Internships → Salary
df['Internships_Group'] = pd.cut(df['Internships_Completed'], bins=[-1, 1, 3, 5], labels=['0–1', '2–3', '4–5'])

# Group the data
sunburst_data = df.groupby(['Field_of_Study', 'Internships_Group', 'Salary_Group']).size().reset_index(name='Count')

import plotly.express as px

# Create the sunburst chart
fig = px.sunburst(
    sunburst_data,
    path=['Field_of_Study', 'Internships_Group', 'Salary_Group'],
    values='Count',
    title='Field of Study → Internships → Starting Salary',
)

fig.show()
