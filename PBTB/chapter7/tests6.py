import json

with open('backup_config.json') as fh:
	conf = json.load(fh)

conf['newkey'] = 5.0005

with open('backup_config.json', 'w') as fh:
	json.dump(conf, fh, indent=4, separators=(',', ': '))
