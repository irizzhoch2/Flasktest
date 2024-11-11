from flask import Flask, request, render_template, redirect
from sqlite import add_name, get_all_names

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():

    name = request.form['name']
    
    if name == 'penis':
        return redirect('/penis')
    
    add_name(name)
    print(f"Name '{name}' wurde erfolgreich hinzugefügt.")

    all_names = get_all_names()

    return(f"<h1>Hallo, {name}</h1> <p>{all_names}</p>")
    
@app.route('/penis')
def catpic():
    return render_template('jont.html')

if __name__ == '__main__':
    app.run(debug=True)