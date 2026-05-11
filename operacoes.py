from datetime import datetime


class Senha:
    contador = 0

    def __init__(self):
        Senha.contador += 1
        self.numero = Senha.contador
        self.data_hora = datetime.now()

    def exibir_senha(self):
        return (
            f"Senha Nº {self.numero} - "
            f"{self.data_hora.strftime('%d/%m/%Y %H:%M')}"
        )


class Fila:
    def __init__(self):
        self.pacientes = []

    def adicionar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def chamar_proximo(self):
        if self.pacientes:
            return self.pacientes.pop(0)

        return None

    def listar_fila(self):
        print("\n=== FILA ===")

        for paciente in self.pacientes:
            print(paciente.nome)


class Triagem:
    def __init__(self, paciente, pressao,
                 temperatura, sintomas, prioridade):

        self.paciente = paciente
        self.pressao = pressao
        self.temperatura = temperatura
        self.sintomas = sintomas
        self.prioridade = prioridade

    def exibir_triagem(self):
        return (
            f"\n=== TRIAGEM ===\n"
            f"Paciente: {self.paciente.nome}\n"
            f"Prioridade: {self.prioridade}"
        )


class Agenda:
    def __init__(self):
        self.consultas = []

    def agendar_consulta(self, consulta):
        self.consultas.append(consulta)

    def listar_agendamentos(self):
        print("\n=== AGENDAMENTOS ===")

        for consulta in self.consultas:
            print(
                f"{consulta.paciente.nome} - "
                f"{consulta.data} às {consulta.horario}"
            )
