from flask import Flask, request, render_template
from sprn.view import SRPN_view

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    view = SRPN_view()
    text = request.form['text']
    processed_text = text.upper()
    return 

if __name__ == "__main__":
    app.run()
