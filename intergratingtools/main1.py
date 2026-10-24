from fastapi import FastAPI
from models1 import Developer, Project

app=FastAPI()

@app.post('/developer/')
def create_developer(developer: Developer):
    return{'message':'Developer created successfully', 'developer':developer}

@app.post('/project')
def create_project(project:Project):
    return {'message':'Project created successfully', 'project':project}

@app.get('/projects/')
def get_projects():
    sample_project= Project(
        title='Sample Project',
        description='This is a sample project',
        languages=['Python', 'JavaScript'],
        lead_developer=Developer(name='Jane Doe', experience=5)
    )
    return{'project':[sample_project]}