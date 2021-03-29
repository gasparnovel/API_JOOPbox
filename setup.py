import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="API_JOOPbox",
    version="0.0.1",
    author="gasparnovel",
    author_email="gnovelcifpfbmoll.eu",
    description="API_Flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gasparnovel/API_JOOPbox/tree/develop",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'aniso8601==9.0.1',
        'atomicwrites==1.4.0',
        'attrs==20.3.0',
        'click==7.1.2',
        'colorama==0.4.4',
        'coverage==5.5',
        'Flask==1.1.2',
        'Flask-RESTful==0.3.8',
        'iniconfig==1.1.1',
        'itsdangerous==1.1.0',
        'Jinja2==2.11.3',
        'jsonschema==3.2.0',
        'MarkupSafe==1.1.1',
        'packaging==20.9',
        'pluggy==0.13.1',
        'py==1.10.0',
        'pyparsing==2.4.7',
        'pyrsistent==0.17.3',
        'pytest==6.2.2',
        'pytest-cov==2.11.1',
        'pytz==2021.1',
        'six==1.15.0',
        'toml==0.10.2',
        'Werkzeug==1.0.1',
    ],
)