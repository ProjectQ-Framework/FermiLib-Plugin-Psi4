import os

from setuptools import setup, find_packages

# This reads the __version__ variable from projectq/_version.py
exec(open('fermilibpluginpsi4/_version.py').read())
# Readme file as long_description:
long_description = open('README.rst').read()
# Read in requirements.txt
requirements = open('requirements.txt').readlines()
requirements = [r.strip() for r in requirements]


setup(
    name='fermilibpluginpsi4',
    version=__version__,
    author='FermiLib plugin Psi4 developers',
    author_email='fermilib@projectq.ch',
    url='http://www.projectq.ch',
    description='A plugin allowing FermiLib to interface with Psi4.',
    long_description=long_description,
    install_requires=requirements,
    license='GNU Lesser General Public License (LGPL), Version 3 or any later'
            ' version',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': [os.path.join('fermilibpluginpsi4', '_psi4_template')]
    }
)
