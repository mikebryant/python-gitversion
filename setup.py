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
)
