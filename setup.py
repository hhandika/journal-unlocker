from setuptools import setup, find_packages

setup(
    name='journal-unlocker',
    version='0.0.1',
    author= "Heru Handika",
    author_email = "hhandika.us@gmail.com",
    include_package_data=True,
    py_modules=find_packages(),
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        ju=ju.ju:main
    ''',
)