import glob
import json
import os

head = []
dropped = ["wayne", "ysl", "kebab"]

os.system("rm -f builds/website_api.json brokenjson.txt")

for x in glob.glob("builds/*.json"):
    with open(x, 'rb') as file:
        try:
            data = json.load(file)
            for item in data:
                item['url'] = "https://www.pling.com/p/1544683"
                for d in dropped:
                    if d in item["filename"]:
                        item["version"] = item["version"] + ", Dropped"
            head += data
        except Exception as e:
            print(f'{x}: {e}\n')
            with open('brokenjson.txt', 'a') as file:
                file.write(f'- {x}: {e}\n')

if os.path.isfile("brokenjson.txt"):
    exit(1)

with open("builds/website_api.json", 'w') as outfile:
    json.dump(head, outfile, ensure_ascii=False)
