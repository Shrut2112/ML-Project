# why we need it ? - it is very useful to build our application as python package
from setuptools import find_packages,setup
from typing import List

#use -e . in requirements.txt to trigger setup.py 
def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path, 'r') as f:
        requirements=f.readlines()
        requirements=[req.replace('/n','') for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name='ml_project',
    version='1.0',
    author='shrut',
    author_email='jainshrutd211204@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)