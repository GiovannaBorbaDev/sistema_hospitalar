# =========================================================
# SISTEMA HOSPITALAR - APP.PY
# FRONT-END ORGANIZADO
# =========================================================

import streamlit as st
import pandas as pd
from pessoas import *
from atendimento import *
from operacoes import *
from documentos import *

# =========================================================
# CONFIGURAÇÃO
# =========================================================

st.set_page_config(
    page_title="Sistema Hospitalar",
    page_icon="🏥",
    layout="wide"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.main-title{
    background: linear-gradient(90deg,#0f172a,#1e3a8a);
    padding:20px;
    border-radius:15px;
    color:white;
    margin-bottom:25px;
}

.card{
    background:#111827;
    padding:20px;
    border-radius:15px;
    border:1px solid #374151;
    margin-bottom:15px;
}

.label{
    color:#60a5fa;
    font-weight:bold;
}

.value{
    color:white;
    margin-bottom:8px;
}

.section{
    color:#2563eb;
    font-size:28px;
    font-weight:bold;
    margin-top:20px;
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# IMPORTANDO DADOS DO MAIN
# =========================================================

from main import (
    paciente,
    medico,
    enfermeira,
    consulta,
    exame,
    fila,
    senha,
    agenda,
    receita,
    laudo,
    triagem
)

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="main-title">
    <h1>🏥 Sistema Hospitalar</h1>
    <p>Painel Administrativo Hospitalar</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# MENU
# =========================================================

pagina = st.sidebar.selectbox(
    "MENU",
    [
        "Dashboard",
        "Paciente",
        "Profissionais",
        "Triagem",
        "Consultas",
        "Exames",
        "Fila",
        "Documentos"
    ]
)

# =========================================================
# DASHBOARD
# =========================================================

if pagina == "Dashboard":

    st.markdown('<div class="section">Dashboard</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Pacientes", "1")

    with col2:
        st.metric("Médicos", "1")

    with col3:
        st.metric("Enfermagem", "1")

    with col4:
        st.metric("Fila Triagem", fila._quantidade_pessoas)

# =========================================================
# PACIENTE
# =========================================================

elif pagina == "Paciente":

    st.markdown('<div class="section">Paciente</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(f"""
        <div class="card">

        <div class="label">Nome</div>
        <div class="value">{paciente.nome}</div>

        <div class="label">CPF</div>
        <div class="value">{paciente.cpf}</div>

        <div class="label">Telefone</div>
        <div class="value">{paciente._telefone}</div>

        <div class="label">Idade</div>
        <div class="value">{paciente.calcular_idade()}</div>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div class="card">

        <div class="label">Endereço</div>
        <div class="value">{paciente._endereco}</div>

        <div class="label">Sexo</div>
        <div class="value">{paciente._demografia._sexo}</div>

        <div class="label">Estado Civil</div>
        <div class="value">{paciente._demografia._estado_civil}</div>

        <div class="label">Escolaridade</div>
        <div class="value">{paciente._demografia._escolaridade}</div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🩺 Prontuário")

    col3, col4 = st.columns(2)

    with col3:

        st.info(f"""
Histórico: {paciente._prontuario_ind._historico}

Alergias: {paciente._prontuario_ind._alergias}

Medicamentos: {paciente._prontuario_ind._medicamentos}
""")

    with col4:

        st.warning(f"""
Histórico Familiar: {paciente._prontuario_fam._historico}

Doenças: {paciente._prontuario_fam._doencas}

Observações: {paciente._prontuario_fam._observacoes}
""")

# =========================================================
# PROFISSIONAIS
# =========================================================

elif pagina == "Profissionais":

    st.markdown('<div class="section">Profissionais</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(f"""
        <div class="card">

        <h3>👨‍⚕️ Médico</h3>

        <div class="label">Nome</div>
        <div class="value">{medico.nome}</div>

        <div class="label">Especialidade</div>
        <div class="value">{medico._especialidade}</div>

        <div class="label">CRM</div>
        <div class="value">{medico._crm}</div>

        <div class="label">Setor</div>
        <div class="value">{medico._setor}</div>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div class="card">

        <h3>👩‍⚕️ Enfermagem</h3>

        <div class="label">Nome</div>
        <div class="value">{enfermeira.nome}</div>

        <div class="label">COREN</div>
        <div class="value">{enfermeira._coren}</div>

        <div class="label">Categoria</div>
        <div class="value">{enfermeira._categoria}</div>

        <div class="label">Setor</div>
        <div class="value">{enfermeira._setor}</div>

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# TRIAGEM
# =========================================================

elif pagina == "Triagem":

    st.markdown('<div class="section">Triagem</div>', unsafe_allow_html=True)

    st.success(f"""
Paciente: {triagem._paciente}

Pressão: {triagem._pressao}

Temperatura: {triagem._temperatura}

Sintomas: {triagem._sintomas}

Prioridade: {triagem._prioridade}
""")

# =========================================================
# CONSULTAS
# =========================================================

elif pagina == "Consultas":

    st.markdown('<div class="section">Consultas</div>', unsafe_allow_html=True)

    dados = {
        "Paciente": [consulta._paciente.nome],
        "Médico": [consulta._profissional_saude.nome],
        "Especialidade": [consulta._especialidade],
        "Motivo": [consulta._motivo],
        "Data": [consulta._data],
        "Horário": [consulta._horario]
    }

    df = pd.DataFrame(dados)

    st.dataframe(df, use_container_width=True)

# =========================================================
# EXAMES
# =========================================================

elif pagina == "Exames":

    st.markdown('<div class="section">Exames</div>', unsafe_allow_html=True)

    dados = {
        "Paciente": [exame._paciente.nome],
        "Profissional": [exame._profissional_saude.nome],
        "Exame": [exame._tipo_exame],
        "Preparo": [exame._preparo],
        "Conduta": [exame._conduta]
    }

    df = pd.DataFrame(dados)

    st.dataframe(df, use_container_width=True)

# =========================================================
# FILA
# =========================================================

elif pagina == "Fila":

    st.markdown('<div class="section">Fila</div>', unsafe_allow_html=True)

    st.metric(
        "Quantidade na fila",
        fila._quantidade_pessoas
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Adicionar Pessoa"):
            fila.adicionar_pessoa()
            st.rerun()

    with col2:

        if st.button("Remover Pessoa"):
            fila.remover_pessoa()
            st.rerun()

# =========================================================
# DOCUMENTOS
# =========================================================

elif pagina == "Documentos":

    st.markdown('<div class="section">Documentos</div>', unsafe_allow_html=True)

    aba1, aba2 = st.tabs(["Receita", "Laudo"])

    with aba1:

        st.info(f"""
Paciente: {receita._paciente}

Profissional: {receita._profissional}

Medicamentos: {receita._medicamentos}

Posologia: {receita._posologia}
""")

    with aba2:

        st.warning(f"""
Paciente: {laudo._paciente}

Profissional: {laudo._profissional}

Tipo Exame: {laudo._tipo_exame}

Resultado: {laudo._resultado}
""")