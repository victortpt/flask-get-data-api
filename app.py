from flask import Flask, render_template
import requests, json
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    req = requests.get('https://cat-fact.herokuapp.com/facts')
    data = json.loads(req.content)
    return render_template('index.html', data=data)

if  (__name__ == "__main__"):
    app.run(debug=True)