from setuptools import setup

setup(
    name='PySGI',
    version='1.0.0',
    description='The easy server library for everyone.',
    author='Jaedson Silva',
    author_email='imunknowuser@protonmail.com',
    packages=['pysgi'],
    install_requires=['http-parser'],
    license='MIT License',
    python_requires='>= 3.9',
    classifiers=[
        'Development Status :: Stable',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Web',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ]
)
