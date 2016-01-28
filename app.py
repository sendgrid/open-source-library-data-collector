from db_connector import DBConnector
from config import Config
from github import GitHub
from package_managers import PackageManagers
from sendgrid_email import SendGrid

config = Config()
db = DBConnector()
github = GitHub() 
pm = PackageManagers()
sg = SendGrid()

# Update the DB with the GitHub repo data
for repo in config.github_repos:
    github.update_library_data(config.github_user, repo)
    
# Update the DB with Package Manager data
pm.update_package_manager_data(config.package_manager_urls)

# Send an email update
sg.send_email(config.to_email, config.from_email, config.email_subject, config.email_body)