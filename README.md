# 🎲 Simulador RNG em Python

Projeto educacional desenvolvido em Python para estudar o funcionamento de um sistema pseudoaleatório com probabilidades ponderadas.
O programa simula rodadas formadas por três símbolos independentes, analisa a frequência dos resultados e compara os valores observados experimentalmente com as probabilidades teóricas.
O objetivo do projeto é praticar conceitos de Python, probabilidade, testes automatizados, organização de código e controle de versão com Git.

---

## 📚 Objetivos do projeto

Este projeto foi criado para estudar, na prática:

- geração de números pseudoaleatórios;
- probabilidades ponderadas;
- eventos independentes;
- simulações com grande quantidade de repetições;
- comparação entre probabilidade teórica e frequência observada;
- seeds e reprodutibilidade;
- funções e módulos em Python;
- pacotes Python;
- dicionários;
- loops e estruturas condicionais;
- validação de parâmetros;
- tratamento de erros;
- testes automatizados;
- mocks;
- injeção de dependência;
- organização de projetos;
- versionamento com Git.

---

## 🎰 Funcionamento da simulação

Cada rodada gera três símbolos de forma independente.

Os símbolos possuem pesos diferentes:

| Símbolo | Peso | Probabilidade |
|---|---:|---:|
| 🍒 | 35 | 35% |
| 🍋 | 27 | 27% |
| 🔔 | 20 | 20% |
| 💎 | 12 | 12% |
| ⭐ | 6 | 6% |

A soma dos pesos é:

```text
35 + 27 + 20 + 12 + 6 = 100
```

Portanto, os pesos podem ser interpretados diretamente como porcentagens.

---

## 🎯 Sorteio ponderado

O motor gera um número inteiro pseudoaleatório entre:

```text
1 e 100
```

Depois utiliza os pesos acumulados para descobrir qual símbolo corresponde ao número sorteado.

Exemplo:

```text
1  - 35  → 🍒
36 - 62  → 🍋
63 - 82  → 🔔
83 - 94  → 💎
95 - 100 → ⭐
```

Assim, símbolos com pesos maiores ocupam intervalos maiores e aparecem com maior frequência ao longo de muitas simulações.

---

## 🧮 Probabilidade das triplas

Uma rodada contém três sorteios independentes.

Para obter três símbolos iguais, a probabilidade individual do símbolo precisa ocorrer três vezes.

A fórmula utilizada é:

```text
P(tripla) = P(símbolo)³
```

Por exemplo, para 🍒:

```text
P(🍒) = 0,35

P(🍒🍒🍒) = 0,35³

P(🍒🍒🍒) = 0,042875

P(🍒🍒🍒) = 4,2875%
```

As probabilidades teóricas são:

| Tripla | Probabilidade teórica |
|---|---:|
| 🍒🍒🍒 | 4,2875% |
| 🍋🍋🍋 | 1,9683% |
| 🔔🔔🔔 | 0,8000% |
| 💎💎💎 | 0,1728% |
| ⭐⭐⭐ | 0,0216% |

Somando todas as possibilidades de três símbolos iguais:

```text
4,2875%
+ 1,9683%
+ 0,8000%
+ 0,1728%
+ 0,0216%
= 7,2502%
```

Portanto, a probabilidade teórica de qualquer tripla é:

```text
7,2502%
```

---

## 🔬 Teoria x experimento

Uma das propostas do projeto é comparar a matemática com os resultados produzidos pela simulação.

Durante a execução, o programa registra:

- quantidade total de rodadas;
- quantidade total de símbolos sorteados;
- quantidade de triplas;
- frequência total de triplas;
- distribuição observada de cada símbolo;
- quantidade observada de cada tripla;
- quantidade teoricamente esperada de cada tripla;
- porcentagem teórica;
- porcentagem observada.

Com poucas rodadas, os resultados podem variar bastante.

À medida que o número de rodadas aumenta, as frequências observadas tendem a se aproximar das probabilidades teóricas.

Esse comportamento está relacionado à **Lei dos Grandes Números**.

---

## 🌱 Seed e reprodutibilidade

O projeto permite utilizar uma `seed` para tornar uma simulação reproduzível.

Exemplo:

```python
seed = 42
```

O simulador cria um gerador próprio:

```python
gerador = random.Random(seed)
```

Quando a mesma seed é utilizada com as mesmas condições, a sequência pseudoaleatória gerada é reproduzível.

Isso é especialmente útil para:

- testes;
- experimentos;
- depuração;
- comparação de resultados.

O projeto utiliza um objeto `random.Random` próprio em vez de depender diretamente do estado pseudoaleatório global do módulo `random`.

---

## 💉 Injeção de dependência

O gerador pseudoaleatório é criado pelo simulador e enviado ao motor.

Fluxo simplificado:

```text
main.py
   │
   ▼
simulador.py
   │
   ├── cria random.Random(seed)
   │
   ▼
executar_rodada(gerador)
   │
   ▼
motor.py
   │
   ▼
sortear_simbolo(gerador)
```

Em vez de o motor procurar um gerador global, ele recebe explicitamente o objeto de que precisa.

