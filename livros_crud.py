from pymongo import MongoClient
from bson.objectid import ObjectId

class LivroModel:
    def __init__(self, database):
        self.db = database

        #Metodos do exercicio

    def criar_livro(self, titulo: str, autor: str, ano: int, preco: float):
        try:
            res = self.db.collection.insert_one({"titulo": titulo, "autor": autor, "ano": ano, "preco": preco})
            print(f"Livro criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o livro: {e}")
            return None

    def ler_livro_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Livro encontrado: {res}")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao ler o livro: {e}")
            return None

    def atualizar_livros(self, id: str, titulo: str, autor: str, ano: int, preco: float):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}})
            print(f"Livro atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o livro: {e}")
            return None

    def apagar_livros(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Livro deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o livro: {e}")
            return None
    

def main():
    # Conectando ao banco de dados
    client = MongoClient('localhost', 27017)
    db = client['mydatabase']
    
    # Inicializando o modelo de livro
    livro_model = LivroModel(db)

    while True:
        print("\nMenu do programa:")
        print("1. Cria um livro")
        print("2. Ira ler o livro pelo seu id")
        print("3. Atualiza Livro")
        print("4. Deletar Livro")
        print("5. sai do programa")

        choice = input("Escolha um numero: ")

        if choice == "1":
            titulo = input("titulo do livro: ")
            autor = input("autor do livro: ")
            ano = int(input("Ano do livro: "))
            preco = float(input("preco do livro: "))
            livro_model.criar_livro(titulo, autor, ano, preco)
        elif choice == "2":
            livro_id = input("id do livro: ")
            livro_model.ler_livro_id(livro_id)
        elif choice == "3":
            livro_id = input("Entre com id do livro a ser atualizado: ")
            titulo = input("Novo nome do livro: ")
            autor = input("Novo autor do livro: ")
            ano = int(input("Novo ano do livro: "))
            preco = float(input("Novo preço do livro: "))
            livro_model.atualizar_livros(livro_id, titulo, autor, ano, preco)
        elif choice == "4":
            livro_id = input("Id do livro que sera deletado no programa: ")
            livro_model.delete_livro(livro_id)
        elif choice == "5":
            print("Saiu do programa!!!!!!!!")
            break
        else:
            print("Digite uma opcao valida para rodar")

if __name__ == "__main__":
    main()