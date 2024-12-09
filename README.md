# fluxo-de-caixa



deve armazenar preço de produtos no estoque ao escolhe o produto deve armazenalo em um planilha 








estoque_software/
├── main.py             # Arquivo principal para execução
├── controllers/        # Lógica do negócio
│   ├── database.py     # Configuração e inicialização do banco de dados SQLite
│   ├── estoque.py      # Funções para manipular produtos e estoque
│   ├── planilha.py     # Funções para registrar transações
├── models/             # Estruturas de dados
│   └── produto.py      # Classe Produto
├── views/              # Interfaces (CLI ou GUI)
│   └── cli_view.py     # Interface de terminal para interação
├── data/               # Dados locais
│   └── estoque.db      # Banco de dados SQLite
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do sistema
