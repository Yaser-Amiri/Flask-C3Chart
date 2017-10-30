import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='Flask-C3Chart',
    version='0.1',
    include_package_data=True,
    license='BSD License',
    description='A simple Flask extension to generate charts with C3 javascript library.',
    long_description=README,
    url='',
    author='Yaser Amiri',
    author_email='yaser.amiri95@gmail.com',
    py_modules=['flask_c3chart'],
    #packages=['flask_c3chart'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
