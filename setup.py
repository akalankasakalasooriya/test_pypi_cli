from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='testjpkg',
    version=1.1,
    packages=['jsonify', 'jsonify.initial_project'],
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
    ],
    entry_points={'console_scripts': ['testj = jsonify.cli:main']}
)
