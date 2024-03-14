from setuptools import find_packages,setup

def get_requirments(file_path:str):
    '''
    this function will return requriments moduls

    '''
    HYPEN_DOT= "-e ."
    requirements=[]
    with open(file_path) as object:
        file=object.readlines()
        requirements=[req.replace("\n","") for req in file]
    if HYPEN_DOT in requirements:
        requirements.remove(HYPEN_DOT)


setup(
    name="ML_Project",
    version="0.0.1",
    author="Umez Harge",
    author_email="Umezharge63@gmail.com",
    packages=find_packages(),
    install_requires=get_requirments("requirements.txt")
)