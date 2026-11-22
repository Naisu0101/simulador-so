# Simulador de Sistema Operacional
# Aluno: Andre Filipe Vaz Dos Santos Oliveira - RA 252-000078

from collections import deque

ARQUIVO = "dados_sistema.txt"

# estruturas (comecam vazias)
fila = deque()   # procs esperando a CPU -> [pid, nome, prioridade]
pilha = []       # chamadas de sub-rotinas -> [id, rotina, tipo]
lista = []       # tabela de procs ativos -> [pid, nome, estado]
arvore = {}      # sist. de arquivos (dicts aninhados)


# ================= FILA (escalonamento) =================

def fila_add():
    pid = input("PID: ")
    nome = input("Nome do processo: ")
    prio = input("Prioridade: ")
    fila.append([pid, nome, prio])  # entra no fim (FIFO)
    print("Processo add na fila.")


def fila_ver():
    if len(fila) == 0:
        print("Fila vazia.")
        return
    pos = 1
    for p in fila:
        print(pos, "- PID:", p[0], "| Nome:", p[1], "| Prioridade:", p[2])
        pos += 1


def fila_atualizar():
    pid = input("PID do processo: ")
    for p in fila:
        if p[0] == pid:
            p[2] = input("Nova prioridade: ")  # so muda o dado, n mexe na ordem
            print("Atualizado.")
            return
    print("PID nao encontrado.")


def fila_remover():
    if len(fila) == 0:
        print("Fila vazia.")
        return
    p = fila.popleft()  # sai o 1o da fila (FIFO)
    print("Processo", p[1], "foi executado na CPU.")


# ================= PILHA (chamadas) =================

def pilha_add():
    id = input("ID da chamada: ")
    rotina = input("Nome da rotina: ")
    tipo = input("Tipo (sub-rotina/interrupcao): ")
    pilha.append([id, rotina, tipo])  # entra no topo (LIFO)
    print("Chamada empilhada.")


def pilha_ver():
    if len(pilha) == 0:
        print("Pilha vazia.")
        return
    # mostra do topo pra base
    for i in range(len(pilha) - 1, -1, -1):
        c = pilha[i]
        print("ID:", c[0], "| Rotina:", c[1], "| Tipo:", c[2])


def pilha_atualizar():
    if len(pilha) == 0:
        print("Pilha vazia.")
        return
    topo = pilha[-1]  # so mexe no topo
    print("Topo atual:", topo[1])
    topo[2] = input("Novo tipo: ")
    print("Atualizado.")


def pilha_remover():
    if len(pilha) == 0:
        print("Pilha vazia.")
        return
    c = pilha.pop()  # tira do topo (LIFO)
    print("Rotina", c[1], "finalizada.")


# ================= LISTA (tabela de processos) =================

def lista_add():
    pid = input("PID: ")
    nome = input("Nome do processo: ")
    estado = input("Estado: ")
    lista.append([pid, nome, estado])
    print("Processo add na tabela.")


def lista_ver():
    if len(lista) == 0:
        print("Tabela vazia.")
        return
    for i in range(len(lista)):
        p = lista[i]
        print("[" + str(i) + "] PID:", p[0], "| Nome:", p[1], "| Estado:", p[2])


def lista_atualizar():
    lista_ver()
    if len(lista) == 0:
        return
    i = int(input("Indice: "))
    if i < 0 or i >= len(lista):  # vrf se o indice existe
        print("Indice invalido.")
        return
    lista[i][2] = input("Novo estado: ")
    print("Atualizado.")


def lista_remover():
    lista_ver()
    if len(lista) == 0:
        return
    i = int(input("Indice: "))
    if i < 0 or i >= len(lista):
        print("Indice invalido.")
        return
    p = lista.pop(i)  # remove pelo indice
    print("Processo", p[1], "encerrado.")


# ================= ARVORE (sist. de arquivos) =================

def arv_inserir(partes):
    atual = arvore
    for nome in partes:
        if nome not in atual:
            atual[nome] = {}  # cria a pasta se n existir
        atual = atual[nome]   # desce um nivel


def arv_achar(partes):
    # anda pelo caminho e devolve o no (ou None)
    atual = arvore
    for nome in partes:
        if nome not in atual:
            return None
        atual = atual[nome]
    return atual


def arv_mostrar(no, nivel):
    for nome in no:
        print("    " * nivel + "|-- " + nome)
        arv_mostrar(no[nome], nivel + 1)  # recursao p/ os filhos


