from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)
app.jinja_env.auto_reload = True  # This enables auto-reloading of templates during development.
app.config['TEMPLATES_AUTO_RELOAD'] = True
# Your view functions and other configurations go here.

RAPIDAPI_KEY = "c31808e9camsh88eaebb5c2c6f84p158cf2jsne30fc5cd6235"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/secondpage')
def second_page():
    return render_template('secondpage.html')

@app.route('/thirdpage')
def third_page():
    return render_template('thirdpage.html')

@app.route('/thirdpage', methods=['POST'])
def search():
    query = request.form['query']

    headers = {
        'X-RAPIDAPI-KEY': RAPIDAPI_KEY
    }

    api_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        results = data['results']
        return jsonify(results)
    else:
        return jsonify([])

    #return render_template('thirdpage.html')



if __name__ == '__main__':
    app.run()