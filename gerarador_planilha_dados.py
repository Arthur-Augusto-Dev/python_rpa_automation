import pandas as pd
import os
import time

# 1. Configurações
arquivo_entrada = "produtos.csv"
arquivo_saida = "Relatorio_Final_LibreOffice.xlsx"

print("--- Iniciando Processo de Exportação ---")

try:
    # Carregar dados
    tabela = pd.read_csv(arquivo_entrada)

    # Tratamento simples para garantir que não vá vazio
    tabela["obs"] = tabela["obs"].fillna("Vazio")

    # 2. Gravação forçada com o motor openpyxl
    # Usamos um gerenciador de contexto para garantir que o arquivo seja fechado corretamente
    with pd.ExcelWriter(arquivo_saida, engine="openpyxl") as writer:
        tabela.to_excel(writer, index=False)

    # Pequena pausa para o Windows liberar o arquivo do cache
    time.sleep(1)

    # 3. Verificação de sucesso
    if os.path.getsize(arquivo_saida) > 0:
        print(f"✅ SUCESSO! Arquivo gerado com {os.path.getsize(arquivo_saida)} bytes.")
        print(f"Caminho: {os.path.abspath(arquivo_saida)}")
    else:
        print("❌ ERRO: O arquivo foi criado mas continua com 0 KB.")

except Exception as e:
    print(f"❌ Ocorreu um erro: {e}")

print("--- Processo Finalizado ---")
