from setuptools import setup, find_packages

setup(
    name='vibration-analysis',  # Note the hyphen
    version='0.1.0',
    author='Asim Basak',
    author_email='your.email@example.com',
    description='A brief description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/asimbasak/vibration_analysis',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
