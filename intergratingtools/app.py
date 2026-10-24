import streamlit as st
import requests 
import pandas as pd

st.title('Project Menagment App')
st.header('Add a Developer')
dev_name=st.text_input('Developer Name')
dev_experience=st.number_input('Experience (Years)', min_value=0, max_value=50, value=0)

if st.button('Create Developer'):
    dev_data={'name':dev_name, 'experience':dev_experience}
    response=requests.post('http://localhost:8000/developers/', json=dev_data)
    st.json(response.json())

st.header('Add a Project')
proj_title=st.text_input('Project Title')
proj_desc=st.text_area('Project Description')
proj_langs=st.text_input('Languages Used (Comma-Seperated)')
lead_dev=st.text_input('Lead Developer Name')
lead_dev_exp=st.number_input('Lead Developer Experience (Years)', min_value=0, max_value=50, value=0)

if st.button('Create Project'):
    lead_dev_data={'name':lead_dev_name, 'experience':lead_dev_exp}
    proj-data={'title':proj_title, 'description':proj_desc, 'languages':proj_langs, 'lead_developer':lead_dev_data}

    response+requests.post


st.header('Project Dashboard')

if st.button('Get Project'):
    response=requests.get('http://localhost:8000/developers/')
    proj_data=response.json()['projects']

    if proj_data:
        proj_df=pd.DataFrame(proj_data)
        st.subheader('Project Overview')
        st.dataframe(proj_df)
        st.subheader('Project Details')
        for project in proj_data:
            st.markdown(f'**Title:**{project['title']}')
            st.markdown(f'**Title:**{project['description']}')
            st.markdown(f'**Title:**{',' .join(project['languages'])}')
            st.markdown(f'**Title:**{project['lead_deceloper']['name']} with {project['lead_developer']['experience']} years of experience')
    else:
        st.warning('No project found.')