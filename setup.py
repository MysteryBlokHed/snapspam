import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='snapspam',
    version='0.1.0',
    author='Adam Thompson-Sharpe',
    author_email='adamthompsonsharpe@gmail.com',
    description=
    'A CLI + library to spam multiple common anonymous message apps for Snapchat.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MysteryBlokHed/snapspam',
    packages=setuptools.find_packages(),
    install_requires=[
        'requests~=2.25',
    ],
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='~=3.6')