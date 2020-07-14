import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easysparql", # Replace with your own username
    version="1.0",
    author="Ahmad Alobaid",
    author_email="aalobaid@fi.upm.es",
    description="A python wrapper to easily query knowledge graphs with SPARQL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oeg-upm/easysparql",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)