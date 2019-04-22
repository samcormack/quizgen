from flask import Flask, request, render_template
import quizgen
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def quiz():
    if request.method == 'POST':
        questions = quizgen.generator(
            int(request.form['max1']),
            int(request.form['max2']),
            int(request.form['maxsum']),
            int(request.form['n_questions'])
        )
        return render_template('output.html.j2', questions=questions, params=request.form)
    else:
        return render_template('quiz.html.j2')
