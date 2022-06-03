import json
from app import *


class Candidates:
    def __init__(self):
        pass

    def load_json(self, filename, encoding='utf-8'):
        with open(filename) as f:
            return json.load(f)

    def load_candidates(self):
        """ Загружает кандидатов из файла candidates.json в список """
        return load_json('candidates.json')
