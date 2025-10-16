# ⚙️ Pipeline de Dados: Extração e Fusão com Orientação a Objeto (POO)

Este projeto implementa um pipeline de dados com foco na arquitetura **Orientada a Objeto (POO)** em Python. O objetivo principal é demonstrar a capacidade de **modularização** e **reutilização de código** ao lidar com diferentes formatos de dados.

O pipeline realiza a extração e fusão de dados de duas empresas, tratando arquivos nos formatos **JSON** e **CSV**, e preparando um conjunto de dados limpo e unificado.

## 🧱 Arquitetura e Estrutura do Projeto

O core do projeto está dividido em dois arquivos Python:

* **`processamento_dados.py`**:
    * Contém a **classe principal `Dados`**, que encapsula toda a lógica de leitura (`.csv`, `.json`), manipulação de colunas (`rename_columns`), e o método estático de união (`join`).
    * Demonstra o uso de POO para criar objetos que representam os dados, com atributos como `nomes_colunas` e `qtd_linhas`.
* **`fusao_mercado.py`**:
    * É o script de execução do pipeline (o **main**).
    * Instancia os objetos da classe `Dados` (Empresa A e Empresa B), aplica as transformações de renomeação e realiza a fusão dos DataFrames.
* **`exploracao.ipynb`**: Notebook de exploração de dados inicial e validação do processo de extração.
* **`data_raw/`**: Contém os arquivos de dados brutos de entrada.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Conceitos Chave:** **Orientação a Objeto (POO)**, Herança, Encapsulamento.
* **Bibliotecas:**
    * `pandas` (Manipulação e leitura de dados).
    * `json` e `csv` (Nativas do Python para I/O de arquivos).

## 🚀 Como Executar o Pipeline

Para rodar este projeto, clone o repositório e siga os passos abaixo.

### 1. Pré-requisitos

Certifique-se de que você tem o Python 3 instalado e as dependências listadas no `requirements.txt`.

```bash
# Se você já criou o ambiente virtual (venv), ative-o:
source .venv/bin/activate
# ou
.\.venv\Scripts\activate  # No Windows

# Instale as dependências:
pip install -r requirements.txt
2. Execução
Execute o script principal para rodar todo o pipeline:

Bash

python fusao_mercado.py
O pipeline imprimirá logs no terminal e salvará o arquivo de dados processado na pasta data_processed/.