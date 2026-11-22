# Simulador de Sistema Operacional

Trabalho final de Teoria das Estruturas de Dados.

**Aluno:** André Filipe Vaz Dos Santos Oliveira - RA 252-000078
**Tema:** Tema 3 - Simulador de Sistema Operacional

## O que é

Um programa de terminal que simula algumas partes de um sistema operacional usando as 4 estruturas da matéria: Fila, Pilha, Lista e Árvore. Os dados podem ser salvos e carregados de um arquivo `dados_sistema.txt`.

## Como rodar

Precisa ter o Python 3 instalado.

1. Baixe o `main.py`
2. Abra o terminal na pasta do arquivo
3. Rode:

```
python main.py
```

4. Use os números do menu pra navegar.

O sistema começa vazio. Pra guardar o que você fez, use a opção **5 - Salvar dados**. Na próxima vez, use **6 - Carregar dados** pra trazer tudo de volta.

## Por que cada estrutura

**Fila (deque) - processos esperando a CPU**
Num SO, os processos esperam a vez de usar a CPU por ordem de chegada. Quem chegou primeiro é executado primeiro (FIFO). Por isso a fila: entra no fim e sai do início. Usei o `deque` porque tirar do início dele é rápido, diferente da `list`.

**Pilha (list) - chamadas de sub-rotinas e interrupções**
Quando uma função chama outra, a última chamada precisa terminar antes de voltar pra anterior. Isso é LIFO: o último que entrou é o primeiro que sai. Por isso a pilha: tudo entra e sai pelo topo (`append` e `pop`).

**Lista (list) - tabela de processos ativos**
A tabela de processos não tem uma ordem obrigatória de entrada e saída. Qualquer processo pode ser consultado, alterado ou encerrado a qualquer momento. Por isso a lista, que deixa mexer em qualquer posição pelo índice.

**Árvore (dicionários aninhados) - sistema de arquivos**
Pastas ficam dentro de pastas, formando uma hierarquia (ex: `raiz/home/andre`). Isso é uma árvore. Cada pasta é um dicionário, e as subpastas são as chaves dentro dele.

## Formato do arquivo

Cada linha começa com o nome da estrutura, e os dados são separados por `|`:

```
LISTA|1|chrome|executando
FILA|2|word|alta
PILHA|1|main|sub-rotina
ARVORE|raiz|home|andre
```
