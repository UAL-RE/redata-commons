from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='redata',
    version='0.1.0',
    packages=find_namespace_packages(),
    url='https://github.com/UAL-ODIS/redata_commons/',
    project_urls={
        'Source': 'https://github.com/UAL-ODIS/redata_commons/',
        'Tracker': 'https://github.com/UAL-ODIS/redata_commons/issues',
    },
    license='MIT License',
    author='Chun Ly',
    author_email='astro.chun@gmail.com',
    description='Commons code used by ReDATA software',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
