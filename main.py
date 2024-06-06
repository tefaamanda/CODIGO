from flask import Flask, render_template, request, redirect
app = Flask(__name__) #instacia flask no aplicativo

#lista
contatos = []

@app.route('/')
def index():
    return render_template('index.html', contatos=contatos)

@app.route('/agenda', methods=['GET', 'POST'])
def agenda():
    if request.method == 'POST':
        nomea = request.form['nomea']
        nomet = request.form['nomet']
        data = request.form['data']
        sintomas = request.form['sintomas']
        codigo = len(contatos)
        contatos.append([codigo, nomea, nomet, data, sintomas])
        return redirect('/')
    else:
        return render_template('agenda.html')


@app.route('/apagar_contato/<int:codigo>')
def apagar_contato(codigo):
    """
    Rota para apagar um contato da lista.
    """
    del contatos[codigo]
    return redirect('/')  # Redireciona de volta para a página inicial

@app.route('/calculadoramp')
def calculadoramp():
    return render_template('calculadoramp.html', resultado="")

@app.route('/calculadoram')
def calculadoram():
    return render_template('calculadoram.html', resultado="")



@app.route('/resultado', methods=['POST'])
def resultado():
    dose = 0
    if request.method == 'POST':
        peso_animal = int(request.form['peso'])
        dose_rec = int(request.form['dose_r'])
        dose = peso_animal * dose_rec

        return render_template('calculadoramp.html', resultado=f"A dose a ser administrada ao animal é de {dose} mg/kg.")



if __name__ == '__main__':
    app.run(debug=True) #executa o aplicativo flask