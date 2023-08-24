from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .'

def get_requirements(filepath):
    filepath = filepath
    with open(filepath,'r') as fileobj:
        requirements = [line.strip() for line in fileobj]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    
    return requirements
    

setup(
    name='Mini Flask Project',
    version='0.0.1',
    author='Noorul Ameen',
    author_email='noorulamean146@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)