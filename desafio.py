### Simulador de Agenda de Contatos
# Author: João Paulo Gazola Bebber
# Email: joao.gbebber@gmail.com

import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_contact(contacts, name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "favorite": False,
    }

    contacts.append(contact)
    print(f"\nContato de {name} adicionado com sucesso!")
    return

def list_contacts(contacts, favorites=False):
    print(f'Lista de contatos{" favoritos ⭐️" if favorites else ""}:\n')
    for index, contact in enumerate(contacts, start=1):
        if favorites and not contact["favorite"]:
            continue

        print(f"{index}.")
        print(f'    Nome: {contact["name"]}')
        print(f'    Telefone: {contact["phone"]}')
        print(f'    Email: {contact["email"]}')
        print(f'    Favorito: {"Sim" if contact["favorite"] else "Não"}')

def update_contact(contacts, index, name, phone, email):
    if name:
        contacts[index]["name"] = name
    if phone:
        contacts[index]["phone"] = phone
    if email:
        contacts[index]["email"] = email

    print(f"\nContato {index + 1} atualizado para {name}")
    return

def favorite_contact(contacts, index, revoke):
    if revoke:
        if contacts[index]["favorite"] is False:
            print(f"\nContato {index + 1} já está fora da lista de favoritos")
        else:
            contacts[index]["favorite"] = False
            print(f"\nContato {index + 1} removido da lista de favoritos")
    else:
        if contacts[index]["favorite"] is True:
            print(f"\nContato {index + 1} já é um contato favorito")
        else:
            contacts[index]["favorite"] = True
            print(f"\nContato {index + 1} marcado como favorito")

    return

def delete_contact(contacts, index):
    for contact_index, contact in enumerate(contacts):
        if contact_index == index:
            contacts.remove(contact)

    print(f"\nContato {index + 1} apagado com sucesso!")
    return

contacts = []
while True:
    clear_terminal()
    print("📖 Menu da Agenda:")
    print("1. Adicionar contato")
    print("2. Visualizar contatos cadastrados")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar contato como favorito")
    print("5. Visualizar contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    choice = input("\n👀 O que você deseja fazer? ")

    clear_terminal()
    if choice == "1":
        print("Digite as informações do contato que deseja adicionar:\n")
        name = input("  - Nome: ")
        phone = input("  - Telefone: ")
        email = input("  - Email: ")

        add_contact(contacts=contacts, name=name, phone=phone, email=email)
    elif choice == "2":
        list_contacts(contacts=contacts)
    elif choice == "3":
        list_contacts(contacts=contacts)

        index = input("\nDigite o número do contato que deseja atualizar: ")
        fixed_index = int(index) - 1

        if fixed_index >= 0 and fixed_index < len(contacts):
            clear_terminal()
            print("Digite as informações do contato que deseja atualizar:")
            print("  🔖 (deixe vazio o campo que não quiser alterar)\n")
            name = input("  - Nome: ")
            phone = input("  - Telefone: ")
            email = input("  - Email: ")

            update_contact(contacts=contacts, index=fixed_index, name=name, phone=phone, email=email)
        else:
            print("\n🚨 Índice de contato inválido")
    elif choice == "4":
        revoke = None

        while revoke is None:
            clear_terminal()
            list_contacts(contacts=contacts)

            revoke_string = input("\nVocê deseja remover algum contato dos favoritos? (Y/n): ")

            if revoke_string == "Y" or revoke_string == "y":
                revoke = True
            elif revoke_string == "N" or revoke_string == "n":
                revoke = False
            else:
                continue

        if revoke:
            index = input("\nDigite o número do contato que deseja remover dos favoritos: ")
        else:
            index = input("\nDigite o número do contato que deseja favoritar: ")

        fixed_index = int(index) - 1

        if fixed_index >= 0 and fixed_index < len(contacts):
            favorite_contact(contacts=contacts, index=fixed_index, revoke=revoke)
        else:
            print("\n🚨 Índice de contato inválido")
    elif choice == "5":
        list_contacts(contacts=contacts, favorites=True)
    elif choice == "6":
        list_contacts(contacts=contacts)

        index = input("\nDigite o número do contato que deseja apagar: ")
        fixed_index = int(index) - 1

        if fixed_index >= 0 and fixed_index < len(contacts):
            delete_contact(contacts=contacts, index=fixed_index)
        else:
            print("\n🚨 Índice de contato inválido")
    elif choice == "7":
        break

    input("\nPressione enter para continuar...")

print("🏃 Programa finalizado")
