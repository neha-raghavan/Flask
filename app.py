from flask import Flask,render_template,request
from evaluation import expression_evaluation as ep
import Calc
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('add.html')
    

@app.route("/result",methods = ['GET'])
def result():
    exp=request.args.get("exp")
    result=ep.infix_evaluation(exp)
    return render_template('result.html', entry=result)
if __name__ == "__main__":
    app.run(debug=True)