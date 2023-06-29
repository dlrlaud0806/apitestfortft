import json
from collections import defaultdict

# Open the JSON file
with open('data.json') as file:
    datas = json.load(file)

mydict=defaultdict(int)
# Process the JSON data
# Access the contents using dictionary-like syntax
t_names=[]
i=1

with open('result1.txt', 'w') as file:
    
    for data in datas:
        file.write(str(i)+"\n")
        for t in sorted(data["traits"], key=lambda x:-x["style"]):
            if t["style"]>0:
                file.write(t["name"].ljust(20)+"\t"+str(t["style"])+"\n")
        characters = [t["character_id"] for t in sorted(data["units"], key=lambda x:x["rarity"])]

        file.writelines(', '.join(characters+["\n"]))
        print(characters)
        i+=1