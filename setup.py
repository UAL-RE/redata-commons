from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fr:
    requirements = fr.read().splitlines()

setup(
    name='redata',
    version='0.5.0',
    packages=find_namespace_packages(),
    url='https://github.com/UAL-RE/redata-commons/',
    project_urls={
        'Source': 'https://github.com/UAL-RE/redata-commons/',
        'Tracker': 'https://github.com/UAL-RE/redata-commons/issues',
    },
    license='MIT License',
    author='Yan Han',
    author_email='yhan818@gmail.com',
    description='Commons code used by ReDATA software',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.8',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
