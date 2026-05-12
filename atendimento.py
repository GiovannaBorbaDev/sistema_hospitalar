
from abc import ABC, abstractmethod


class Atendimento(ABC):
    def __init__(self, codigo, data, horario, paciente, profissional_saude, conduta):
        self._codigo = codigo
        self._data = data
        self._horario = horario
        self._paciente = paciente
        self._profissional_saude = profissional_saude
        self._conduta = conduta

    @abstractmethod
    def exibir_detalhes(self):
        pass


class Consulta(Atendimento):
    def __init__(
        self,
        codigo,
        data,
        horario,
        paciente,
        profissional_saude,
        conduta,
        especialidade,
        motivo
    ):
        super().__init__(codigo, data, horario, paciente, profissional_saude, conduta)

        self._especialidade = especialidade
        self._motivo = motivo

    def exibir_detalhes(self):
        return (
            f"\n========== CONSULTA ==========\n"
            f"Código: {self._codigo}\n"
            f"Paciente: {self._paciente}\n"
            f"Médico: {self._profissional_saude}\n"
            f"Data: {self._data}\n"
            f"Horário: {self._horario}\n"
            f"Especialidade: {self._especialidade}\n"
            f"Motivo: {self._motivo}\n"
            f"Conduta: {self._conduta}"
        )


class Exame(Atendimento):
    def __init__(
        self,
        codigo,
        data,
        horario,
        paciente,
        profissional_saude,
        conduta,
        tipo_exame,
        preparo
    ):
        super().__init__(codigo, data, horario, paciente, profissional_saude, conduta)

        self._tipo_exame = tipo_exame
        self._preparo = preparo

    def exibir_detalhes(self):
        return (
            f"\n========== EXAME ==========\n"
            f"Código: {self._codigo}\n"
            f"Paciente: {self._paciente}\n"
            f"Profissional: {self._profissional_saude}\n"
            f"Tipo de exame: {self._tipo_exame}\n"
            f"Preparo: {self._preparo}\n"
            f"Conduta: {self._conduta}"
        )


class Cirurgia(Atendimento):
    def __init__(
        self,
        codigo,
        data,
        horario,
        paciente,
        profissional_saude,
        conduta,
        tipo_cirurgia,
        porte
    ):
        super().__init__(codigo, data, horario, paciente, profissional_saude, conduta)

        self._tipo_cirurgia = tipo_cirurgia
        self._porte = porte

    def exibir_detalhes(self):
        return (
            f"\n========== CIRURGIA ==========\n"
            f"Código: {self._codigo}\n"
            f"Paciente: {self._paciente}\n"
            f"Cirurgião: {self._profissional_saude}\n"
            f"Tipo de cirurgia: {self._tipo_cirurgia}\n"
            f"Porte: {self._porte}\n"
            f"Conduta: {self._conduta}"
        )


class Procedimento(Atendimento):
    def __init__(
        self,
        codigo,
        data,
        horario,
        paciente,
        profissional_saude,
        conduta,
        tipo_procedimento,
        descricao
    ):
        super().__init__(codigo, data, horario, paciente, profissional_saude, conduta)

        self._tipo_procedimento = tipo_procedimento
        self._descricao = descricao

    def exibir_detalhes(self):
        return (
            f"\n========== PROCEDIMENTO ==========\n"
            f"Código: {self._codigo}\n"
            f"Paciente: {self._paciente}\n"
            f"Profissional: {self._profissional_saude}\n"
            f"Tipo: {self._tipo_procedimento}\n"
            f"Descrição: {self._descricao}\n"
            f"Conduta: {self._conduta}"
        )