from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def pagina_inicial():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        nome = request.form['nome']
        peso = request.form['peso']
        altura = request.form['altura']
        resultado = None

        erros = []
        if nome == '':
            erros.append("campo nome obrigatório")

        if peso == '':
            erros.append("campo peso obrigatório")

        else:
            peso = float(peso)
            if peso <= 0 or peso > 300:
               erros.append("peso deve ser maior que 0 e até 300")


        if altura == '':
                erros.append("campo altura obrigatório")
        else:
            altura = float(altura)
            if altura < 0.5 or altura > 2.5:
                erros.append("altura deve ser entre 0,5 e 2,5M")       

        if len(erros) == 0 :

            altura2 = altura * altura
            imc = round(peso / altura2, 2)

            if imc >= 30:
                mensagem = "Obesidade"
                cor = "danger"
            elif imc >= 25 :
                mensagem = "Sobrepeso"
                cor = "warning"
            elif imc >= 18.5 :
                mensagem = "Peso normal"
                cor = "success"
            else :
                mensagem = "Abaixo do peso"
                cor = "info"

          #  resultado =  {"imc" : imc, "mensagem" : mensagem, "erros" : erros, "nome" : nome}

            return render_template('index.html', imc = imc, mensagem = mensagem, nome = nome, cor = cor)
    return render_template('index.html', erros = erros)


@app.route('/equipe')
def contato():
    return render_template('equipe.html')


if __name__ == '__main__':
    app.run(debug=True)

