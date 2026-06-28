from setuptools import setup, find_packages
from typing import List
HYPHON_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements"""
    requirements=[]
    with open(file_path) as f:
        requirements = f.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)
            return requirements

    

setup(
    name='ml_project',
    version='0.0.1',
    packages=find_packages(),
    author='BhumaViswa',
    author_email='bhumaviswa@example.com',
    description='A simple machine learning project',
    install_requires=get_requirements('requirements.txt')
)