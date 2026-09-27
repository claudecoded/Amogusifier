from setuptools import setup, find_packages

setup(
    name="amogusifier",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python tool to transform photos into an Among Us character mosaic",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pillow>=10.0.0",
        "numpy>=1.20.0",
    ],
    entry_points={
        "console_scripts": [
            "amogusify=main:main",
        ],
    },
)
