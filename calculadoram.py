from flask import Flask, render_template, request, redirect
app = Flask(__name__)

contatos = []


@app.route('/calculadoram')
def calculadoram():
    return render_template('calculadoram.html', resultado='')

@app.route('/resultado', methods=['POST'])
def resultado():
    pesoanimal = float(request.form['peso'])
    graudesidrata = request.form['desidratação']

    if pesoanimal > 0:
        if graudesidrata.upper() == 'LEVE':
            soroml = pesoanimal * 50
            quantidade = f'Você deve aplicar {soroml}ml de soro '
        elif graudesidrata.upper() == 'MODERADA':
            soroml = pesoanimal * 75
            quantidade = f'Você deve aplicar {soroml}ml de soro '
        elif graudesidrata.upper() == 'GRAVE':
            soroml = pesoanimal * 100
            quantidade = f'Você deve aplicar {soroml}ml de soro '
        else:
            quantidade = 'Isso não é um grau válido'

    else:
        quantidade = f'Isso não é um peso válido'

    return render_template('calculadoram.html', resultado=f'{quantidade}')


if __name__ == '__main__':
    app.run(debug=True)