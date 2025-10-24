import json

data = {"name": "Saklain", "age": 23, "skills": ["python", "java"]}
text = "Hi I'm Saklain Vempalli Shaik"

# write (create/overwrite) JSON file (utf-8 & pretty)
with open("data.txt", "w", encoding="utf-8") as f:
    json.dump(text, f, ensure_ascii=False, indent=2)

# read JSON back into Python object (dict/list)
with open("data.json", "r", encoding="utf-8") as f:
    obj = json.load(f)
print(obj["name"])  # Saklain
