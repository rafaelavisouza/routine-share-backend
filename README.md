# Sistema de Gestão de Rotinas Compartilhadas

Este repositório contém o backend do projeto final para o curso **CEPEDI - Bolsa Futuro Digital**. O site é uma aplicação voltada para a gamificação de rotinas, permitindo que amigos criem grupos, acompanhem o progresso uns dos outros e disputem rankings, inspirado no conceito de "Gym Rats".

---

## 📌 Sobre o Projeto
O objetivo principal é transformar a disciplina individual em uma experiência social e competitiva. Os usuários podem cadastrar tarefas diárias, ganhar pontos ao completá-las e visualizar sua posição em rankings globais e de grupos específicos.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Framework:** Django / FastAPI (definir o escolhido)
* **Banco de Dados:** PostgreSQL / SQLite
* **Autenticação:** JWT (JSON Web Tokens)
* **Documentação:** Swagger / Redoc

## 📂 Estrutura da Aplicação (Endpoints & Regras de Negócio)

O site foi desenhada para suportar as seguintes funcionalidades:

### 🔐 Autenticação e Usuário
* **Login/Cadastro:** Fluxo completo de criação de conta com validação de dados (Email, Senha, Telefone, Endereço).
* **Perfil:** Gerenciamento de dados pessoais e visualização de estatísticas individuais.

### 🏠 Dashboard e Ranking
* Cálculo de performance diária.
* Geração de rankings dinâmicos: **Pessoal, Por Grupo e Geral**.

### 👥 Grupos
* Criação e gerenciamento de grupos de amigos.
* Listagem de membros e integração social.

### ✅ Rotinas e Metas
* **CRUD de Tarefas:** Criação de rotinas com categorias, frequências e pesos de pontuação.
* **Check-in:** Sistema de validação de conclusão de tarefas para atribuição de pontos.

---

## 🗂️ Organização do Sistema (Sitemap do Backend)

O backend fornece suporte para as seguintes interfaces:

1.  **Auth:** `POST /auth/register`, `POST /auth/login`
2.  **User:** `GET /user/profile`, `PUT /user/edit`
3.  **Dashboard:** `GET /dashboard/stats`
4.  **Groups:** `GET /groups`, `POST /groups/create`, `GET /groups/{id}`
5.  **Routines:** `GET /routines`, `POST /routines`, `PATCH /routines/{id}/complete`
6.  **Goals:** `GET /goals`, `POST /goals`

---

Desenvolvedores

Rafaela Vitoria Marques Souza - @rafaelavisoouza

Ivana Nolasco dos Santos - @NDSIVANA

Vinicius Brito de Oliveira - @VnncsB


Este projeto foi desenvolvido como requisito para a conclusão do módulo de Backend do programa Bolsa Futuro Digital - CEPEDI.
