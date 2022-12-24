import json

class klass:
    def __init__(self, name, id, worksheet):
        self.name = name
        self.id_ = id
        self.worksheet = worksheet

    def klass_to_dict(self):
        dct = dict()
        dct['name'] = self.name
        dct['id'] = self.id_
        dct['worksheet'] = self.worksheet
        return dct

CLASS_ID = []

def find_klass(name):
    for klass in range(len(CLASS_ID)):
        if CLASS_ID[klass].name == name:
            return klass

def get_names():
    return [klass.name for klass in CLASS_ID]

def print_klasses():
    for klass in CLASS_ID:
        print(f'{klass.name}: {klass.id_, klass.worksheet}', end=', ')

def read_db():
    with open('db.json') as f:
        data = json.load(f)
        print(json.dumps(data, indent=4))
        for klass_ in data['klasses']:
            CLASS_ID.append(klass(
                klass_['name'],
                klass_['id'],
                klass_['worksheet']
            ))

def save_db():
    dct = dict()
    dct['klasses'] = []
    for i in CLASS_ID:
        dct['klasses'].append(i.klass_to_dict())
    with open('db.json', 'w') as f:
        f.write(json.dumps(dct, indent=4))