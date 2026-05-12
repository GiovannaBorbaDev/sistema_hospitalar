
from abc import ABC, abstractmethod


class Documento(ABC):
    def __init__(self, data, paciente, profissional):
        self._data = data
        self._paciente = paciente
        self._profissional = profissional

    @abstractmethod
    def exibir_documento(self):
        pass


class Encaminhamento(Documento):
    def __init__(self, data, paciente, profissional, destino, motivo):
        super().__init__(data, paciente, profissional)

        self._destino = destino
        self._motivo = motivo

    def exibir_documento(self):
        return (
            f"\n========== ENCAMINHAMENTO ==========\n"
            f"Data: {self._data}\n"
            f"Paciente: {self._paciente}\n"
            f"Profissional: {self._profissional}\n"
            f"Destino: {self._destino}\n"
            f"Motivo: {self._motivo}"
        )


class Receita(Documento):
    def __init__(self, data, paciente, profissional, medicamentos, posologia):
        super().__init__(data, paciente, profissional)

        self._medicamentos = medicamentos
        self._posologia = posologia

    def exibir_documento(self):
        return (
            f"\n========== RECEITA ==========\n"
            f"Data: {self._data}\n"
            f"Paciente: {self._paciente}\n"
            f"Profissional: {self._profissional}\n"
            f"Medicamentos: {self._medicamentos}\n"
            f"Posologia: {self._posologia}"
        )


class Laudo(Documento):
    def __init__(self, data, paciente, profissional, tipo_exame, resultado):
        super().__init__(data, paciente, profissional)

        self._tipo_exame = tipo_exame
        self._resultado = resultado

    def exibir_documento(self):
        return (
            f"\n========== LAUDO ==========\n"
            f"Data: {self._data}\n"
            f"Paciente: {self._paciente}\n"
            f"Profissional: {self._profissional}\n"
            f"Tipo de exame: {self._tipo_exame}\n"
            f"Resultado: {self._resultado}"
        )


class Declaracao(Documento):
    def __init__(self, data, paciente, profissional, finalidade, conteudo):
        super().__init__(data, paciente, profissional)

        self._finalidade = finalidade
        self._conteudo = conteudo

    def exibir_documento(self):
        return (
            f"\n========== DECLARAÇÃO ==========\n"
            f"Data: {self._data}\n"
            f"Paciente: {self._paciente}\n"
            f"Profissional: {self._profissional}\n"
            f"Finalidade: {self._finalidade}\n"
            f"Conteúdo: {self._conteudo}"
        )