from setuptools import setup

with open('DESCRIPTION.md', 'r') as reader:
    description = reader.read()

setup(
    name='PySGI',
    version='1.3.1',
    description='The easy server library for everyone.',
    long_description=description,
    long_description_content_type='text/markdown',
    author='Jaedson Silva',
    author_email='imunknowuser@protonmail.com',
    packages=['pysgi', 'pysgi/utils'],
    install_requires=['http-pyparser==0.3.2'],
    license='MIT License',
    python_requires='>= 3.6',
    url='https://github.com/jaedsonpys/pysgi',
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
        'License': 'https://github.com/jaedsonpys/pysgi/blob/master/LICENSE'
    },
    keywords=['server', 'http', 'internet', 'www', 'framework']
)
