#Gabriel Vasquez - RM: 557056
#Gustavo Oliveira - RM: 559163

from datetime import datetime

def coletar_dados():
    # Inicializa listas para armazenar os dados coletados
    datas = []
    temperaturas = []
    ph_valores = []
    contaminacoes = []
    
    while True:
        # Menu para o usuário selecionar a opção desejada
        print("\n[Menu de Coleta de Dados]")
        print("1. Inserir dados de qualidade da água")
        print("2. Finalizar e analisar dados")
        escolha = input("Escolha uma opção: ")
        
        # Verifica a escolha do usuário
        if escolha == '2':
            break
        elif escolha == '1':
            # Coleta os dados da água
            data_input = input("Digite a data (AAAA-MM-DD): ")
            # Verifica se a data está no formato correto
            if len(data_input) != 10 or data_input[4] != '-' or data_input[7] != '-':
                print("Data inválida. Por favor, use o formato AAAA-MM-DD.")
                continue
            # Divide a data em partes e converte para um objeto datetime
            data_parts = data_input.split('-')
            ano, mes, dia = map(int, data_parts)
            # Verifica se os valores de ano, mês e dia são válidos
            if not (1 <= mes <= 12 and 1 <= dia <= 31):
                print("Data inválida. Por favor, use o formato AAAA-MM-DD.")
                continue
            data = datetime(ano, mes, dia)
            
            # Coleta a temperatura da água
            temp_input = input("Digite a temperatura da água: ")
            # Verifica se a temperatura é um número válido
            if not temp_input.replace('.', '', 1).isdigit():
                print("Temperatura inválida. Por favor, digite um número.")
                continue
            temp = float(temp_input)

            # Coleta o pH da água
            ph_input = input("Digite o pH da água: ")
            # Verifica se o pH é um número válido
            if not ph_input.replace('.', '', 1).isdigit():
                print("pH inválido. Por favor, digite um número.")
                continue
            ph = float(ph_input)

            # Coleta o nível de contaminação da água
            cont_input = input("Digite o nível de contaminação: ")
            # Verifica se o nível de contaminação é um número válido
            if not cont_input.replace('.', '', 1).isdigit():
                print("Nível de contaminação inválido. Por favor, digite um número.")
                continue
            cont = float(cont_input)
            
            # Adiciona os dados coletados às listas correspondentes
            datas.append(data)
            temperaturas.append(temp)
            ph_valores.append(ph)
            contaminacoes.append(cont)
            
            print("\nDados inseridos com sucesso!")
        else:
            print("Escolha inválida. Tente novamente.")
    
    return datas, temperaturas, ph_valores, contaminacoes

# Função para exibir estatísticas básicas dos dados coletados
def estatisticas_basicas(datas, temperaturas, ph_valores, contaminacoes):
    for valores, nome in zip([temperaturas, ph_valores, contaminacoes], ['temperatura', 'ph', 'contaminacao']):
        if valores:
            # Calcula a média, mínimo e máximo dos valores
            media = sum(valores) / len(valores)
            minimo = min(valores)
            maximo = max(valores)
            # Exibe as estatísticas básicas
            print(f"\n{nome.capitalize()}:")
            print(f"  Média = {media:.2f}")
            print(f"  Mínimo = {minimo:.2f}")
            print(f"  Máximo = {maximo:.2f}")
        else:
            print(f"\nNenhum dado para {nome}.")

# Função para verificar alertas baseados nos dados coletados
def verificar_alertas(datas, temperaturas, ph_valores, contaminacoes):
    alertas = {
        'temperatura': [i for i, valor in enumerate(temperaturas) if valor > 28 or valor < 22],
        'ph': [i for i, valor in enumerate(ph_valores) if valor < 7.5 or valor > 8.5],
        'contaminacao': [i for i, valor in enumerate(contaminacoes) if valor > 0.1]
    }
    
    for parametro, indices in alertas.items():
        if indices:
            # Exibe alertas caso os valores estejam fora dos limites
            print(f"\nAlerta: {parametro.capitalize()} fora dos limites em {len(indices)} dias:")
            for i in indices:
                print(f"  - Data: {datas[i].strftime('%Y-%m-%d')}, Valor: {temperaturas[i]}")
        else:
            print(f"\n{parametro.capitalize()} está dentro dos limites aceitáveis.")

# Função principal para executar o programa
def main():
    # Mensagem de boas-vindas
    print("=== Programa de Monitoramento da Qualidade da Água ===")
    # Coleta os dados da água
    datas, temperaturas, ph_valores, contaminacoes = coletar_dados()
    # Verifica se foram coletados dados
    if datas:
        # Exibe estatísticas básicas dos dados coletados
        print("\n=== Estatísticas Básicas ===")
        estatisticas_basicas(datas, temperaturas, ph_valores, contaminacoes)
        # Verifica alertas baseados nos dados coletados
        print("\n=== Verificação de Alertas ===")
        verificar_alertas(datas, temperaturas, ph_valores, contaminacoes)
    else:
        print("Nenhum dado coletado.")

if __name__ == "__main__":
    main()