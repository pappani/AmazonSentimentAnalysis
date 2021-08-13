import json
import random

data = []
file_name = 'Electronics_5'
with open(f'./{file_name}.json') as f:
	for line in f:
		review = json.loads(line)
		data.append(review)

final_data = random.sample(data, 75000)

print(len(final_data))

with open(f'./{file_name}_small.json', 'w') as f:
	for review in final_data:
		f.write(json.dumps(review)+'\n')