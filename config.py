import os
import yaml


class Config(object):
    """All configuration for this app is loaded here"""
    def __init__(self):
        if (os.environ.get('ENV') != 'prod'):  # We are not in Heroku
            self.init_environment()

        """Allow variables assigned in config.yml available the following
           variables via properties"""
        self.base_path = os.path.abspath(os.path.dirname(__file__))
        with open(self.base_path + '/config.yml') as stream:
            config = yaml.load(stream)
            self._github_user = config['github_user'][0]
            self._github_repos = config['github_repos']
            self._package_manager_urls = config['package_manager_urls']
            self._to_email = config['email']['to']
            self._from_email = config['email']['from']
            self._email_subject = config['email']['subject']
            self._email_body = config['email']['body']
            self._export_github = config['export_tables']['Github']
            self._export_package_managers = \
                config['export_tables']['PackageManagers']

    @staticmethod
    def init_environment():
        """Allow variables assigned in .env available using
           os.environ.get('VAR_NAME')"""
        base_path = os.path.abspath(os.path.dirname(__file__))
        if os.path.exists(base_path + '/.env'):
            for line in open(base_path + '/.env'):
                var = line.strip().split('=')
                if len(var) == 2:
                    os.environ[var[0]] = var[1]

    @property
    def github_user(self):
        return self._github_user

    @property
    def github_repos(self):
        return self._github_repos

    @property
    def package_manager_urls(self):
        return self._package_manager_urls

    @property
    def to_email(self):
        return self._to_email

    @property
    def from_email(self):
        return self._from_email

    @property
    def email_subject(self):
        return self._email_subject

    @property
    def email_body(self):
        return self._email_body

    @property
    def export_github(self):
        return self._export_github

    @property
    def export_package_managers(self):
        return self._export_package_managers
