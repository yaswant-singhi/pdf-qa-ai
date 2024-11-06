from setuptools import setup, find_packages
from pdf_qa_ai import __version__


PACKAGE_REQUIREMENTS = [
    "pdfplumber",
    "groq",
    "streamlit",
]

DEV_REQUIREMENTS = [
    "black"
]

setup(
    name="",
    packages=find_packages(exclude=["tests"]),
    setup_requires=["setuptools", "wheel"],
    install_requires = PACKAGE_REQUIREMENTS,
    extras_require={
        "dev": DEV_REQUIREMENTS,
    },
    version=__version__,
    description="PDF Q&A AI",
    author="",
)