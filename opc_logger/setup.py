from setuptools import setup, find_packages

setup(
    name="opc_logger",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "customtkinter",
        "opcua-client",
        "pandas",
        "numpy",
        "cryptography",
    ],
)
