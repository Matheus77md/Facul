CREATE DATABASE sistema_consultas;

USE sistema_consultas;

CREATE TABLE pacientes (
    cpf VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    telefone VARCHAR(15),
    email VARCHAR(100)
);

SELECT * FROM pacientes;

CREATE TABLE consultas (
    cpf_paciente VARCHAR(11),
    data_consulta DATE,
    horario TIME,
    medico VARCHAR(100),
    PRIMARY KEY (cpf_paciente, data_consulta, horario),
    FOREIGN KEY (cpf_paciente) REFERENCES pacientes(cpf)
);

SELECT * FROM consultas;