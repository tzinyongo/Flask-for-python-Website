from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


RAPIDAPI_KEY = "c31808e9camsh88eaebb5c2c6f84p158cf2jsne30fc5cd6235"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/secondpage')
def second_page():
    return render_template('secondpage.html')

@app.route('/thirdpage', methods = ['GET','POST'])
def third_page():
    if request.method == 'POST':
        query = request.form['query']
        url = "https://yahoo-finance127.p.rapidapi.com/search/"+query
        headers = {
            "X-RapidAPI-Key": "a7794b9a36mshed157cdb4537f8ap1b3af5jsn3878cc4f1a3c",
            "X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            results = data.get('quotes', [])
            print(results)
            return jsonify(results)
        else:
            return jsonify([])

    return render_template('thirdpage.html')
    #return render_template('thirdpage.html')



if __name__ == '__main__':
    app.run()