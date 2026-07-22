from setuptools import setup, find_packages

setup(
    name='micql',
    version='1.0.0',
    description='Micql — минималистичный язык запросов',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='rostichar1-hue',
    url='https://github.com/rostichar1-hue/Micql',
    packages=find_packages(),
    install_requires=['tabulate'],
    entry_points={
        'console_scripts': [
            'micro=micql.cli:main',
        ],
    },
    python_requires='>=3.6',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
