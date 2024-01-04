from setuptools import setup, find_packages

setup(
    name="personal-use-clis",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'click==8.0.3',
    ],
    entry_points={
        'console_scripts': [
            'hello-cli=src.hello_cli:hello',
            'reading-cli=src.reading_cli:hello'
        ],
    },
)