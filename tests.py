'''Tests for gitversion.'''
# pylint: disable=C0103
# pylint: disable=R0904

import contextlib
import gitversion
import os
import shutil
import tempfile
import unittest

import logging
LOGGER = logging.getLogger(__name__)

class GitVersionCase(unittest.TestCase):
    '''Test the correct versions are detected (and written, if applicable).'''

    versionstrings = {
        'normal': '3.0.34',
        'extracommit': '3.0.34+git.1.1bd773a',
    }

    def setUp(self):

        self.tempdir = tempfile.mkdtemp()
        LOGGER.debug("Created temporary directory %r", self.tempdir)
        self.testdir = os.path.join(self.tempdir, 'repo')
        self.gitdir = os.path.join(self.testdir, '.git')
        self.versionfilepath = os.path.join(self.testdir, 'version.py')

    def tearDown(self):

        LOGGER.debug('Removing %r', self.tempdir)
        shutil.rmtree(self.tempdir)

    @contextlib.contextmanager
    def create_gitdir(self, name='normal'):
        '''Creates a populated git directory.'''

        test_data = os.path.join(os.path.dirname(__file__), 'test_data', name)
        shutil.copytree(test_data, self.testdir)
        shutil.move(os.path.join(self.testdir, 'dot.git'), self.gitdir)
        yield
        shutil.rmtree(self.testdir)

    def test_git_describe(self):
        '''
        Tests that the version is determined correctly.
        '''

        for repo_name, correctversion in self.versionstrings.items():
            with self.create_gitdir(repo_name):
                self.assertEqual(
                    gitversion.determine_git_version(self.versionfilepath),
                    correctversion,
                )
