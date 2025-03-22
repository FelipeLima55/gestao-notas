import sys
from datetime import datetime, timedelta

#Lista para armazenar as notas temporariamente
notas = []

def calcular_data_vencimento(tipo):
    """Define a data de vencimento conforme o tipo"""
    hoje = datetime.today().date()
    dias_para_vencer = 90 if tipo == "NC" else 30
    return hoje + timedelta(days=dias_para_vencer)

def calcular_dias_restantes(data_vencimento):
    hoje = datetime.today().date()
    return (data_vencimento - hoje).days

def adicionar_nota():
    titulo = input("Digite o titulo da nota: ")
    tipo = input("Essa é uma nota (N) ou uma ZZ9 (NC)? ").strip().upper()
    if tipo not in ["N", "NC"]:
        print("Opção inválida! Use 'N' para nota ou 'NC' para ZZ9.")
        return
    data_vencimento = calcular_data_vencimento(tipo)
    dias_restantes = calcular_dias_restantes(data_vencimento)
    endereço = input("Digite o endereço: ")

    #Adicionar a lista de notas
    nota = {
        "titulo": titulo,
        "tipo": tipo,
        "data_vencimento": data_vencimento,
        "endereco": endereço,
        "dias_restantes": dias_restantes
    }
    notas.append(nota)
    
    print(f"\n✅ Nota '{titulo}' cadastrada com sucesso! Vence em {dias_restantes} dias.\n")

def listar_notas():
    if not notas:
        print("Nenhuma nota cadastrada.\n")
        return
    
    print("Notas cadastradas:")
    for idx, nota in enumerate(notas, 1):
        status = "✅ Dentro do prazo" if nota["dias_restantes"] >= 0 else "⚠️ Vencida"
        print(f"{idx}. [{nota['tipo']}] {nota['titulo']} - {nota['data_vencimento']} ({nota['dias_restantes']} dias restantes) - {status}")
        print(f"   📍 Endereço: {nota['endereco']}\n")

def menu():
    while True:
        print("\n=== Gestão de Notas ===")
        print("1. Adicionar Nota")
        print("2. Listar Notas")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_nota()
        elif opcao == "2":
            listar_notas()
        elif opcao == "3":
            print("saindo...")
            sys.exit(0)
        else:
            print("Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    menu()                        
