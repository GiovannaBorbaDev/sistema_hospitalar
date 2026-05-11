from abc import ABC, abstractmethod
from datetime import datetime


class Pessoa(ABC):
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @abstractmethod
    def exibir_dados(self):
        pass


class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado, cep):
        self._rua = rua
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade
        self._estado = estado
        self._cep = cep

    def __str__(self):
        return f"{self._rua}, {self._numero} - {self._bairro}"


class Demografia:
    def __init__(self, idade, sexo, estado_civil):
        self._idade = idade
        self._sexo = sexo
        self._estado_civil = estado_civil

    def __str__(self):
        return (
            f"Idade: {self._idade}\n"
            f"Sexo: {self._sexo}\n"
            f"Estado Civil: {self._estado_civil}"
        )


class ProntuarioIndividual:
    def __init__(self, numero, historico, alergias):
        self._numero = numero
        self._historico = historico
        self._alergias = alergias

    def __str__(self):
        return (
            f"Número: {self._numero}\n"
            f"Histórico: {self._historico}\n"
            f"Alergias: {self._alergias}"
        )


class Paciente(Pessoa):
    def __init__(self, nome, cpf, nascimento, telefone,
                 endereco, demografia, prontuario):

        super().__init__(nome, cpf)

        self._nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
        self._telefone = telefone
        self._endereco = endereco
        self._demografia = demografia
        self._prontuario = prontuario

    def calcular_idade(self):
        hoje = datetime.now().year
        return hoje - self._nascimento.year

    def exibir_dados(self):
        return (
            f"\n=== PACIENTE ===\n"
            f"Nome: {self.nome}\n"
            f"CPF: {self.cpf}\n"
            f"Telefone: {self._telefone}\n"
            f"Idade: {self.calcular_idade()}\n"
            f"\nEndereço:\n{self._endereco}\n"
            f"\nDemografia:\n{self._demografia}\n"
            f"\nProntuário:\n{self._prontuario}"
        )

    def __str__(self):
        return self.nome


class ProfissionalSaude(Pessoa):
    def __init__(self, nome, cpf, registro, setor):
        super().__init__(nome, cpf)
        self._registro = registro
        self._setor = setor


class Medico(ProfissionalSaude):
    def __init__(self, nome, cpf, registro, setor, especialidade, crm):
        super().__init__(nome, cpf, registro, setor)
        self._especialidade = especialidade
        self._crm = crm

    def exibir_dados(self):
        return (
            f"\n=== MÉDICO ===\n"
            f"Nome: {self.nome}\n"
            f"Especialidade: {self._especialidade}\n"
            f"CRM: {self._crm}"
        )

    def __str__(self):
        return self.nome


class Enfermagem(ProfissionalSaude):
    def __init__(self, nome, cpf, registro, setor, coren):
        super().__init__(nome, cpf, registro, setor)
        self._coren = coren

    def exibir_dados(self):
        return (
            f"\n=== ENFERMAGEM ===\n"
            f"Nome: {self.nome}\n"
            f"COREN: {self._coren}"
        )

    def __str__(self):
        return self.nome
