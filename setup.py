import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='Discrept',
    version='1.1',
    scripts=['subscrept.py'],
    author="Andrew Reed",
    author_email="AndrewReed2017@icloud.com",
    description="A Language that Generates PDF / Math coding language",
    long_description=long_description,
    url="https://github.com/areed2017/Subscrept",
    packages=[
        'Errors',
        'lexical',
        'syntax.calls',
        'syntax.keywords',
        'syntax.math',
        'syntax.objects',
        'syntax.types'
    ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )