from abc import ABC, abstractmethod
from datetime import datetime


class Documento(ABC):
    def __init__(self, paciente, profissional):
        self.data = datetime.now()
        self.paciente = paciente
        self.profissional = profissional

    @abstractmethod
    def gerar_documento(self):
        pass


class Receita(Documento):
    def __init__(self, paciente, profissional,
                 medicamentos, posologia):

        super().__init__(paciente, profissional)

        self.medicamentos = medicamentos
        self.posologia = posologia

    def gerar_documento(self):
        return (
            f"\n=== RECEITA ===\n"
            f"Paciente: {self.paciente.nome}\n"
            f"Médico: {self.profissional.nome}\n"
            f"Medicamentos: {self.medicamentos}\n"
            f"Posologia: {self.posologia}"
        )


class Laudo(Documento):
    def __init__(self, paciente, profissional,
                 exame, resultado):

        super().__init__(paciente, profissional)

        self.exame = exame
        self.resultado = resultado

    def gerar_documento(self):
        return (
            f"\n=== LAUDO ===\n"
            f"Paciente: {self.paciente.nome}\n"
            f"Exame: {self.exame}\n"
            f"Resultado: {self.resultado}"
        )
