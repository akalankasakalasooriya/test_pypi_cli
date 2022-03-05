# [test_pypi_cli]
A test python package with a simple CLI script that can read and jsonify raw text mainly aimed to test pypi releases.

## How to test the cli tool
Install the tool using:
```shell
pip install -i https://test.pypi.org/simple/ testjpkg==1.2.1
```

Running the CLI tool  
1. To crete a dir structure automatically and get the jsonified string from the text file included in the init dir. This will create a dir named "test" and a text file named "testfile.txt".
```python
testj --file test/testfile.txt --init init
```

2. Jsonify your own text file. (loose the --init argument)
```python
testj --file /path/to/your/textfile.txt
```

Package Link: https://test.pypi.org/project/testjpkg/1.2.1/

References:
[1]. https://dev.to/wangonya/publishing-your-python-packages-on-testpypi-before-publishing-on-pypi-2gb2
[2]. https://stackoverflow.com/questions/1612733/including-non-python-files-with-setup-py
```python
setup_requires=['setuptools_scm'],
include_package_data=True,
```

## Steps to re-produce a similar package
- create the package
- create the setup.py
- install it locally using:  pip install --editable . [locally install only]
- build using wheel: python setup.py sdist bdist_wheel
- pip install twine
- upload using twine: twine upload --repository-url https://test.pypi.org/legacy/ dist/* [for test pypi]
- upload using twine: twine upload dist/* [for pypi]
- push it to test pypi
- install and test