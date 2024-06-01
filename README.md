<h1 align=center>Sistema Hospitalar 🏥</br></br><div align=center><img src="http://ForTheBadge.com/images/badges/made-with-python.svg"></div> <img src="https://badges.aleen42.com/src/cli.svg"></h1>
<p text-align=justify>Um hospital precisa de um sistema para ter controle dos médicos, pacientes e exames
realizados, para isso foi desenvolvido um programa Python realizando as seguintes operações:</p>

<ul>
  <li>Cadastrar médico</li>
  <li>Cadastrar paciente</li>
  <li>Cadastrar exame</li>
  <li>Consultar todos os exames de um determinado paciente</li>
</ul>

<p align=justify>Foi utilizado o SQLITE para criação das tabelas: </p>

```markdown

### Tabela: `PACIENTE`

| Campo         | Tipo         | Descrição                          |
|---------------|--------------|------------------------------------|
| ID            | INTEGER      | PRIMARY KEY                        |
| NOME          | VARCHAR(255) | Nome do paciente                   |
| CPF           | VARCHAR(255) | CPF do paciente                    |
| IDADE         | INTEGER      | Idade do paciente                  |

### Tabela: `MEDICO`

| Campo         | Tipo         | Descrição                          |
|---------------|--------------|------------------------------------|
| ID            | INTEGER      | PRIMARY KEY                        |
| NOME          | VARCHAR(255) | Nome do médico                     |
| CRM           | VARCHAR(255) | CRM do médico                      |
| ESPECIALIZACAO| VARCHAR(255) | Especialização do médico           |

### Tabela: `EXAME`

| Campo         | Tipo         | Descrição                          |
|---------------|--------------|------------------------------------|
| ID            | INTEGER      | PRIMARY KEY                        |
| ID_MEDICO     | INTEGER      | ID do médico                       |
| ID_PACIENTE   | INTEGER      | ID do paciente                     |
| DESCRICAO     | VARCHAR(255) | Descrição do exame                 |
| RESULTADO     | VARCHAR(255) | Resultado do exame                 |

```

<p align=justify>Para o mapeamento das tabelas foi utilizado o ORM SQLAlchemy</p>
