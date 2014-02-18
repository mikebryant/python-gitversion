=================
python-gitversion
=================

.. image:: https://travis-ci.org/mikebryant/python-gitversion.png?branch=master
    :target: https://travis-ci.org/mikebryant/python-gitversion
    :alt: Build Status Badge
.. image:: https://coveralls.io/repos/mikebryant/python-gitversion/badge.png?branch=master
    :target: https://coveralls.io/r/mikebryant/python-gitversion?branch=master
    :alt: Coverage Status Badge
.. image:: https://landscape.io/github/mikebryant/python-gitversion/master/landscape.png
   :target: https://landscape.io/github/mikebryant/python-gitversion/master
   :alt: Code Health Badge
.. image:: https://pypip.in/v/gitversion/badge.png
    :target: https://pypi.python.org/pypi/gitversion/
    :alt: Version Badge
.. image:: https://pypip.in/d/gitversion/badge.png
    :target: https://pypi.python.org/pypi/gitversion/
    :alt: Downloads Badge
.. image:: https://pypip.in/wheel/gitversion/badge.png
    :target: https://pypi.python.org/pypi/gitversion/
    :alt: Wheel Status Badge
.. image:: https://pypip.in/license/gitversion/badge.png
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