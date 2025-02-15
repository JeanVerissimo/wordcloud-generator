# Gerador de Nuvem de Palavras para PDF

[🇬🇧 Read in English](README.md)

## Visão Geral

Este projeto implementa um **Gerador de Nuvem de Palavras para PDF** que extrai texto de um arquivo PDF, processa-o removendo stopwords, números e pontuação, e gera uma nuvem de palavras com base na análise de frequência de palavras.

### Principais Funcionalidades:
- **Remoção de Stopwords**: Limpa o texto extraído removendo palavras comuns com base no idioma selecionado.
- **Análise de Frequência de Palavras**: Calcula a ocorrência das palavras e destaca as mais utilizadas.
- **Geração de Nuvem de Palavras**: Exibe uma nuvem de palavras visualmente atraente utilizando as bibliotecas `wordcloud` e `matplotlib`.
- **Suporte a Múltiplos Idiomas**: Permite a remoção de stopwords em diversos idiomas.

---

## Instalação

Para executar este projeto, certifique-se de ter o Python 3.x instalado. Além disso, será necessário instalar as dependências requeridas.

1. **Clone o repositório**:

```bash
git clone https://github.com/JeanVerissimo/wordcloud-generator.git
cd wordcloud-generator
```

2. **Instale as dependências**:

```bash
pip install pymupdf nltk wordcloud matplotlib
```

3. **Baixe as stopwords do NLTK**:

```python
import nltk
nltk.download('stopwords')
```

---

## Uso

Execute o script `main.py` para iniciar a aplicação. Este script fornece uma **interface gráfica** para selecionar um arquivo PDF, analisar seu conteúdo e gerar uma nuvem de palavras.

```bash
python main.py
```

### Passos para Utilização:
1. **Selecionar Idioma**: Escolha um idioma no menu suspenso.
2. **Carregar PDF**: Clique no botão "Carregar PDF" para selecionar um arquivo.
3. **Visualizar Estatísticas de Palavras**: O texto extraído é analisado e estatísticas como total de palavras, palavras únicas e frequência de palavras são exibidas.
4. **Gerar Nuvem de Palavras**: Clique no botão "Gerar Nuvem de Palavras" para visualizar as palavras mais frequentes.

---

