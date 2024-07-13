class Paciente:
    def __init__(self, nome, idade, endereco, telefone, historico_medico):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.historico_medico = historico_medico
        self.consultas = []
        self.despesas = 0

    def adicionar_consulta(self, data, descricao, valor):
        self.consultas.append({"data": data, "descricao": descricao, "valor": valor})
        self.despesas += valor

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}")
        print(f"Histórico Médico: {self.historico_medico}")
        print("Consultas:")
        for consulta in self.consultas:
            print(f"  - Data: {consulta['data']}, Descrição: {consulta['descricao']}, Valor: R$ {consulta['valor']:.2f}")
        print(f"Total de Despesas: R$ {self.despesas:.2f}")

def cadastrar_paciente():
    nome = input("Nome do Paciente: ")
    idade = int(input("Idade: "))
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    historico_medico = input("Histórico Médico: ")

    paciente = Paciente(nome, idade, endereco, telefone, historico_medico)
    return paciente

def adicionar_consulta_paciente(paciente):
    data = input("Data da Consulta (DD/MM/AAAA): ")
    descricao = input("Descrição da Consulta: ")
    valor = float(input("Valor da Consulta: R$ "))
    paciente.adicionar_consulta(data, descricao, valor)

# Cadastro do paciente
paciente = cadastrar_paciente()

# Adicionar consultas ao paciente
while True:
    adicionar_consulta_paciente(paciente)
    continuar = input("Deseja adicionar outra consulta? (s/n): ")
    if continuar.lower() != 's':
        break

# Exibir os dados do paciente
paciente.exibir_dados()
