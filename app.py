from flask import Flask
app = Flask(__name__)


@app.route("/")
def page_index(candidate_list_formated):
    return f'<pre>{candidate_list_formated}<pre>'


@app.route("/candidates/id")
def page_id(candidate_id):
    return f'<img src="(ссылка на картинку)">\n<pre>{candidate_id}<pre>'


@app.route("/skills/skill")
def page_skill(candidate_skill):
    return f'<pre>{candidate_skill}<pre>'


app.run()
