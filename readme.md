# Registro de Pacientes e Variantes Genéticas

Este projeto é uma aplicação para registrar e gerenciar informações de pacientes e variantes genéticas. A aplicação fornece uma API RESTful que permite a realização de operações de criação, leitura, atualização e exclusão (CRUD) de registros de pacientes e variantes genéticas.

## Endpoints da API

### Pacientes

- **Criar um Paciente:**
    - Rota: '**POST /pacientes**'
    - Descrição: Cria um novo registro de paciente com os dados fornecidos.
    - Exemplo:
  
```python
@app.route('/pacientes', methods=['POST'])
def criar_paciente_route():
    return criar_paciente()
```

- **Listar Todos os Pacientes:**
    - Rota: '**GET /pacientes**'
    - Descrição: Retorna uma lista de todos os registros de pacientes.
    -  Exemplo:
  
```python
@app.route('/pacientes', methods=['GET'])
def listar_pacientes_route():
    return listar_pacientes()
```


- **Atualizar um Paciente por ID:**
    - Rota: '**PUT /pacientes/<int:paciente_id>**'
    - Descrição: Atualiza os dados de um paciente existente com base no ID fornecido.
    -  Exemplo:
  
```python
@app.route('/pacientes/<int:paciente_id>', methods=['PUT'])
def atualizar_paciente_route():
    return atualizar_paciente()
```

- **Recuperar um Paciente por ID:**
    - Rota: '**GET /pacientes/<int:paciente_id>**'
    - Descrição:  Recupera os detalhes de um paciente com base no ID fornecido.
    -  Exemplo:
  
```python
@app.route('/pacientes/<int:paciente_id>', methods=['GET'])
def obter_paciente_route():
    return obter_paciente()
```

- **Excluir um Paciente por ID:**
    - Rota: '**DELETE /pacientes/<int:paciente_id>**'
    - Descrição:  Exclui um paciente com base no ID fornecido.
    -  Exemplo:
  
```python
@app.route('/pacientes/<int:paciente_id>', methods=['DELETE'])
def excluir_paciente_route():
    return excluir_paciente()
```
### Variantes Genéticas

- **Criar uma Variante Genética:**
    - Rota: '**POST /variantes**'
    - Descrição:  Cria um novo registro de variante genética com os dados fornecidos.
    -  Exemplo:
  
```python
@app.route('/variantes', methods=['POST'])
def criar_variante_route():
    return criar_variante()
```

- **Listar Todas as Variantes Genéticas:**
    - Rota: '**GET /variantes**'
    - Descrição: Retorna uma lista de todos os registros de variantes genéticas.
    -  Exemplo:
  
```python
@app.route('/variantes', methods=['GET'])
def listar_variantes_route():
    return listar_variantes()
```

- **Atualizar uma Variante Genética por ID:**
    - Rota: '**PUT /variantes/<int:variante_id>**'
    - Descrição: : Atualiza os dados de uma variante genética existente com base no ID fornecido.
    -  Exemplo:
  
```python
@app.route('/variantes/<int:variante_id>', methods=['PUT'])
def atualizar_variante_route():
    return atualizar_variante()

```

- **Recuperar uma Variante Genética por ID:**
    - Rota: '**GET /variantes/<int:variante_id>**'
    - Descrição: : Recupera os detalhes de uma variante genética com base no ID fornecido.
    -  Exemplo:
  
```python
@app.route('/variantes/<int:variante_id>', methods=['GET'])
def obter_variante_route():
    return obter_variante()
```

- **Excluir uma Variante Genética por ID:**
    - Rota: '**DELETE /variantes/<int:variante_id>**'
    - Descrição: : Exclui uma variante genética com base no ID fornecido.
    -  Exemplo:
  
```python
@app.route('/variantes/<int:variante_id>', methods=['DELETE'])
def excluir_variante_route():
    return excluir_variante()
```

## Executando a Aplicação Localmente

Para executar a aplicação localmente, siga estas etapas:

1. Clone o repositório do projeto para sua máquina local.
2. Certifique-se de ter Python e as bibliotecas necessárias instaladas.
3. Navegue até o diretório raiz do projeto em seu terminal.
4. Execute o seguinte comando para iniciar a aplicação:
   
```python
python app.py
```
5. A aplicação estará disponível em '**http://localhost:5000**'.


## Realizando Consultas via API

Você pode usar ferramentas como '**curl**' ou um cliente API, como o '**requests**' do Python, para realizar consultas à API. Aqui está um exemplo de como usar '**requests**' para fazer uma consulta:

```python
import requests

base_url = 'http://localhost:5000'

# Exemplo de criação de um paciente
data = {
    'nome_completo': 'Nome do Paciente',
    'idade': 30,
    'sexo': 'Masculino'
}

response = requests.post(f'{base_url}/pacientes', json=data)
print(response.json())

# Exemplo de listagem de pacientes
response = requests.get(f'{base_url}/pacientes')
print(response.json())

```

