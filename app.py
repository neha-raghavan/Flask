from flask import Flask,render_template,request,jsonify,redirect,make_response
from evaluation import expression_evaluation as ep
import json
import Calc
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('add.html')
    

@app.route("/result",methods = ['POST'])
def result():
    exp=json.loads(request.data)
    result=ep.infix_evaluation(exp['exp'])
    return jsonify({"result":result})
if __name__ == "__main__":
    app.run(debug=True)