'''Setup file for gitversion.'''
from setuptools import setup
from gitversion.version import __VERSION__

setup(
    name='gitversion',
    version=__VERSION__,
    packages=['gitversion'],
    description='Utility to get the git version of a package.',
    author='Mike Bryant',
    author_email='mike@mikebryant.me.uk',
    include_package_data=True,
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Version Control',
    ],
)
