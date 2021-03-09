from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='redata_commons',
    version='0.0.1',
    packages=['redata_commons'],
    url='https://github.com/UAL-ODIS/redata_commons/',
    license='MIT License',
    author='Chun Ly',
    author_email='astro.chun@gmail.com',
    description='Commons code used by ReDATA software',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
