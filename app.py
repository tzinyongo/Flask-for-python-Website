from flask import Flask, render_template, request, jsonify, json
import requests, urllib.request 
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

mock_stock_data = [
    {'exchange': 'NMS', 'shortname': 'Apple Inc.', 'industry': 'Technology'},
    {'exchange': 'NYQ', 'shortname': 'Microsoft Corp.', 'industry': 'Technology'}
    # Add more mock data as needed
]

RAPIDAPI_KEY = "c31808e9camsh88eaebb5c2c6f84p158cf2jsne30fc5cd6235"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/secondpage')
def second_page():
    return render_template('secondpage.html')

@app.route('/thirdpage', methods=['GET','POST'])
def third_page():
    if request.method == 'POST':
        query = request.form['query']
        api_url = "https://yahoo-finance127.p.rapidapi.com/search/"+query

        headers = {
        "X-RapidAPI-Key": "a7794b9a36mshed157cdb4537f8ap1b3af5jsn3878cc4f1a3c",

        "X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
        }

        response = requests.get(api_url, headers=headers)
  
        data = response.json()
        stock_data = data.get('quotes',[])
        #stock_data = [{'exchange': 'NMS', 'shortname': 'Apple Inc.', 'quoteType': 'EQUITY', 'symbol': 'AAPL', 'index': 'quotes', 'score': 454300, 'typeDisp': 'Equity', 'longname': 'Apple Inc.', 'exchDisp': 'NASDAQ', 'sector': 'Technology', 'sectorDisp': 'Technology', 'industry': 'Consumer Electronics', 'industryDisp': 'Consumer Electronics', 'dispSecIndFlag': True, 'isYahooFinance': True}, {'exchange': 'NYQ', 'shortname': 'Apple Hospitality REIT, Inc.', 'quoteType': 'EQUITY', 'symbol': 'APLE', 'index': 'quotes', 'score': 21978, 'typeDisp': 'Equity', 'longname': 'Apple Hospitality REIT, Inc.', 'exchDisp': 'NYSE', 'sector': 'Real Estate', 'sectorDisp': 'Real Estate', 'industry': 'REIT—Hotel & Motel', 'industryDisp': 'REIT—Hotel & Motel', 'isYahooFinance': True}, {'exchange': 'NEO', 'shortname': 'APPLE CDR (CAD HEDGED)', 'quoteType': 'EQUITY', 'symbol': 'AAPL.NE', 'index': 'quotes', 'score': 20625, 'typeDisp': 'Equity', 'longname': 'Apple Inc.', 'exchDisp': 'NEO', 'sector': 'Technology', 'sectorDisp': 'Technology', 'industry': 'Consumer Electronics', 'industryDisp': 'Consumer Electronics', 'isYahooFinance': True}, {'exchange': 'GER', 'shortname': 'APPLE INC.', 'quoteType': 'EQUITY', 'symbol': 'APC.DE', 'index': 'quotes', 'score': 20216, 'typeDisp': 'Equity', 'longname': 'Apple Inc.', 'exchDisp': 'XETRA', 'sector': 'Technology', 'sectorDisp': 'Technology', 'industry': 'Consumer Electronics', 'industryDisp': 'Consumer Electronics', 'isYahooFinance': True}, {'exchange': 'BUE', 'shortname': 'APPLE INC CEDEAR(REPR 1/10 SHR)', 'quoteType': 'EQUITY', 'symbol': 'AAPL.BA', 'index': 'quotes', 'score': 20101, 'typeDisp': 'Equity', 'longname': 'Apple Inc.', 'exchDisp': 'Buenos Aires', 'sector': 'Technology', 'sectorDisp': 'Technology', 'industry': 'Consumer Electronics', 'industryDisp': 'Consumer Electronics', 'isYahooFinance': True}, {'exchange': 'PNK', 'shortname': 'APPLE RUSH COMPANY INC', 'quoteType': 'EQUITY', 'symbol': 'APRU', 'index': 'quotes', 'score': 20082, 'typeDisp': 'Equity', 'longname': 'Apple Rush Company, Inc.', 'exchDisp': 'OTC Markets', 'sector': 'Consumer Defensive', 'sectorDisp': 'Consumer Defensive', 'industry': 'Beverages—Non-Alcoholic', 'industryDisp': 'Beverages—Non—Alcoholic', 'isYahooFinance': True}, {'exchange': 'MEX', 'shortname': 'APPLE INC', 'quoteType': 'EQUITY', 'symbol': 'AAPL.MX', 'index': 'quotes', 'score': 20071, 'typeDisp': 'Equity', 'longname': 'Apple Inc.', 'exchDisp': 'Mexico', 'sector': 'Technology', 'sectorDisp': 'Technology', 'industry': 'Consumer Electronics', 'industryDisp': 'Consumer Electronics', 'isYahooFinance': True}]
        print(stock_data)
        # return render_template('thirdpage.html', stock_data = filtered_stock_data)
        return jsonify(stock_data)
    return render_template('thirdpage.html', stock_data=None) 



if __name__ == '__main__':
    app.run(debug = True)



 #if response.status_code == 200:
        #    data = response.json()

        #    results = data.get('quotes', [])

        #print(response.json())
        #    return jsonify(results)
        #else:
        #return jsonify([])

 ##for stock in data.get('quotes'):
            #stock_info = {
              #  "stock": stock.get("shortname"),
               # "industry": stock.get("industry"),
                #"symbol": stock.get("symbol"),
                #"score": stock.get("score"),
           ## }
            #stock_data.append(stock_info)
        #return jsonify({"results": stock_data})