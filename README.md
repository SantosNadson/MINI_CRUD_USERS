# MINI_CRUD_USERS

---

## 🇸 ENGLISH

### About The Project

The project allows users to access a website to perform the following actions:

- Get registered users
- Register a new user
- Delete a user
- Update user's data

A simple and efficient CRUD application for user management with a web interface.

---

### Requirements

#### Technologies Used:

- **Database**: Microsoft SQL Server (Express - localhost)
- **Backend**: Python 3.14
- **Frontend**: HTML5, JavaScript, CSS

#### Dependencies:

All required frameworks are specified in the file `requirements.txt`

To install dependencies:
```bash
pip install -r requirements.txt
```

---

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SantosNadson/MINI_CRUD_USERS.git
   cd MINI_CRUD_USERS
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

### How to Use

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Open your browser and access:**
   ```
   http://localhost:8000
   ```

3. **Use the web interface to manage users**

---

### Project Structure

```
MINI_CRUD_USERS/
│
├── backend/             # Backend application
│   ├── main.py          # Application entry point
│   ├── routes.py        # Application routes
│   ├── services.py      # Business logic
│   └── __pycache__/     # Python cache
│
├── frontend/            # Frontend application
│   ├── static/          # Static files
│   │   └── script.js    # JavaScript functionality
│   │
│   └── templates/       # HTML templates
│       ├── home.html    # Home page
│       └── users.html   # Users management page
│
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

---

## 🇧🇷 PORTUGUÊS (PT-BR)

### Sobre o Projeto

O projeto permite aos usuários acessar um website para realizar as seguintes ações:

- Obter usuários registrados
- Registrar um novo usuário
- Deletar um usuário
- Atualizar dados do usuário

Uma aplicação CRUD simples e eficiente para gerenciamento de usuários com interface web.

---

### Requisitos

#### Tecnologias Utilizadas:

- **Banco de Dados**: Microsoft SQL Server (Express - localhost)
- **Backend**: Python 3.14
- **Frontend**: HTML5, JavaScript, CSS

#### Dependências:

Todos os frameworks necessários estão especificados no arquivo `requirements.txt`

Para instalar as dependências:
```bash
pip install -r requirements.txt
```

---

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/SantosNadson/MINI_CRUD_USERS.git
   cd MINI_CRUD_USERS
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

---

### Como Usar

1. **Execute a aplicação:**
   ```bash
   python main.py
   ```

2. **Abra seu navegador e acesse:**
   ```
   http://localhost:8000
   ```

3. **Use a interface web para gerenciar usuários**

---

### Estrutura do Projeto

```
MINI_CRUD_USERS/
│
├── backend/             # Aplicação backend
│   ├── main.py          # Ponto de entrada da aplicação
│   ├── routes.py        # Rotas da aplicação
│   ├── services.py      # Lógica de negócio
│   └── __pycache__/     # Cache do Python
│
├── frontend/            # Aplicação frontend
│   ├── static/          # Arquivos estáticos
│   │   └── script.js    # Funcionalidade JavaScript
│   │
│   └── templates/       # Templates HTML
│       ├── home.html    # Página inicial
│       └── users.html   # Página de gerenciamento de usuários
│
├── requirements.txt     # Dependências do projeto
└── README.md           # Este arquivo
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/`      | Home page |
| GET    | `/users` | Get all users |
| POST   | `/users` | Create a new user |
| PUT    | `/users/<id>` | Update user |
| DELETE | `/users/<id>` | Delete user |

---

## Author

**Nadson Santos**

- GitHub: [SantosNadson](https://github.com/SantosNadson)

---

## License

This project is open source and available under the MIT License.
