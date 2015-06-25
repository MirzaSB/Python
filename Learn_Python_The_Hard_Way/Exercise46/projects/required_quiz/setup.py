try:
	from setuptools import setup
	from bin import testbin
except:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'My Name',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'My email.',
	'version': '0.1',
	'install_requires': ['nose', 'requests'],
	'packages': ['NAME'],
	'scripts': ['bin/testbin.py'],
	'name': 'projectname'
	}

setup(**config)
