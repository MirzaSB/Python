import json

with open('backup_config.json') as fh:
	conf = json.load(fh)

print conf
print type(conf)
