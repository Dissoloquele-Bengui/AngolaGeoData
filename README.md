# 🇦🇴 AngolaGeoData

Bem-vindo ao **AngolaGeoData**, um repositório dedicado a fornecer **dados geográficos e político-administrativos atualizados de Angola**.

Este projeto foi criado para resolver a dificuldade enfrentada por desenvolvedores em acessar informações confiáveis sobre a divisão administrativa do país, incluindo:

- Províncias
- Municípios
- Governadores
- Vice-Governadores
- Capitais
- Línguas
- Etnias
- E outras informações relevantes

Os dados são extraídos de sites governamentais oficiais e disponibilizados em **formatos acessíveis (JSON e PHP)** para facilitar a integração em aplicações e sistemas.

---

## 🎯 Motivação

Desenvolver aplicações que dependem de dados geográficos de Angola pode ser desafiador devido à falta de fontes centralizadas e acessíveis. Muitas vezes, desenvolvedores precisam recorrer a métodos manuais ou dados desatualizados.

O **AngolaGeoData** resolve esse problema ao oferecer:

- ✅ Dados estruturados e atualizados sobre a nova divisão político-administrativa de Angola
- 🐍 Um script Python de web scraping para coletar informações diretamente de fontes oficiais (ex: `governo.gov.ao`, `iapi.gov.ao`)
- 📁 Arquivos de saída em formatos amplamente utilizados: `angola_municipios.json` e `angola_municipios.php`

O meu objetivo é **capacitar a comunidade de desenvolvedores angolanos e internacionais** a criar soluções mais robustas e precisas, economizando tempo e esforço.

---

## ⚙️ Funcionalidades

### 📊 Dados Extraídos:

- **Províncias**:
  - Nome, ID, capital
  - Línguas, densidade populacional, data de fundação, extensão territorial, etnias
  - Número de municípios

- **Governadores**:
  - Nome, data de nomeação, imagem

- **Vice-Governadores**:
  - Nome, setor, data de nomeação, imagem

- **Municípios**:
  - Nome, comunas, distritos, data de fundação, administrador

### 🗃️ Formatos de Saída:

- `angola_municipios.json`: Dados estruturados em JSON para uso em qualquer linguagem
- `angola_municipios.php`: Array PHP para integração com Laravel, WordPress ou outros frameworks PHP

### 🧠 Script de Scraping:

- Um script Python que extrai dados de sites governamentais
- Pode ser executado periodicamente para manter os dados atualizados

---

## 🚀 Como Usar

### 📌 Pré-requisitos

- Python 3.11 ou superior
- Bibliotecas Python:
  
```bash
pip install requests beautifulsoup4
````

---

### 📥 Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/AngolaGeoData.git
cd AngolaGeoData

# Instale as dependências
pip install -r requirements.txt

# Execute o script de scraping
python app.py
```

---

### 📤 Saídas

* `angola_municipios.json`: Contém os dados completos de todas as províncias em formato JSON
* `angola_municipios.php`: Contém os dados em array PHP, pronto para uso

---

## 🧾 Exemplo de Dados

```json
{
  "provinces": [
    {
      "it_id_provincia": 15,
      "vc_nome": "MOXICO",
      "vc_governador": {
        "vc_nome": "Ernesto Muangala",
        "vc_data_nomeacao": "11/10/2022",
        "vc_imagem": "https://plataformacipra.gov.ao/..."
      },
      "vc_vice_governadores": [
        {
          "vc_nome": "Wilson Agnelo Chinhama Augusto",
          "vc_setor": "Serviços Técnicos e Infra-estruturas",
          "vc_data_nomeacao": "11/10/2022",
          "vc_imagem": "https://sys.portais.gov.ao/..."
        }
      ],
      "vc_capital": "Luena",
      "vc_linguas": "Português, Cokwe, Nganguela",
      "vc_densidade_populacional": "00",
      "vc_data_fundacao_provincia": "15-09-1917",
      "vc_extensao": "223.023 km²",
      "vc_etnias": "Ovanga",
      "it_numero_municipios": 12,
      "municipalities": [...]
    }
  ]
}
```

---

## 🤝 Como Contribuir

Contribuições são bem-vindas! Aqui estão algumas formas de ajudar:

* 🐞 **Reportar problemas**: Abra uma *issue* para relatar erros ou dados incorretos
* 💡 **Melhorar o script**: Envie *pull requests* com suporte a novas fontes ou melhorias de performance
* 📚 **Adicionar documentação**: Expanda este README com tutoriais ou exemplos de uso
* 🔌 **Criar APIs**: Desenvolva APIs ou outros formatos de saída (ex.: CSV, SQL)

### ✅ Passos para Contribuir

```bash
# Faça um fork do repositório
git checkout -b minha-feature

# Faça commit das alterações
git commit -m "Adiciona nova funcionalidade"

# Envie para o seu fork
git push origin minha-feature
```

Depois, abra um **Pull Request** explicando suas mudanças!

---

## ⚠️ Avisos

* ⚖️ **Uso Ético**: Este script realiza scraping de sites governamentais. Respeite os termos de uso e implemente `delays` entre as requisições.
* 🔄 **Atualização dos dados**: Execute o script periodicamente para manter os arquivos `angola_municipios.json` e `angola_municipios.php` atualizados.
* 🌐 **Conexão ativa**: Certifique-se de ter uma boa conexão, já que o script depende dos sites `governo.gov.ao` e `iapi.gov.ao`.

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**. Você pode usar, modificar e distribuir o código, desde que mantenha os créditos.

---

## 📬 Contato

Para sugestões, dúvidas ou suporte, abra uma *issue* neste repositório ou entre em contato via e-mail:

📧 **[dissoloquelebengui67@gmail.com](mailto:dissoloquelebengui67@gmail.com)**

---

> **AngolaGeoData**: Facilitando o acesso a informações geográficas de Angola para desenvolvedores de todo o mundo!
