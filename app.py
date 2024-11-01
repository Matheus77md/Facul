from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Conexão com o banco de dados
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="senha123", 
    database="sistema_consultas"
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

# Cadastro de pacientes
@app.route('/cadastrar_paciente', methods=['GET', 'POST'])
def cadastrar_paciente():
    if request.method == 'POST':
        cpf = request.form['cpf']
        nome = request.form['nome']
        idade = request.form['idade']
        telefone = request.form['telefone']
        email = request.form['email']
        cursor.execute("INSERT INTO pacientes (cpf, nome, idade, telefone, email) VALUES (%s, %s, %s, %s, %s)", 
                       (cpf, nome, idade, telefone, email))
        db.commit()
        return redirect('/')
    return render_template('cadastrar_paciente.html')

# Agendamento de consultas
@app.route('/agendar_consulta', methods=['GET', 'POST'])
def agendar_consulta():
    if request.method == 'POST':
        cpf_paciente = request.form['cpf']
        data_consulta = request.form['data_consulta']
        horario = request.form['horario']
        medico = request.form['medico']
        cursor.execute("INSERT INTO consultas (cpf_paciente, data_consulta, horario, medico) VALUES (%s, %s, %s, %s)",
                       (cpf_paciente, data_consulta, horario, medico))
        db.commit()
        return redirect('/')
    return render_template('agendar_consulta.html')

# Atualização de consultas
@app.route('/atualizar_consulta', methods=['GET', 'POST'])
def atualizar_consulta():
    if request.method == 'POST':
        cpf_paciente = request.form['cpf']
        data_consulta = request.form['data_consulta']
        horario = request.form['horario']
        novo_horario = request.form['novo_horario']
        novo_medico = request.form['novo_medico']
        cursor.execute("UPDATE consultas SET horario = %s, medico = %s WHERE cpf_paciente = %s AND data_consulta = %s AND horario = %s",
                       (novo_horario, novo_medico, cpf_paciente, data_consulta, horario))
        db.commit()
        return redirect('/')
    return render_template('atualizar_consulta.html')

# Cancelamento de consultas
@app.route('/cancelar_consulta', methods=['GET', 'POST'])
def cancelar_consulta():
    if request.method == 'POST':
        cpf_paciente = request.form['cpf']
        data_consulta = request.form['data_consulta']
        horario = request.form['horario']
        cursor.execute("DELETE FROM consultas WHERE cpf_paciente = %s AND data_consulta = %s AND horario = %s", 
                       (cpf_paciente, data_consulta, horario))
        db.commit()
        return redirect('/')
    return render_template('cancelar_consulta.html')

if __name__ == '__main__':
    app.run(debug=True)
