CREATE TABLE `github_data` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `date_updated` datetime DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `pull_requests` int(11) unsigned DEFAULT NULL,
  `open_issues` int(11) unsigned DEFAULT NULL,
  `number_of_commits` int(11) unsigned DEFAULT NULL,
  `number_of_branches` int(11) unsigned DEFAULT NULL,
  `number_of_releases` int(11) unsigned DEFAULT NULL,
  `number_of_contributors` int(11) unsigned DEFAULT NULL,
  `number_of_watchers` int(11) unsigned DEFAULT NULL,
  `number_of_stargazers` int(11) unsigned DEFAULT NULL,
  `number_of_forks` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE `package_manager_data` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `date_updated` datetime DEFAULT NULL,
  `csharp_downloads` int(11) unsigned DEFAULT NULL,
  `nodejs_downloads` int(11) unsigned DEFAULT NULL,
  `php_downloads` int(11) unsigned DEFAULT NULL,
  `python_downloads` int(11) unsigned DEFAULT NULL,
  `ruby_downloads` int(11) unsigned DEFAULT NULL,
  `java_downloads` int(11) unsigned DEFAULT NULL,
  `python_http_client_downloads` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;