from flask import Flask, request, render_template

app = Flask(__name__,template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    try:
        number = int(request.args.get('number'))
        if number % 2 == 0:
            result = 'even'
        else:
            result = 'odd'
    except (TypeError, ValueError):
        result = 'not an integer'
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)