import json

number_of_batches = 12

data = {"intents": []}

for i in range(number_of_batches):
    filename = f'data/intents_{i:02d}_expanded.json'

    with open(filename, encoding='utf-8') as f:
        d = json.load(f)

        data["intents"].extend(d["intents"])

with open('data/intents_expanded.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)
