import os
import yaml

class Config(object):
    def __init__(self):
        if (os.environ.get('ENV') != 'prod'):  # We are not in Heroku
            """Setup Environment"""
            if os.path.exists(os.path.abspath(os.path.dirname(__file__)) + '/.env'):
                for line in open(os.path.abspath(os.path.dirname(__file__)) + '/.env'):
                    var = line.strip().split('=')
                    if len(var) == 2:
                        os.environ[var[0]] = var[1]
        
        """Initialize Configuration"""
        with open(os.path.abspath(os.path.dirname(__file__)) + '/config.yml') as stream:
            config = yaml.load(stream)
            self._github_user = config['github_user'][0]
            self._github_repos = config['github_repos']
            self._package_manager_urls = config['package_manager_urls']
            self._to_email = config['email']['to']
            self._from_email = config['email']['from']
            self._email_subject = config['email']['subject']
            self._email_body = config['email']['body']

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