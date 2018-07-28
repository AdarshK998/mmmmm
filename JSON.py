import json

with open("foodyo_output.json") as json_file:
	data = json.load(json_file)

for x in data['body']['Recommendations']:
	print x['RestaurantName']
	for item in x['menu']:
		if (item['type'] == "sectionheader"):
			for child in item['children']:
				if (child['type'] == "item") and (child['selected'] == 1):
					print "-->" + child['name']
					for children in child['children']:
						if children['selected'] == 1:
							print "------>" + children['name']
							for children1 in children['children']:
								print "--------->" + children1['name']
