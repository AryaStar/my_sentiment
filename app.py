from flask import Flask,render_template, request, redirect, url_for
from function import mymodel

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def input_sentence():
    if request.method == 'POST':
        mystr = request.form.get('mystr')
        if mystr == '':
            return redirect(url_for('wrong'))
        return redirect(url_for('myresult',mystr=mystr))

    return render_template('index.html')


@app.route('/myresult/<mystr>')
def myresult(mystr):
    my_result = mymodel(mystr)
    return render_template('result.html',myresult=my_result)

@app.route('/wrong')
def wrong():
    return render_template('wrong.html')

if __name__ == '__main__':
    app.run(debug=True)
