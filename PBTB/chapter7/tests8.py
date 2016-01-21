import yaml

myobj = (
	[1,2,3,4,5],
	{'a': 1, 'b': 2, 'c': 3},
	[	
		{'x': 98, 'y': 99, 'z': 100},
		3,
		4
	],
	{'a': [1,2,3], 'b': [4,5,6], 'c': [7.8,9]}
)

print yaml.dump(myobj, default_flow_style=False)
