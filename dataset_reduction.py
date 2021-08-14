import json
import random

data = []
with open(f'./Electronics_5.json') as f:
	for line in f:
		review = json.loads(line)
		data.append(review)

output = random.sample(data, 75000)
print(len(output))
with open(f'./Electronics_5_small.json', 'w') as f:
	for review in output:
		f.write(json.dumps(review)+'\n')