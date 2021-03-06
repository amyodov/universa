import setuptools


CLASSIFIERS = [
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Intended Audience :: Developers',
]


with open('README.md', 'r') as fh:
    long_description = fh.read()


EXTRAS_REQUIRE = {
    'dev': [
        'pytest',
    ]
}


setuptools.setup(
    name='universa',
    version='0.0.7',
    author='Vadim Kovrigin',
    author_email='kovrigin.dev@gmail.com',
    description='Python package to access Universa API from python.',
    include_package_data=True,
    install_requires=[
        "pexpect>=4.0.0",
    ],
    extras_require=EXTRAS_REQUIRE,
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['Universa'],
    url='https://github.com/vkovrigin/universa',
    packages=setuptools.find_packages(),
    classifiers=CLASSIFIERS,
)
