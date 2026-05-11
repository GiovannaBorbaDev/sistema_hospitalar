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


# =========================
# FILA
# =========================

class Fila:
    def __init__(self):
        self.pacientes = []

    def adicionar_paciente(self, paciente):
        self.pacientes.append(paciente)
        print(f"{paciente.nome} entrou na fila.")

    def chamar_proximo(self):
        if len(self.pacientes) > 0:
            paciente = self.pacientes.pop(0)

            print(f"Chamando paciente: {paciente.nome}")

            return paciente

        print("Fila vazia.")
        return None

    def listar_fila(self):
        print("\n=== FILA DE PACIENTES ===")

        if len(self.pacientes) == 0:
            print("Nenhum paciente na fila.")

        else:
            for i, paciente in enumerate(self.pacientes, start=1):
                print(f"{i} - {paciente.nome}")

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
            f"Pressão: {self.pressao}\n"
            f"Temperatura: {self.temperatura}°C\n"
            f"Sintomas: {self.sintomas}\n"
            f"Prioridade: {self.prioridade}"
        )


class Agenda:
    def __init__(self):
        self.consultas = []

    def agendar_consulta(self, consulta):
        self.consultas.append(consulta)

        print(
            f"Consulta agendada para "
            f"{consulta.paciente.nome} "
            f"com {consulta.profissional.nome} "
            f"em {consulta.data} às {consulta.horario}"
        )

    def listar_agendamentos(self):
        print("\n=== AGENDAMENTOS ===")

        if len(self.consultas) == 0:
            print("Nenhum agendamento.")

        else:
            for consulta in self.consultas:
                print(
                    f"Paciente: {consulta.paciente.nome} | "
                    f"Profissional: {consulta.profissional.nome} | "
                    f"Data: {consulta.data} | "
                    f"Horário: {consulta.horario}"
                )


class Conduta:
    def __init__(self, descricao, profissional):
        self.descricao = descricao
        self.profissional = profissional
        self.data = datetime.now()

    def exibir_conduta(self):
        return (
            f"\n=== CONDUTA ===\n"
            f"Profissional: {self.profissional.nome}\n"
            f"Data: {self.data.strftime('%d/%m/%Y %H:%M')}\n"
            f"Descrição: {self.descricao}"
        )


if __name__ == "__main__":

    from pessoas import Paciente, Medico
    from pessoas import Endereco
    from pessoas import Demografia
    from pessoas import ProntuarioIndividual

    from atendimento import Consulta

    endereco = Endereco(
        "Rua A",
        100,
        "Centro",
        "São Paulo",
        "SP",
        "00000-000"
    )

    demografia = Demografia(
        20,
        "Feminino",
        "Solteira"
    )

    prontuario = ProntuarioIndividual(
        1,
        "Sem doenças",
        "Nenhuma"
    )

    paciente = Paciente(
        "Giovanna",
        "123.456.789-00",
        "10/05/2005",
        "(11)99999-9999",
        endereco,
        demografia,
        prontuario
    )

    medico = Medico(
        "Dr. João",
        "987.654.321-00",
        "123",
        "Clínica",
        "Cardiologia",
        "CRM12345"
    )

    # SENHA
    senha = Senha()
    print(senha.exibir_senha())

    # FILA
    fila = Fila()

    fila.adicionar_paciente(paciente)

    fila.listar_fila()

    fila.chamar_proximo()

    # TRIAGEM
    triagem = Triagem(
        paciente,
        "12x8",
        36.5,
        "Dor de cabeça",
        "Média"
    )

    print(triagem.exibir_triagem())

    # CONSULTA
    consulta = Consulta(
        1,
        "15/05/2026",
        "14:00",
        paciente,
        medico,
        "Repouso",
        "Cardiologia",
        "Dor de cabeça"
    )

    agenda = Agenda()

    agenda.agendar_consulta(consulta)

    agenda.listar_agendamentos()


    conduta = Conduta(
        "Repouso e uso de medicação.",
        medico
    )

    print(conduta.exibir_conduta())
