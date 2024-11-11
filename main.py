from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')  


@app.route('/process', methods=['POST'])
def process():

    name = request.form['name']
    
    if name == 'penis':
        return redirect('/penis')
    

    return f"<p>Hallo, {name}</p>"

@app.route('/penis')
def catpic():
    return render_template('jont.html')

if __name__ == '__main__':
    app.run(debug=True)