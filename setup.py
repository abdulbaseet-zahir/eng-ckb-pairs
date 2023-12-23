from setuptools import setup, find_packages

setup(
    name="eng_ckb",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pandas"],
    license="Unlicense",
    description="A package for collecting and translating English sentences to Central Kurdish.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Abdulbasit Zahir",
        "License :: Public Domain",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing :: Translation",
    ],
)
