from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Read dependencies from a requirements file,
    clean up whitespace and remove editable flags (-e .).
    """
    requirements = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                req = line.strip()
                # Skip empty lines and editable installs
                if req and not req.startswith('-e'):
                    requirements.append(req)
    except FileNotFoundError:
        print(f" Warning: {file_path} not found. Continuing without it.")
    return requirements


setup(
    name='MLProject',
    version='0.1.0',
    author='Maliha Mehnaz',
    author_email='malihamehnazcse2gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='A machine learning project setup.',
    long_description=open('README.md').read() if open('README.md', 'r') else '',
    long_description_content_type='text/markdown',
)
