import setuptools

with open("README.md","r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.0"
REPO_NAME = "TEXT-SUMMARIZER"
AUTHOR_USER_NAME = "aadi-ninja"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "aadithyakg04@gmail.com"

setuptools.setup(
    name=SRC_REPO,  # Replace with your own package name    
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP App",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },  
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),     
)