from setuptools import setup

setup(
    name="StrictSignal",
    version="0.1.0",
    install_requires=[
        "PySide6",
        "executing",
    ],
    author="Louie Atkins-Turkish",
    author_email="louie.atk@gmail.com",
    description="A module that provides type checking for PySide6.QtCore.Signal",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Loubrains/StrictSignal",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
