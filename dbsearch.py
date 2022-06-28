from tqdm import tqdm

def search(text, db):
    results = []
    for entity in tqdm(db):
        if entity in text:
            idx = text.find(entity)
            while idx != -1:
                results.append((entity, db[entity], idx))
                idx = text[idx+1:].find(entity)
    
    return results