from flask import Flask, request, render_template_string
#
app = Flask(__name__)

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Erro: Divisão por zero!"

def multiplicacao(num1, num2):
    return num1 * num2

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        operacao = request.form.get('operacao')

        if num1 and num2 and operacao:
            num1 = float(num1)
            num2 = float(num2)

            if operacao == 'soma':
                resultado = soma(num1, num2)
            

            return render_template_string('''
                <html>
                    <body>
                        <h1>Resultado da Operação</h1>
                        <p>O resultado da operação é: {{ resultado }}</p>
                    </body>
                </html>
            ''', resultado=resultado)
        else:
            return render_template_string('''
                <html>
                    <body>
                        <h1>Calculadora</h1>
                        <form method="post">
                            <label for="num1">Número 1:</label>
                            <input type="number" id="num1" name="num1"><br><br>
                            <label for="num2">Número 2:</label>
                            <input type="number" id="num2" name="num2"><br><br>
                            <label for="operacao">Operação:</label>
                            <select id="operacao" name="operacao">
                                <option value="soma">Soma</option>
                            </select><br><br>
                            <input type="submit" value="Calcular">
                        </form>
                        <p>Por favor, preencha todos os campos.</p>
                    </body>
                </html>
            ''')
    else:
        return render_template_string('''
            <html>
                <body>
                    <h1>Calculadora</h1>
                    <form method="post">
                        <label for="num1">Número 1:</label>
                        <input type="number" id="num1" name="num1"><br><br>
                        <label for="num2">Número 2:</label>
                        <input type="number" id="num2" name="num2"><br><br>
                        <label for="operacao">Operação:</label>
                        <select id="operacao" name="operacao">
                            <option value="soma">Soma</option>
                        </select><br><br>
                        <input type="submit" value="Calcular">
                    </form>
                </body>
            </html>
        ''')

if __name__ == '__main__':
    app.run(debug=True)