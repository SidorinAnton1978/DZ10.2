from flask import Flask
from utils import *
app = Flask(__name__)


@app.route("/")
def page_main():
    candidates: list[dict] = load_candidates()
    all_candidates: str  = format_candidate(candidates)
    return all_candidates


@app.route("/candidates/<int:id>")
def page_id(id):
    candidate: dict = candidates_id(id)
    result: str = f'{candidates_picture(id)}\n{format_candidate([candidate])}'
    return result


@app.route("/skills/<skill>")
def page_skills(skill):
    candidates: list[dict] = candidates_skills(skill)
    all_candidates: str = format_candidate(candidates)
    return all_candidates


if __name__ == '__main__':
    app.run(debug=True)
