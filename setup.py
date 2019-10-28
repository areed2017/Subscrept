import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Subcrept',
    version='1.0',
    scripts=['subscrept.py'],
    author="Andrew Reed",
    author_email="AndrewReed2017@icloud.com",
    description="Math coding language",
    long_description=long_description,
    url="https://github.com/areed2017/Subscrept",
    packages=[
        'subscrept_pac.errors',
        'subscrept_pac.lexical',
        'subscrept_pac.syntax.calls',
        'subscrept_pac.syntax.keywords',
        'subscrept_pac.syntax.math',
        'subscrept_pac.syntax.objects',
        'subscrept_pac.syntax.types'
    ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )