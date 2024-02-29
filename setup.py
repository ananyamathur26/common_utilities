from setuptools import setup, find_packages

setup(
    name='common_utilities',
    version='0.0.1',
    description='My private package from private github repo',
    url='git@github.com:ananyamathur26/common_utilities.git',
    author='Ananya Mathur',
    author_email='ananyamathur26@gmail.com',
    license='unlicense',
    packages=find_packages(),
    zip_safe=False
)

