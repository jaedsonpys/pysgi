from setuptools import setup
from pysgi import __version__

with open('DESCRIPTION.md', 'r') as reader:
    description = reader.read()

setup(
    name='PySGI',
    version=__version__,
    description='The easy server library for everyone.',
    long_description=description,
    long_description_content_type='text/markdown',
    author='Jaedson Silva',
    author_email='imunknowuser@protonmail.com',
    packages=['pysgi'],
    install_requires=['http-parser'],
    license='MIT License',
    python_requires='>= 3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ],
    project_urls={
        'Source code': 'https://github.com/jaedsonpys/pysgi',
        'License': 'https://github.com/jaedsonpys/pysgi/blob/master/LICENSE'
    },
    keywords=['server', 'http', 'internet', 'www', 'framework']
)
