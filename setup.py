import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='shift-register',  
    version='0.1',
    scripts=['shiftRegister'] ,
    author="nated0g",
    author_email="n.usher87@gmail.com",
    description="SN74HC164 shift register library for Raspberry Pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nated0g/shift-register",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
)
