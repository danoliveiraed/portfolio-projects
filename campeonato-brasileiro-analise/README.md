# 📊 Análise de Desempenho no Campeonato Brasileiro (2012–2022)

Este projeto tem como objetivo aplicar técnicas de análise de dados utilizando Python e Power BI Web para explorar e visualizar informações relevantes do **Campeonato Brasileiro Série A**, no período de **2012 a 2022**.

---

## 🧰 Ferramentas Utilizadas

- Python (Pandas, Matplotlib)
- Jupyter Notebook (Google Colab)
- Power BI Web
- GitHub

---

## 🗂️ Estrutura do Projeto

```

campeonato-brasileiro-analise/
│
├── data/
│   ├── raw/                       # Dados originais
│   ├── processed/                 # Dados limpos e tratados para Power BI
│
├── notebooks/
│   └── Campeonato_brasileiro_analise.ipynb   # Notebook completo com tratamento, análises e exportações
│
├── dashboards/                    # Capturas dos dashboards criados
│
└── README.md                      # Este arquivo

```

---

## 📈 Dashboards Criados (Power BI Web)

Devido às limitações do Power BI Web (sem DAX ou múltiplos arquivos), todas as agregações foram feitas previamente em Python. Os dashboards foram construídos a partir de arquivos `.csv` já tratados.

### 1. **Gols por Time (Ofensivo e Defensivo)**
- Comparação entre gols marcados e sofridos por equipe
- Destaques:
  - Flamengo-RJ, Atlético-MG e Palmeiras-SP: melhores ataques
  - Chapecoense-SC e Avaí-SC: piores saldos de gols

### 2. **Desempenho Mandante x Visitante**
- Vitórias em casa e fora por time
- Percentual de aproveitamento total
- Gráfico de dispersão: regularidade vs. número de jogos

### 3. **Distribuição de Jogos por Estado**
- Quantidade absoluta e percentual de jogos por estado
- Mostra concentração em estados do Sudeste

---

## 📁 Arquivos Exportados para Power BI

- `gols_total.csv`: Gols marcados e sofridos por time
- `desempenho_times.csv`: Vitórias mandante e visitante + aproveitamento
- `jogos_por_estado.csv`: Contagem de jogos por estado do mandante

---

## 📌 Principais Insights

- O **fator casa** ainda é um diferencial no Brasileirão.
- **Desempenho ofensivo consistente** está diretamente ligado à presença entre os melhores aproveitamentos.
- Estados como **SP e RJ** concentram o maior número de jogos, refletindo o domínio de clubes da região.

---

## 📎 PDF Resumo

Um PDF com os principais insights e capturas dos dashboards foi gerado para apresentação do projeto.  
🔗 https://github.com/danoliveiraed/portfolio-projects/blob/c47ca899163fa035c9e52a3b64b385893788f048/campeonato-brasileiro-analise/dashboard/An%C3%A1lise%20de%20Desempenho%20no%20Campeonato%20Brasileiro_%20Gols%2C%20Jogos%20e%20Aproveitamento%20(2012%20-%202022).pdf

---

## 👨‍💻 Autor

**Dan Oliveira**  
Portfólio: [github.com/danoliveiraed](https://github.com/danoliveiraed)  
Contato: [https://www.linkedin.com/in/danielhroliveira/ 
daniel.rodrigues12.85@gmail.com]


