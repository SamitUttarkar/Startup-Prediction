from setuptools import find_packages,setup
from typing import List
#setup.py can help put our application as a py file and deploy it
# Building our application as a package 
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name = 'Startup-Prediction',
    version = '0.0.1',
    author = 'Samit',
    author_email='samituttarkar@gmail.com',
    packages=find_packages(), #searched folder which have __init__.py and build package 
    install_requires=get_requirements('requirements.txt')   
)