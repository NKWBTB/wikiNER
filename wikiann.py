from datasets import load_dataset
import json
from tqdm import tqdm
import dbsearch as DB

def save_db():
    dataset = load_dataset("wikiann", "en")
    
    db = {}

    for sample in tqdm(dataset["train"]):
        for span in sample["spans"]:
            idx = span.find(":")
            etype = span[:idx].strip()
            entity = span[idx+1:].strip()
            db[entity] = etype
    
    with open("db.json", "w", encoding="UTF-8") as f:
        json.dump(db, f, indent=2)

if __name__ == '__main__':
    # save_db()
    
    with open("db.json", "r", encoding="UTF-8") as f:
        db = json.load(f)
    
    text = 'BBC company'
    results = DB.search(text, db)
    
    print(text)
    print(results)