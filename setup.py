from setuptools import setup, find_packages
from pdf_qa_ai import __version__

setup(
    name="",
    packages=find_packages(exclude=["tests"]),
    setup_requires=["setuptools", "wheel"],
    version=__version__,
    description="PDF Q&A AI",
    author="",
)