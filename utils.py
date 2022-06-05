import json


def load_json(filename, encoding='utf-8'):
    """ Чтение данных из файла"""
    with open(filename, 'r',  encoding=encoding) as f:
        return json.load(f)


def load_candidates() -> list[dict]:
    """ Загружает кандидатов из файла candidates.json в список """
    candidates = load_json('candidates.json')
    return candidates


def format_candidate(candidates: list[dict]) -> str:
    """ Преобразует список кандидатов"""
    result = '<pre>'
    for candidate in candidates:
        result += f"""
            {candidate["name"]}\n
            {candidate["position"]}\n
            {candidate["skills"]}\n\n
        """
    result += '</pre>'
    return result


def candidates_id(id: int) -> dict:
    """ Поиск кандидатов по id"""
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['id'] == id:
            return candidate


def candidates_picture(id: int) -> str:
    """ Поиск картинки(фото) кандидата"""
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['id'] == id:
            picture = f'<img src="{candidate["picture"]}">'
            return picture


def candidates_skills(skill: str) -> list[dict]:
    """ Поиск по навыкам кандидата"""
    candidates = load_candidates()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result
