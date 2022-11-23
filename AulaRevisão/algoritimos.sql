DROP DATABASE IF EXISTS algoritimos;
CREATE DATABASE algoritimos;

USE algoritimos;

CREATE TABLE disciplina (
id INT NOT NULL AUTO_INCREMENT
,nome VARCHAR(200) NOT NULL
,ch INT
,professor VARCHAR(200)
,chr FLOAT
,CONSTRAINT pk_disciplina PRIMARY KEY (id)
);

SELECT * FROM disciplina;