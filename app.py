from flask import Flask, render_template, request
from  flask_debugtoolbar import DebugToolbarExtension
from stories import story



app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'
debug = DebugToolbarExtension(app)



@app.route('/')
def questions():
    prompts = story.prompts
    return render_template('questions.html', prompts=prompts)

@app.route("/story", methods=['GET', 'POST'])
def show_story():
    if request.method == 'POST':
        answers = {prompt: request.form[prompt] for prompt in story.prompts}
        text = story.generate(answers)
        print("Generated Story:", text)  # Add this line for debugging
        return render_template("story.html", text=text)
    return render_template("story.html", text='')
