import yaml
import json

with open('app.yaml') as fh:
	struct = yaml.load(fh)

print json.dumps(struct, indent=4, separators=(',', ':'))
