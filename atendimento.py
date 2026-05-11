from abc import ABC, abstractmethod


class Atendimento(ABC):
    def __init__(self, codigo, data, horario,
                 paciente, profissional, conduta):

        self.codigo = codigo
        self.data = data
        self.horario = horario
        self.paciente = paciente
        self.profissional = profissional
        self.conduta = conduta

    @abstractmethod
    def exibir_detalhes(self):
        pass


class Consulta(Atendimento):
    def __init__(self, codigo, data, horario,
                 paciente, profissional,
                 conduta, especialidade, motivo):

        super().__init__(
            codigo, data, horario,
            paciente, profissional, conduta
        )

        self.especialidade = especialidade
        self.motivo = motivo

    def exibir_detalhes(self):
        print(
            f"\n=== CONSULTA ===\n"
            f"Paciente: {self.paciente.nome}\n"
            f"Médico: {self.profissional.nome}\n"
            f"Especialidade: {self.especialidade}\n"
            f"Motivo: {self.motivo}"
        )


class Exame(Atendimento):
    def __init__(self, codigo, data, horario,
                 paciente, profissional,
                 conduta, tipo_exame):

        super().__init__(
            codigo, data, horario,
            paciente, profissional, conduta
        )

        self.tipo_exame = tipo_exame

    def exibir_detalhes(self):
        print(
            f"\n=== EXAME ===\n"
            f"Paciente: {self.paciente.nome}\n"
            f"Exame: {self.tipo_exame}"
        )
