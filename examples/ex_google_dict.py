from core.english_modules import Google_Dictionary

model = Google_Dictionary()

results = model.get('took')
print(results)