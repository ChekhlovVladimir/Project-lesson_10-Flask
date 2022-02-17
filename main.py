from flask import Flask
import functions

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = functions.candidate_matching()
    return "<pre>"+candidates+"</pre>"


@app.route("/candidate/<int:person_id>")
def page_id(person_id):
    candidate = functions.candidate_by_id(person_id)
    container = f"""
        <img src='https://picsum.photos/200'>
        <pre>
        {candidate['name']}
        {candidate['position']}
        {candidate['skills']}
        </pre>
        """

    return "<pre>" + container + "</pre>"


@app.route("/skills/<skill_list>")
def page_skills(skill_list):
    candidates = functions.candidates_by_skills(skill_list)
    skilled_candidates = functions.candidate_matching(candidates)
    return "<pre>" + skilled_candidates + "</pre>"


app.run()
