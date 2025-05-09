import json
import itertools

filepath = 'data/intents.json'

with open(filepath) as f:
    data = json.load(f)

batches = itertools.batched(data['intents'], 5)

for i, batch in enumerate(batches):
    filename = f'data/intents_{i:02d}.json'
    subset = {'intents': batch}

    with open(filename, 'w') as f:
        json.dump(subset, f, indent=2)