Essa abordagem reduz dependências globais e facilita testes e controle do estado pseudoaleatório.

---

## 🗂️ Estrutura do projeto

```text
simulador-rng/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── motor.py
│   └── simulador.py
│
├── tests/
│   ├── test_config.py
│   ├── test_motor.py
│   └── test_simulador.py
│
├── data/
├── .gitignore
└── README.md
```

### `config.py`

Armazena as configurações do experimento, incluindo:

- símbolos;
- pesos;
- multiplicadores utilizados pela simulação.

### `motor.py`

Contém a lógica fundamental de uma rodada:

- sorteio ponderado;
- geração das três posições;
- identificação de símbolos iguais.

### `simulador.py`

Controla a execução de várias rodadas.

Também é responsável por:

- validar a quantidade de rodadas;
- criar o gerador pseudoaleatório;
- contar símbolos;
- contar triplas;
- calcular a frequência observada.

### `main.py`

É o ponto de entrada do programa.

Executa a simulação e apresenta o relatório estatístico no terminal.

### `tests/`

Contém os testes automatizados do projeto.

---

## 🧪 Testes automatizados

O projeto utiliza a biblioteca padrão:

```python
unittest
```

Os testes verificam diferentes comportamentos do sistema, incluindo:

- soma dos pesos igual a 100;
- símbolos sorteados válidos;
- estrutura de uma rodada;
- reconhecimento de uma tripla;
- resultado de símbolos diferentes;
- quantidade total de símbolos contabilizados;
- limites da quantidade de triplas;
- limites da frequência percentual;
- consistência entre triplas e total contabilizado;
- rejeição de zero rodadas;
- rejeição de valores negativos;
- rejeição de tipos inválidos;
- reprodutibilidade utilizando a mesma seed.

Alguns testes utilizam:

```python
unittest.mock.patch
```

Isso permite substituir temporariamente partes do sistema por resultados controlados e testar comportamentos específicos.

---

## ▶️ Como executar

### Requisitos

O projeto utiliza apenas recursos da biblioteca padrão do Python.

É necessário possuir Python instalado.

### Executar a simulação

Na pasta raiz do projeto:

```bash
python -m src.main
```

### Executar todos os testes

```bash
python -m unittest discover -s tests -v
```

Os testes devem finalizar com:

```text
OK
```

---

## 📊 Exemplo de relatório

Uma execução apresenta informações semelhantes a:

```text
=== RESULTADO DA SIMULAÇÃO ===

Seed: 42
Total de rodadas: 1000000
Total de símbolos: 3000000
Total de vitórias: ...
Frequência de vitórias: ...%

=== DISTRIBUIÇÃO DOS SÍMBOLOS ===

🍒 → Quantidade: ... | Teórico: 35.0000% | Observado: ...%
🍋 → Quantidade: ... | Teórico: 27.0000% | Observado: ...%
🔔 → Quantidade: ... | Teórico: 20.0000% | Observado: ...%
💎 → Quantidade: ... | Teórico: 12.0000% | Observado: ...%
⭐ → Quantidade: ... | Teórico: 6.0000% | Observado: ...%

=== TRIPLAS: TEÓRICO X OBSERVADO ===

🍒🍒🍒 → Observado: ... | Esperado: 42875.00 | Teórico: 4.2875% | Observado: ...%
🍋🍋🍋 → Observado: ... | Esperado: 19683.00 | Teórico: 1.9683% | Observado: ...%
🔔🔔🔔 → Observado: ... | Esperado: 8000.00 | Teórico: 0.8000% | Observado: ...%
💎💎💎 → Observado: ... | Esperado: 1728.00 | Teórico: 0.1728% | Observado: ...%
⭐⭐⭐ → Observado: ... | Esperado: 216.00 | Teórico: 0.0216% | Observado: ...%
```

Os valores observados não precisam ser exatamente iguais aos valores teóricos.

A comparação serve para observar experimentalmente a aproximação das frequências conforme o tamanho da amostra aumenta.

---

## 🛠️ Tecnologias utilizadas

- Python
- `random`
- `unittest`
- `unittest.mock`
- Git

Nenhuma biblioteca externa é necessária.

---

## 🧠 Conceitos praticados

Durante o desenvolvimento foram trabalhados conceitos fundamentais e intermediários de programação, como:

```text
variáveis
funções
parâmetros
argumentos
return
tuplas
desempacotamento
dicionários
loops
condicionais
compreensões
módulos
imports
pacotes
validação
exceções
pseudoaleatoriedade
probabilidade
testes
mocks
injeção de dependência
Git
```

Além da implementação, o projeto procura demonstrar a importância de entender **por que o código funciona**, e não apenas chegar ao resultado final.

---

## ⚠️ Observação

Este projeto é uma simulação educacional criada para estudar programação, pseudoaleatoriedade, testes e probabilidade.

Os símbolos e multiplicadores fazem parte exclusivamente do modelo fictício utilizado no experimento.

---

## 🏁 Versão

```text
v1.0.0
```

Primeira versão completa do simulador RNG educacional.