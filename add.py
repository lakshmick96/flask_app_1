from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def add():
   return render_template('add.html')

@app.route('/', methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		num1 = request.form['num1']
		num2 = request.form['num2']
		result = int(num1) + int(num2)
		return render_template('result.html', num1=num1, num2=num2, result=result) 
if __name__ == '__main__':
   app.run(debug = True)
