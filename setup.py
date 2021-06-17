from setuptools import setup, find_packages

with open("requirements.txt", "r") as FH:
    REQUIREMENTS = FH.readlines()

NAME = 'infores_smartapi'
VERSION = '0.0.1'
URL = 'https://github.com/sierra-moxon/infores_smartapi'
AUTHOR = 'Sierra Moxon'
EMAIL = 'smoxon@lbl.gov'
REQUIRES_PYTHON = '>=3.7'
LICENSE = 'BSD'

setup(
    name=NAME,
    author=AUTHOR,
    version=VERSION,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    install_requires=[r for r in REQUIREMENTS if not r.startswith("#")],
    keywords='NCATS NCATS-Translator Biolink-Model',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3'
    ],
)
