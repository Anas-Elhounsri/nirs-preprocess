from setuptools import setup, find_packages

setup(
    name="nirs-preprocess",
    version="1.4.0",
    description="Preprocessing pipelines for near-infrared spectral data",
    author="Anas El Hounsri",
    author_email="elhounsri.anas@gmail.com",
    packages=find_packages(),
    install_requires=["numpy>=1.24", "scipy>=1.10"],
    python_requires=">=3.9",
)
