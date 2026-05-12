
from abc import ABC, abstractmethod
from datetime import datetime

# CLASSE PESSOA

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



# ENDEREÇO

class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado, cep):
        self._rua = rua
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade
        self._estado = estado
        self._cep = cep

    def __str__(self):
        return f"{self._rua}, {self._numero} - {self._bairro}, {self._cidade}/{self._estado} - CEP: {self._cep}"


# DEMOGRAFIA

class Demografia:
    def __init__(self, idade, sexo, estado_civil, escolaridade, nacionalidade):
        self._idade = idade
        self._sexo = sexo
        self._estado_civil = estado_civil
        self._escolaridade = escolaridade
        self._nacionalidade = nacionalidade

    def __str__(self):
        return (
            f"Idade: {self._idade}\n"
            f"Sexo: {self._sexo}\n"
            f"Estado Civil: {self._estado_civil}\n"
            f"Escolaridade: {self._escolaridade}\n"
            f"Nacionalidade: {self._nacionalidade}"
        )



# PRONTUÁRIOS

class ProntuarioIndividual:
    def __init__(self, numero, historico, alergias, medicamentos):
        self._numero = numero
        self._historico = historico
        self._alergias = alergias
        self._medicamentos = medicamentos

    def __str__(self):
        return (
            f"Nº: {self._numero}\n"
            f"Histórico: {self._historico}\n"
            f"Alergias: {self._alergias}\n"
            f"Medicamentos: {self._medicamentos}"
        )


class ProntuarioFamiliar:
    def __init__(self, historico, doencas, observacoes):
        self._historico = historico
        self._doencas = doencas
        self._observacoes = observacoes

    def __str__(self):
        return (
            f"Histórico Familiar: {self._historico}\n"
            f"Doenças Hereditárias: {self._doencas}\n"
            f"Observações: {self._observacoes}"
        )



# PACIENTE

class Paciente(Pessoa):
    def __init__(
        self,
        nome,
        cpf,
        data_nascimento,
        telefone,
        endereco,
        demografia,
        prontuario_ind,
        prontuario_fam
    ):
        super().__init__(nome, cpf)

        self._data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        self._telefone = telefone
        self._endereco = endereco
        self._demografia = demografia
        self._prontuario_ind = prontuario_ind
        self._prontuario_fam = prontuario_fam

    def calcular_idade(self):
        hoje = datetime.now().date()
        nasc = self._data_nascimento.date()

        idade = hoje.year - nasc.year

        if (hoje.month, hoje.day) < (nasc.month, nasc.day):
            idade -= 1

        return idade

    def exibir_dados(self):
        return (
            f"\nPACIENTE\n"
            f"Nome: {self.nome}\n"
            f"CPF: {self.cpf}\n"
            f"Telefone: {self._telefone}\n"
            f"Idade: {self.calcular_idade()}\n\n"
            f"--- Endereço ---\n{self._endereco}\n\n"
            f"--- Demografia ---\n{self._demografia}\n\n"
            f"--- Prontuário Individual ---\n{self._prontuario_ind}\n\n"
            f"--- Prontuário Familiar ---\n{self._prontuario_fam}"
        )

    def __str__(self):
        return self.nome



# PROFISSIONAIS

class ProfissionalSaude(Pessoa):
    def __init__(self, nome, cpf, registro, setor):
        super().__init__(nome, cpf)

        self._registro = registro
        self._setor = setor

    def alterar_setor(self, novo_setor):
        self._setor = novo_setor


class Medico(ProfissionalSaude):
    def __init__(self, nome, cpf, registro, setor, especialidade, crm):
        super().__init__(nome, cpf, registro, setor)

        self._especialidade = especialidade
        self._crm = crm

    def exibir_dados(self):
        return (
            f"\nMÉDICO\n"
            f"Nome: {self.nome}\n"
            f"CPF: {self.cpf}\n"
            f"Registro: {self._registro}\n"
            f"Setor: {self._setor}\n"
            f"Especialidade: {self._especialidade}\n"
            f"CRM: {self._crm}"
        )

    def atender_paciente(self, paciente):
        return f"{self.nome} atendeu {paciente.nome}"

    def __str__(self):
        return self.nome


class Enfermagem(ProfissionalSaude):
    def __init__(self, nome, cpf, registro, setor, coren, categoria):
        super().__init__(nome, cpf, registro, setor)

        self._coren = coren
        self._categoria = categoria

    def exibir_dados(self):
        return (
            f"\nENFERMAGEM\n"
            f"Nome: {self.nome}\n"
            f"CPF: {self.cpf}\n"
            f"Registro: {self._registro}\n"
            f"Setor: {self._setor}\n"
            f"COREN: {self._coren}\n"
            f"Categoria: {self._categoria}"
        )

    def administrar_medicacao(self, paciente, medicamento):
        return f"{self.nome} administrou {medicamento} em {paciente.nome}"

    def __str__(self):
        return self.nome