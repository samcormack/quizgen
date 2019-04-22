from flask import Flask, request, render_template
from quizgen import Quiz
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def quiz():
    if request.method == 'POST':
        quiz_cls = Quiz.get(request.form['quiztype'])
        quiz = quiz_cls(request.form)
        questions = quiz.generate()
        return render_template('output.html.j2', questions=questions, quiz=quiz)
    else:
        quiztype = request.args.get('type', 'add')
        quiz_cls = Quiz.get(quiztype)
        return render_template('quiz.html.j2', quiz=quiz_cls(), types=Quiz.types())
