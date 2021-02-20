# setup.py
from setuptools import setup, find_packages

author_name = 'Armando Barbosa Sobrinho'
author_email = 'armandobs14@gmail.com'

setup(
    name='tagger',
    version='0.0.1',
    description='Song Tagger',
    long_description='Tool for rename unknoing songs',
    author=author_name,
    author_email=author_email,
    maintainer=author_name,
    maintainer_email=author_email,
    license='MIT',
    keywords='tagger',
    packages=find_packages(exclude=['tests*']),
    install_requires=['ShazamAPI'],
    entry_points={'console_scripts': ['tagger = tagger:main']},
    platforms='windows linux',
)