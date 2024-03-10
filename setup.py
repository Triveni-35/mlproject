from setuptools import find_packages,setup

from typing import List

hyphenedot = '-e .'
def get_requirements(file_path:str)->List[str]:
    ''' return list of requirements '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        [req.replace('\n','') for req in requirements]
    if hyphenedot in requirements:
        requirements.remove(hyphenedot)

setup(
name = 'mlproject',
version = '0.0.1',
author='Triveni P',
author_email='ugs21016_cse.triveni@cbit.org.in',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')

)