def arv_add():
    caminho = input("Caminho (ex: raiz/home/andre): ")
    arv_inserir(caminho.split("/"))
    print("Caminho criado.")


def arv_ver():
    if len(arvore) == 0:
        print("Arvore vazia.")
        return
    arv_mostrar(arvore, 0)


def arv_renomear():
    caminho = input("Caminho da pasta: ").split("/")
    pai = arv_achar(caminho[:-1])  # pega a pasta de cima
    velho = caminho[-1]
    if pai is None or velho not in pai:
        print("Caminho nao encontrado.")
        return
    novo = input("Novo nome: ")
    pai[novo] = pai.pop(velho)  # troca a chave e mantem o conteudo
    print("Renomeado.")


def arv_remover():
    caminho = input("Caminho da pasta: ").split("/")
    pai = arv_achar(caminho[:-1])
    nome = caminho[-1]
    if pai is None or nome not in pai:
        print("Caminho nao encontrado.")
        return
    del pai[nome]  # apaga a pasta e tudo dentro
    print("Removido.")


# ================= ARQUIVO TXT =================

def arv_salvar(no, caminho, arq):
    for nome in no:
        novo = caminho + [nome]
        if len(no[nome]) == 0:
            # chegou na folha -> grava o caminho todo
            arq.write("ARVORE|" + "|".join(novo) + "\n")
        else:
            arv_salvar(no[nome], novo, arq)


def salvar():
    arq = open(ARQUIVO, "w", encoding="utf-8")
    for p in lista:
        arq.write("LISTA|" + "|".join(p) + "\n")
    for p in fila:
        arq.write("FILA|" + "|".join(p) + "\n")
    for c in pilha:  # base -> topo, assim volta na msm ordem
        arq.write("PILHA|" + "|".join(c) + "\n")
    arv_salvar(arvore, [], arq)
    arq.close()
    print("Dados salvos em", ARQUIVO)


def carregar():
    try:
        arq = open(ARQUIVO, "r", encoding="utf-8")
    except FileNotFoundError:
        print("Arquivo nao encontrado.")
        return

    # limpa tudo antes de carregar
    lista.clear()
    fila.clear()
    pilha.clear()
    arvore.clear()

    for linha in arq:
        partes = linha.strip().split("|")
        tipo = partes[0]   # 1o campo diz qual estrutura e
        dados = partes[1:]
        if tipo == "LISTA":
            lista.append(dados)
        elif tipo == "FILA":
            fila.append(dados)
        elif tipo == "PILHA":
            pilha.append(dados)
        elif tipo == "ARVORE":
            arv_inserir(dados)
    arq.close()
    print("Dados carregados.")


# ================= MENUS =================

def submenu(titulo, add, ver, atualizar, remover, txt_remover):
    # menu generico, recebe as funcoes de cada estrutura
    while True:
        print("\n---", titulo, "---")
        print("1 - Adicionar")
        print("2 - Ver")
        print("3 - Atualizar")
        print("4 -", txt_remover)
        print("0 - Voltar")
        op = input("Opcao: ")
        if op == "1":
            add()
        elif op == "2":
            ver()
        elif op == "3":
            atualizar()
        elif op == "4":
            remover()
        elif op == "0":
            break
        else:
            print("Opcao invalida.")


def menu():
    while True:
        print("\n===== SIMULADOR DE SO =====")
        print("1 - Fila de processos (CPU)")
        print("2 - Pilha de chamadas")
        print("3 - Tabela de processos ativos")
        print("4 - Sistema de arquivos")
        print("5 - Salvar dados")
        print("6 - Carregar dados")
        print("0 - Sair")
        op = input("Opcao: ")
        if op == "1":
            submenu("FILA DE PROCESSOS", fila_add, fila_ver, fila_atualizar, fila_remover, "Executar proximo")
        elif op == "2":
            submenu("PILHA DE CHAMADAS", pilha_add, pilha_ver, pilha_atualizar, pilha_remover, "Desempilhar")
        elif op == "3":
            submenu("TABELA DE PROCESSOS", lista_add, lista_ver, lista_atualizar, lista_remover, "Remover")
        elif op == "4":
            submenu("SISTEMA DE ARQUIVOS", arv_add, arv_ver, arv_renomear, arv_remover, "Remover pasta")
        elif op == "5":
            salvar()
        elif op == "6":
            carregar()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opcao invalida.")


menu()
