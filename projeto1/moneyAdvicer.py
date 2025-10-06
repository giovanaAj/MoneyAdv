import requests

def pegarcotacoes(cod_moeda):
    try:
        cod_moeda = cod_moeda.upper()
        requisicao = requests.get(f"https://economia.awesomeapi.com.br/json/last/{cod_moeda}-BRL")
        requisicao.raise_for_status()
        requisicao_dic = requisicao.json()
        moeda_key = f"{cod_moeda}BRL"

        if moeda_key in requisicao_dic:
            cotacao = requisicao_dic[moeda_key]["bid"]
            return cotacao
        else:
            print(f"Cotação não encontrada para {moeda_key}")
            return None

    except Exception as e:
        print(f"Erro ao buscar cotação: {e}")
        return None

# Teste simples se quiser rodar só este arquivo
if __name__ == "__main__":
    print(pegarcotacoes('USD'))  # Exemplo de uso