from textblob import TextBlob
import json


with open('language.json','r') as f:
    data = json.load(f)


text = 'I am satyam'
to_lang = "Hindi"
for key, value in data.items():
    if key == to_lang:
        blob=TextBlob(text)
        b = blob.translate(to=value)
        break
print(blob)
print(str(b))
