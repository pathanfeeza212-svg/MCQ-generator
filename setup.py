from setuptools import setup, find_packages

setup(
    name="mcq_generator",
    version="0.1",
    author="Feezan Khan",
    author_email="pathanfeeza212@gmail.com",
    packages=find_packages(),
    install_requires=[
        "openai",
        "langchain",
        "streamlit",
        "python-dotenv",
        "PyPDF2"
    ]
)