import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="economicapi-tdybda", # Replace with your own username
    version="0.0.1",
    author="tdybda17",
    author_email="tdybda17@student.aau.dk",
    description="E-conomic order api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tdybda17/economicapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
