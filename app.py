from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.auto_reload = True  # This enables auto-reloading of templates during development.
app.config['TEMPLATES_AUTO_RELOAD'] = True
# Your view functions and other configurations go here.

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/secondpage')
def second_page():
    return render_template('secondpage.html')

if __name__ == '__main__':
    app.run()