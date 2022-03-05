from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='testjpkg',
    version='1.2.11rc1',
    packages=find_packages(),
    setup_requires=['setuptools_scm'],
    include_package_data=True,
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.py", "*.png", "*.bak"],
    },
    description="Save contacts from your terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thisisishara/test_pypi_cli",
    author="Ishara Dissanayake",
    author_email="thisismaduishara@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=[
        # 'rasa==2.8.8',
    ],
    entry_points={'console_scripts': ['testj = jsonify.cli:main']}
)
