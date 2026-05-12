

from datetime import datetime


def data_atual():
    return datetime.now().strftime("%d/%m/%Y")


def horario_atual():
    return datetime.now().strftime("%H:%M")


class Fila:
    def __init__(self, nome_fila, quantidade_pessoas=0):
        self._nome_fila = nome_fila
        self._setor = nome_fila
        self._quantidade_pessoas = quantidade_pessoas
        self._data = data_atual()
        self._horario = horario_atual()

    def adicionar_pessoa(self):
        self._quantidade_pessoas += 1

    def remover_pessoa(self):
        if self._quantidade_pessoas > 0:
            self._quantidade_pessoas -= 1

    def exibir_dados(self):
        return (
            f"\n========== FILA ==========\n"
            f"Nome da fila: {self._nome_fila}\n"
            f"Setor: {self._setor}\n"
            f"Quantidade de pessoas: {self._quantidade_pessoas}\n"
            f"Data: {self._data}\n"
            f"Horário: {self._horario}"
        )


class Senha:
    SETOR_PADRAO = "Recepção"

    def __init__(self, numero, tipo):
        self._numero = numero
        self._tipo = tipo
        self._horario_emissao = horario_atual()
        self._status = "Aguardando"
        self._setor = self.SETOR_PADRAO
        self._data = data_atual()

    def atualizar_status(self, novo_status):
        self._status = novo_status

    def exibir_dados(self):
        return (
            f"\n========== SENHA ==========\n"
            f"Número: {self._numero}\n"
            f"Tipo: {self._tipo}\n"
            f"Setor: {self._setor}\n"
            f"Status: {self._status}\n"
            f"Data: {self._data}\n"
            f"Horário: {self._horario_emissao}"
        )


class Triagem:
    SETOR_PADRAO = "Triagem"

    def __init__(self, paciente, pressao, temperatura, sintomas, prioridade):
        self._paciente = paciente
        self._pressao = pressao
        self._temperatura = temperatura
        self._sintomas = sintomas
        self._prioridade = prioridade
        self._setor = self.SETOR_PADRAO
        self._data = data_atual()
        self._horario = horario_atual()

    def exibir_dados(self):
        return (
            f"\n========== TRIAGEM ==========\n"
            f"Paciente: {self._paciente}\n"
            f"Pressão: {self._pressao}\n"
            f"Temperatura: {self._temperatura}\n"
            f"Sintomas: {self._sintomas}\n"
            f"Prioridade: {self._prioridade}\n"
            f"Setor: {self._setor}\n"
            f"Data: {self._data}\n"
            f"Horário: {self._horario}"
        )


class Agenda:
    SETOR_PADRAO = "Agendamento"

    def __init__(self, id_agenda, profissional_saude, paciente, data, horario):
        self._id = id_agenda
        self._profissional_saude = profissional_saude
        self._paciente = paciente
        self._data = data
        self._horario = horario
        self._status = "Agendado"
        self._setor = self.SETOR_PADRAO

    def atualizar_status(self, novo_status):
        self._status = novo_status

    def exibir_dados(self):
        return (
            f"\n========== AGENDA ==========\n"
            f"ID: {self._id}\n"
            f"Paciente: {self._paciente}\n"
            f"Profissional: {self._profissional_saude}\n"
            f"Status: {self._status}\n"
            f"Data: {self._data}\n"
            f"Horário: {self._horario}"
        )


class Conduta:
    SETOR_PADRAO = "Enfermagem"

    def __init__(self, descricao, observacoes, encaminhamento_necessario):
        self._descricao = descricao
        self._observacoes = observacoes
        self._encaminhamento_necessario = encaminhamento_necessario
        self._setor = self.SETOR_PADRAO
        self._data = data_atual()
        self._horario = horario_atual()

    def exibir_dados(self):
        encaminhamento = "Sim" if self._encaminhamento_necessario else "Não"

        return (
            f"\n========== CONDUTA ==========\n"
            f"Descrição: {self._descricao}\n"
            f"Observações: {self._observacoes}\n"
            f"Encaminhamento necessário: {encaminhamento}\n"
            f"Setor: {self._setor}\n"
            f"Data: {self._data}\n"
            f"Horário: {self._horario}"
        )