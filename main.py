from pessoas import *
from atendimento import *
from operacoes import *
from documentos import *


endereco = Endereco(
    "Rua A", 100,
    "Centro", "São Paulo",
    "SP", "00000-000"
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
    "Dr. Carlos",
    "987.654.321-00",
    "123",
    "Clínica",
    "Cardiologia",
    "CRM12345"
)

print(paciente.exibir_dados())
print(medico.exibir_dados())


senha = Senha()
print(senha.exibir_senha())


fila = Fila()
fila.adicionar_paciente(paciente)
fila.listar_fila()


consulta = Consulta(
    1,
    "11/05/2026",
    "14:00",
    paciente,
    medico,
    "Repouso",
    "Cardiologia",
    "Dor no peito"
)

consulta.exibir_detalhes()


agenda = Agenda()
agenda.agendar_consulta(consulta)
agenda.listar_agendamentos()


receita = Receita(
    paciente,
    medico,
    "Dipirona",
    "1 comprimido a cada 8h"
)

print(receita.gerar_documento())
