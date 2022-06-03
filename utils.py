import json
from app import *


def load_json(filename):
    with open(filename) as f:
        return json.load(f)


def load_candidates():
    """ Загружает кандидатов из файла candidates.json в список """
    return load_json('candidates.json')


