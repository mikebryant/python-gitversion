=================
python-gitversion
=================

.. image:: https://img.shields.io/travis/mikebryant/python-gitversion/master.png
    :target: https://travis-ci.org/mikebryant/python-gitversion
    :alt: Build Status Badge
.. image:: https://img.shields.io/coveralls/mikebryant/python-gitversion/master.png
    :target: https://coveralls.io/r/mikebryant/python-gitversion?branch=master
    :alt: Coverage Status Badge
.. image:: https://landscape.io/github/mikebryant/python-gitversion/master/landscape.png
   :target: https://landscape.io/github/mikebryant/python-gitversion/master
   :alt: Code Health Badge
.. image:: https://img.shields.io/pypi/v/gitversion.png
    :target: https://pypi.python.org/pypi/gitversion/
    :alt: Version Badge
.. image:: https://img.shields.io/pypi/dm/gitversion.png
    :target: https://pypi.python.org/pypi/gitversion/
    :alt: Downloads Badge
.. image:: https://img.shields.io/badge/license-GPLv3+-blue.png
    :target: https://pypi.python.org/pypi/gitversion/
    :alt: License Badge

This package lets you use git tags to version python projects.

Usage
=====
``setup.py``:

.. code-block:: python

    from <package>.version import __VERSION__
    setup(version=__VERSION__, ...)

``<package>/version.py``:

.. code-block:: python

    from gitversion import rewritable_git_version
    __VERSION__ = rewritable_git_version(__file__)
