from setuptools import setup, find_packages

setup(
    name='ghostpip',
    version='1.0.3',
    author='Mohammad Alamin',
    author_email='akxvau@gmail.com',
    description='A Python module for interacting with the ghost.toxinum.xyz API',
    url='https://github.com/illusionghost3/ghostpip',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
