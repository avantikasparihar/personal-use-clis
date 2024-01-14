from setuptools import setup, find_packages

setup(
    name="utility-clis",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'click==8.0.3',
        'PyYAML==6.0.1'
    ],
    entry_points={
        'console_scripts': [
            'hello-cli=src.hello_cli.cli:hello',
            'read-100pages-a-day-cli=src.reading_cli.cli:reading_cli'
        ],
    },
)