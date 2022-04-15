from setuptools import setup
from pysgi import __version__

setup(
    name='PySGI',
    version=__version__,
    description='The easy server library for everyone.',
    author='Jaedson Silva',
    author_email='imunknowuser@protonmail.com',
    packages=['pysgi'],
    install_requires=['http-parser'],
    license='MIT License',
    python_requires='>= 3.9'
)
