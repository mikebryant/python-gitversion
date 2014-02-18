"""A module to assist in getting the git version of a package."""
from __future__ import with_statement

import atexit
from subprocess import Popen, PIPE
import os
import re

class NoVersionError(Exception):
    """
    This is not a git repo, or it has not been tagged with a version.
    """

def determine_git_version(filename):
    """
    Take a filename (generally of a setup.py file),
    and return the git version.
    This should conform to semantic versioning standards.

    Example:
    setup(version=get_git_version(__file__))
    """

    # pylint doesn't understand Popen,
    # specifically the stderr and stdout accesses.
    # pylint: disable=E1101

    thisdir = os.path.abspath(os.path.dirname(filename))


    proc = Popen(
        ['git', 'describe', '--tags', '--match', '*.*'],
        stdout=PIPE,
        stderr=PIPE,
        cwd=thisdir
    )
    proc.stderr.close()
    bad_version = proc.stdout.read().decode('utf-8').strip()
    proc.stdout.close()

    if not bad_version:
        raise NoVersionError()

    match = re.match(
        '(?P<tag>.*)-(?P<commits>[0-9]+)-g(?P<hash>[0-9a-f]+)',
        bad_version
    )
    if match:
        version = "%(tag)s+git.%(commits)s.%(hash)s" % match.groupdict()
    else:
        version = bad_version

    return version

def _set_versionfile(versionfile, contents):
    """
    Set a version file to the given contents.
    """
    with open(versionfile, 'w') as fobj:
        fobj.write(contents)

def rewritable_git_version(filename):
    """
    Take a filename (which should resolve to a version.py file).
    Work out the git version, then rewrite that version.py file so it'll work correctly
    in a tarball version.

    At interpreter exit, fix this.

    Example usage:

    setup.py:
        from <package>.version import __VERSION__
        setup(version=__VERSION__, ...)

    <package>/version.py:
        from gitversion import rewritable_git_version
        __VERSION__ = rewritable_git_version(__file__)
    """

    versionfile = os.path.abspath(filename).rstrip('c')
    version = determine_git_version(filename)

    with open(versionfile, 'r') as fobj:
        versioncontents = fobj.read()

    with open(versionfile, 'w') as fobj:
        fobj.write("__VERSION__ = '%s'\n" % version)

    # At interpreter exit, reset the versionfile to its original contents.
    atexit.register(_set_versionfile, versionfile, versioncontents)

    return version
