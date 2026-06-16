# 🏥 Sistema Hospitalar de Gestão Integrada

## 📌 Sobre o Projeto

O **Sistema Hospitalar de Gestão Integrada** foi desenvolvido com o objetivo de otimizar e centralizar processos administrativos e operacionais de uma instituição de saúde. O sistema permite o gerenciamento de pacientes, profissionais da saúde, triagem, consultas, exames, filas de atendimento e documentos clínicos.

O projeto foi desenvolvido como atividade acadêmica, simulando uma **empresa de tecnologia voltada para a área da saúde**, com foco na organização hospitalar e melhoria da eficiência dos atendimentos.

---

## 🎯 Objetivo

Desenvolver uma solução tecnológica capaz de auxiliar hospitais e clínicas na gestão de informações, promovendo:

- Organização dos dados hospitalares
- Controle de pacientes e profissionais
- Gerenciamento de atendimentos
- Redução de processos manuais
- Melhor fluxo de atendimento

---

## ⚙️ Funcionalidades do Sistema

### 👤 Gestão de Pacientes
- Cadastro de pacientes
- Dados pessoais
- Endereço
- Demografia
- Prontuário individual
- Histórico familiar

### 👨‍⚕️ Gestão de Profissionais
- Cadastro de médicos
- Cadastro de enfermagem
- Controle por setor
- Especialidade médica
- Registro profissional (CRM/COREN)

### 🩺 Triagem Hospitalar
- Registro de sinais vitais
- Sintomas do paciente
- Prioridade do atendimento
- Organização do fluxo hospitalar

### 📅 Atendimentos
- Consultas
- Exames
- Cirurgias
- Procedimentos

### 📋 Operações Hospitalares
- Controle de filas
- Sistema de senhas
- Agenda médica

### 📄 Documentos Clínicos
- Receitas médicas
- Laudos médicos

---

## 🧠 Conceitos de POO Aplicados

O sistema foi desenvolvido utilizando **Programação Orientada a Objetos (POO)**.

### Abstração
Uso de classes abstratas:

- `Pessoa`
- `Atendimento`
- `Documento`

### Herança
Exemplos:

```python
Paciente → Pessoa
Medico → ProfissionalSaude
Enfermagem → ProfissionalSaude
Consulta → Atendimento
Exame → Atendimento
```

### Encapsulamento
Utilização de atributos privados:

```python
self._nome
self._cpf
self._telefone
```

### Polimorfismo
Métodos implementados de maneiras diferentes em várias classes:

```python
exibir_dados()
exibir_detalhes()
exibir_documento()
```

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Streamlit**
- **Pandas**
- **Plotly**
- **Programação Orientada a Objetos (POO)**

---

## 📂 Estrutura do Projeto

```text
Sistema_Hospitalar/
│
├── app.py              # Interface do sistema
├── pessoas.py          # Classes de pacientes e profissionais
├── atendimento.py      # Consultas, exames e procedimentos
├── operacoes.py        # Triagem, filas e agenda
├── documentos.py       # Receita e laudo
├── main.py             # Integração dos dados
└── README.md
```

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone LINK_DO_REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd Sistema_Hospitalar
```

### 3. Instale as dependências

```bash
pip install streamlit pandas plotly
```

### 4. Execute o sistema

```bash
streamlit run app.py
```

---

## 💡 Melhorias Futuras

- Banco de dados integrado
- Sistema de login
- Controle de permissões
- Exportação de relatórios PDF
- Dashboard analítico
- Histórico médico completo

---

## 👨‍💻 Desenvolvedores

Projeto acadêmico desenvolvido por:

- **Giovanna Borba**
- **(Adicionar integrantes)**

---

## 📚 Projeto Acadêmico

Este sistema foi desenvolvido para fins acadêmicos, aplicando conceitos de **Programação Orientada a Objetos**, arquitetura de software e gestão hospitalar.
