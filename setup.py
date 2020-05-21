import setuptools

setuptools.setup(
    name='economicapi',
    version='0.1',
    scripts=['api'],
    author="Tobias Dybdahl",
    author_email="tobiasdybdahl@gmail.com",
    description="A api for creating e-conomic orders",
    long_description="Some long description",
    long_description_content_type="text/markdown",
    url="https://github.com/tdybda17/economicapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
