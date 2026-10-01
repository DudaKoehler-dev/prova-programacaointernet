from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def pagina_inicial():
  
    

@app.route('/equipe')
def contato():
    return render_template('equipe.html')


if __name__ == '__main__':
    app.run(debug=True)