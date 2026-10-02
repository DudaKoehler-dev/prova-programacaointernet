# inicia o py
from flask import Flask, render_template, request
app = Flask(__name__)

# define a rota do index
@app.route("/", methods=["GET", "POST"])
def index():
    nome = ""
    peso = ""
    altura = ""
    erros = []
    resultado = None #segurança

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        peso = request.form.get("peso", "").strip()
        altura = request.form.get("altura", "").strip()

        if nome == "":
            erros.append("Informe o seu nome.")

        peso_valor = None
        if peso == "":
            erros.append("Informe o peso.")
        else:
            try:
                peso_valor = float(peso)
                if not 0 < peso_valor :
                    erros.append("O peso deve ser maior que 0")
            except ValueError:
                erros.append("O peso deve ser um número válido.")

        altura_valor = None
        if altura == "":
            erros.append("Informe a altura.")
        else:
            try:
                altura_valor = float(altura)
                if not 0.5 <= altura_valor <= 2.5:
                    erros.append("A altura deve estar entre 0,5 e 2,5 metros.")
            except ValueError:
                erros.append("A altura deve ser um número válido.")

        if not erros:

            ## round para formatar para 2 casas decimais
            imc = round(peso_valor / (altura_valor ** 2), 2)

            if imc < 18.5:
                faixa = "Abaixo do peso"
                cor = "info"
            elif imc < 25:
                faixa = "Peso normal"
                cor = "success"
            elif imc < 30:
                faixa = "Sobrepeso"
                cor = "warning"
            else:
                faixa = "Obesidade"
                cor = "danger"

            resultado = {"nome": nome, "imc": imc, "faixa": faixa, "cor": cor}

    return render_template(
        "index.html",
        nome=nome,
        peso=peso,
        altura=altura,
        erros=erros,
        resultado=resultado,
    )

##/equipe
@app.route("/equipe")
def equipe():
    
    
    return render_template("equipe.html")

## ultima coisa
if __name__ == "__main__":
    app.run(debug=True)
