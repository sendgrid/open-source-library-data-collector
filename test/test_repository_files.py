import os
import unittest


class TestRepositoryFiles(unittest.TestCase):

    def setUp(self):
        self.required_repo_files = [
            ['./Docker', './docker/Docker'],
            ['./docker-compose.yml', './docker/docker-compose.yml'],
            ['./.codeclimate.yml'],
            ['./.env_sample'],
            ['./.github/ISSUE_TEMPLATE'],
            ['./.github/PULL_REQUEST_TEMPLATE'],
            ['./.gitignore'],
            ['./.travis.yml'],
            ['./CHANGELOG.md'],
            ['./CODE_OF_CONDUCT.md'],
            ['./CONTRIBUTING.md'],
            ['./LICENSE.md'],
            ['./README.md'],
            ['./TROUBLESHOOTING.md'],
            ['./USAGE.md'],
            ['./USE_CASES.md'],
        ]

    def _file_exists(self, files):
        return len([fp for fp in files if os.path.isfile(fp)]) > 0

    def test_files_exists(self):
        for files in self.required_repo_files:
            self.assertTrue(self._file_exists(files))
