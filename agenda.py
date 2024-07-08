import json

# Função para carregar contatos do arquivo
def carregar_contatos():
    try:
        with open('contatos.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# Função para salvar contatos no arquivo
def salvar_contatos(contatos):
    with open('contatos.json', 'w') as arquivo:
        json.dump(contatos, arquivo)

# Função para adicionar um novo contato
def adicionar_contato(contatos):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contatos.append({'nome': nome, 'telefone': telefone, 'email': email})
    salvar_contatos(contatos)
    print("Contato salvo com sucesso!")

# Função para exibir todos os contatos salvos
def exibir_contatos(contatos):
    for contato in contatos:
        print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")

# Função para buscar um contato pelo nome
def buscar_contato(contatos):
    nome = input("Digite o nome do contato: ")
    for contato in contatos:
        if contato['nome'].lower() == nome.lower():
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
            return
    print("Contato não encontrado.")

# Função para editar um contato já salvo
def editar_contato(contatos):
    nome = input("Digite o nome do contato que deseja editar: ")
    for contato in contatos:
        if contato['nome'].lower() == nome.lower():
            contato['telefone'] = input(f"Novo telefone ({contato['telefone']}): ") or contato['telefone']
            contato['email'] = input(f"Novo email ({contato['email']}): ") or contato['email']
            salvar_contatos(contatos)
            print("Contato editado com sucesso!")
            return
    print("Contato não encontrado.")

# Função para excluir um contato
def excluir_contato(contatos):
    nome = input("Digite o nome do contato que deseja excluir: ")
    for contato in contatos:
        if contato['nome'].lower() == nome.lower():
            contatos.remove(contato)
            salvar_contatos(contatos)
            print("Contato excluído com sucesso!")
            return
    print("Contato não encontrado.")

# Função Main
def main():
    contatos = carregar_contatos()
    while True:
        print("\nAgenda de Contatos")
        print("1. Adicionar contato")
        print("2. Exibir contatos")
        print("3. Buscar contato")
        print("4. Editar contato")
        print("5. Excluir contato")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            adicionar_contato(contatos)
        elif escolha == '2':
            exibir_contatos(contatos)
        elif escolha == '3':
            buscar_contato(contatos)
        elif escolha == '4':
            editar_contato(contatos)
        elif escolha == '5':
            excluir_contato(contatos)
        elif escolha == '6':
            break
        else:
            print("Opção inválida, tente novamente.")

# Execução da função main
if __name__ == "__main__":
    main()
