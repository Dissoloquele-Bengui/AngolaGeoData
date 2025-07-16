AngolaGeoData
Bem-vindo ao AngolaGeoData, um repositório dedicado a fornecer dados geográficos e político-administrativos atualizados de Angola. Este projeto foi criado para resolver a dificuldade enfrentada por desenvolvedores em acessar informações confiáveis sobre a divisão administrativa do país, incluindo províncias, municípios, governadores, vice-governadores, capitais, línguas, etnias e outras informações relevantes. Os dados são extraídos de sites governamentais oficiais e disponibilizados em formatos acessíveis (JSON e PHP) para facilitar a integração em aplicações e sistemas.
Motivação
Desenvolver aplicações que dependem de dados geográficos de Angola pode ser desafiador devido à falta de fontes centralizadas e acessíveis. Muitas vezes, desenvolvedores precisam recorrer a métodos manuais ou dados desatualizados. O AngolaGeoData aborda esse problema ao oferecer:

Dados estruturados e atualizados sobre a nova divisão político-administrativa de Angola.
Um script Python de web scraping para coletar informações diretamente de fontes oficiais, como governo.gov.ao e iapi.gov.ao.
Arquivos de saída em formatos amplamente utilizados (angola_municipios.json e angola_municipios.php) para integração em projetos web, mobile e outros sistemas.

Nosso objetivo é capacitar a comunidade de desenvolvedores angolanos e internacionais a criar soluções mais robustas e precisas, economizando tempo e esforço.
Funcionalidades

Dados Extraídos:
Províncias: Nome, ID, capital, línguas, densidade populacional, data de fundação, extensão territorial, etnias e número de municípios.
Governadores: Nome, data de nomeação e imagem.
Vice-Governadores: Nome, setor, data de nomeação e imagem.
Municípios: Nome, comunas, distritos, data de fundação e administrador.


Formatos de Saída:
angola_municipios.json: Dados estruturados em JSON para uso em qualquer linguagem de programação.
angola_municipios.php: Array PHP para integração direta em projetos Laravel, WordPress ou outros frameworks PHP.


Script de Scraping: Um script Python que extrai dados de sites governamentais, permitindo atualizações periódicas.

Como Usar
Pré-requisitos

Python 3.11 ou superior
Bibliotecas Python: requests, beautifulsoup4pip install requests beautifulsoup4



Instalação

Clone o repositório:git clone https://github.com/seu-usuario/AngolaGeoData.git
cd AngolaGeoData


Instale as dependências:pip install -r requirements.txt


Execute o script de scraping:python scrape_angola_municipios.py



Saídas

angola_municipios.json: Contém os dados completos de todas as províncias em formato JSON.
angola_municipios.php: Contém os dados em formato de array PHP, pronto para uso em projetos PHP.

Exemplo de Dados
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
        },
        ...
      ],
      "vc_capital": "Luena",
      "vc_linguas": "Português, Cokwe, Nganguela",
      "vc_densidade_populacional": "00",
      "vc_data_fundacao_provincia": "15-09-1917",
      "vc_extensao": "223.023 km²",
      "vc_etnias": "Ovanga",
      "it_numero_municipios": 12,
      "municipalities": [...]
    },
    ...
  ]
}

Como Contribuir
Quer ajudar a melhorar o AngolaGeoData? Contribuições são bem-vindas! Aqui estão algumas formas de contribuir:

Reportar Problemas: Abra uma issue para relatar erros no script ou dados incorretos.
Melhorar o Script: Envie pull requests com melhorias no código de scraping, como suporte a novas fontes ou otimização de performance.
Adicionar Documentação: Ajude a expandir este README com tutoriais ou exemplos de uso.
Criar APIs: Desenvolva APIs ou outros formatos de saída (ex.: CSV, SQL) para ampliar a usabilidade.

Passos para Contribuir

Faça um fork do repositório.
Crie uma branch para sua feature ou correção:git checkout -b minha-feature


Faça commit das suas alterações:git commit -m "Adiciona nova funcionalidade"


Envie para o repositório remoto:git push origin minha-feature


Abra um Pull Request.

Avisos

Uso Ético: Este script realiza web scraping em sites governamentais. Certifique-se de respeitar os termos de uso dos sites e evitar sobrecarga nos servidores (ex.: implementando delays entre requisições).
Atualização dos Dados: Os dados podem mudar com o tempo. Execute o script periodicamente para manter os arquivos angola_municipios.json e angola_municipios.php atualizados.
Conexão: Certifique-se de ter uma conexão estável com a internet, pois o script depende de acesso aos sites governo.gov.ao e iapi.gov.ao.

Licença
Este projeto está licenciado sob a MIT License. Sinta-se à vontade para usar, modificar e distribuir os dados e o código, desde que respeite os termos da licença.
Contato
Para sugestões, dúvidas ou suporte, abra uma issue no repositório ou entre em contato com seu-email@exemplo.com.

AngolaGeoData: Facilitando o acesso a informações geográficas de Angola para desenvolvedores de todo o mundo!