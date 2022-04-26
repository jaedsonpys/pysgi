from setuptools import setup

setup(
    name='PySGI',
    version='1.2.0',
    description='The easy server library for everyone.',
    author='Jaedson Silva',
    author_email='imunknowuser@protonmail.com',
    packages=['pysgi'],
    install_requires=['http-parser'],
    license='MIT License',
    python_requires='>= 3.9',
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
    }
)
