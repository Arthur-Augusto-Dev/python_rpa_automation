import pandas as pd
import pyautogui
import time

# Configurações iniciais
pyautogui.PAUSE = 1

# 1. Ler a base de dados (o arquivo produtos.csv deve estar na mesma pasta)
tabela = pd.read_csv("produtos.csv")

# 2. Abrir o Bloco de Notas para servir como nosso "sistema"
pyautogui.press("win")
pyautogui.write("notepad")
pyautogui.press("enter")
time.sleep(2)  # Tempo para o Notepad abrir

# Mensagem inicial no arquivo
pyautogui.write("--- INICIANDO CADASTRO DE PRODUTOS ---")
pyautogui.press("enter")

# 3. Rodar o loop para cada linha da tabela
for linha in tabela.index:
    # Extrair dados e converter para string para o PyAutoGUI escrever
    codigo = str(tabela.loc[linha, "codigo"])
    marca = str(tabela.loc[linha, "marca"])
    tipo = str(tabela.loc[linha, "tipo"])
    categoria = str(tabela.loc[linha, "categoria"])
    preco = str(tabela.loc[linha, "preco_unitario"])
    custo = str(tabela.loc[linha, "custo"])

    # Simular o preenchimento no Bloco de Notas
    pyautogui.write(f"ID: {codigo} | Marca: {marca} | Tipo: {tipo} | Preco: {preco}")
    pyautogui.press("enter")

    # Feedback no terminal para você acompanhar
    print(f"Produto {codigo} cadastrado com sucesso!")

pyautogui.write("--- FIM DO PROCESSO ---")
