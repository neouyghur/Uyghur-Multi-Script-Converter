from setuptools import setup, find_packages

setup(
    name='umsc',
    version='0.4.0',
    author='Osman Tursun',
    author_email='osmanjan.t@gmail.com',
    maintainer='Osman Tursun',
    maintainer_email='mpcabd@gmail.com',
    description='Script Converter for Uyghur Language',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='uyghur script converter arabic latin cyrillic IPA ئۇيغۇر',
    url='https://github.com/neouyghur/ScriptConverter4Uyghur',
    packages=find_packages(),
    install_requires=[
        "regex"
    ],
    classifiers=[
        # Trove classifiers to categorize the package (https://pypi.org/classifiers/)
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.0',  # Minimum version requirement of the package
)
