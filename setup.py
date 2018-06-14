import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='abna',
    version='0.1.1',
    author='Dirkjan Ochtman',
    author_email='dirkjan@ochtman.nl',
    description='Automated retrieval of mutations from ABN Amro',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/djc/abna',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=['cryptography', 'requests'],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
