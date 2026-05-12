
from pessoas import *
from atendimento import *
from operacoes import *
from documentos import *



# OBJETOS BASICOS

endereco = Endereco(
    "Rua A",
    123,
    "Centro",
    "São Paulo",
    "SP",
    "00000-000"
)

demografia = Demografia(
    20,
    "Feminino",
    "Solteira",
    "Superior",
    "Brasileira"
)

prontuario_ind = ProntuarioIndividual(
    101,
    "Saudavel",
    "Nenhuma",
    "Nenhum"
)

prontuario_fam = ProntuarioFamiliar(
    "Pais saudaveis",
    "Diabetes",
    "Acompanhar"
)

paciente = Paciente(
    "Giovanna",
    "523.456.789-00",
    "10/05/2005",
    "(11) 99078-5967",
    endereco,
    demografia,
    prontuario_ind,
    prontuario_fam
)

medico = Medico(
    "Dr. Carlos",
    "289.459.987-51",
    "123",
    "UTI",
    "Cardiologia",
    "CRM999"
)

enfermeira = Enfermagem(
    "Ana Ferreira",
    "245.678.985-26",
    "456",
    "UTI",
    "COREN123",
    "Enfermeira"
)

# EXIBIR DADOS


print(paciente.exibir_dados())
print(medico.exibir_dados())
print(enfermeira.exibir_dados())

# TRIAGEM


triagem = Triagem(
    paciente,
    "12x8",
    "36.5",
    "Dor no peito",
    "Alta"
)

print(triagem.exibir_dados())

# CONSULTA

consulta = Consulta(
    1,
    "11/05/2026",
    "14:00",
    paciente,
    medico,
    "Repouso e medicação",
    "Cardiologia",
    "Dor no peito"
)

print(consulta.exibir_detalhes())

# EXAME

exame = Exame(
    2,
    "11/05/2026",
    "15:00",
    paciente,
    enfermeira,
    "Aguardar resultado",
    "Exame de Sangue",
    "Jejum 8h"
)

print(exame.exibir_detalhes())

# FILA

fila = Fila("Triagem")

fila.adicionar_pessoa()
fila.adicionar_pessoa()

print(fila.exibir_dados())

# SENHA

senha = Senha(1, "Preferencial")

print(senha.exibir_dados())

# AGENDA

agenda = Agenda(
    1,
    medico,
    paciente,
    "12/05/2026",
    "09:00"
)

print(agenda.exibir_dados())

# DOCUMENTOS

receita = Receita(
    "11/05/2026",
    paciente,
    medico,
    "Dipirona",
    "1 comprimido a cada 8h"
)

print(receita.exibir_documento())

laudo = Laudo(
    "11/05/2026",
    paciente,
    medico,
    "Raio-X",
    "Sem alterações"
)

print(laudo.exibir_documento())