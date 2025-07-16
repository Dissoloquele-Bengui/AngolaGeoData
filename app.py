import requests
from bs4 import BeautifulSoup
import json
import re
import uuid

# Lista de IDs das províncias (1 a 18, 22 a 24)
province_ids = list(range(1, 19)) + list(range(22, 25))

# Lista para armazenar os dados das províncias
provinces_data = []

# Cabeçalhos para simular um navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

# Função para limpar texto e tratar valores nulos
def clean_text(text):
    text = text.strip() if text else ""
    return text if text and text != "Sem informação" and text != "-" else ""

# Função para normalizar nomes de províncias
def normalize_province_name(name):
    name = re.sub(r"^(Governador|Governadora)\s+da\s+Província\s+(do|de|da)?\s*", "", name, flags=re.IGNORECASE).strip()
    return name.upper()

# Função para extrair dados dos governadores
def scrape_governors():
    url = "https://governo.gov.ao/governador"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        governor_boxes = soup.find_all("div", class_="box_list")
        governors_data = {}
        for box in governor_boxes:
            province_elem = box.find("small")
            name_elem = box.find("b").find("a", class_="hover")
            date_elem = box.find(string=re.compile("Data de Nomeação:")).find_next("b")
            img_elem = box.find("figure").find("img")
            vice_gov_url = box.find("a", href=re.compile(r"/vice-governador/"))
            if province_elem and name_elem and date_elem and img_elem:
                province_name = normalize_province_name(province_elem.text)
                governor_name = clean_text(name_elem.text)
                governor_date = clean_text(date_elem.text)
                governor_img = clean_text(img_elem["src"])
                vice_gov_url = vice_gov_url["href"] if vice_gov_url else ""
                governors_data[province_name] = {
                    "vc_nome": governor_name,
                    "vc_data_nomeacao": governor_date,
                    "vc_imagem": governor_img,
                    "vice_gov_url": vice_gov_url
                }
        return governors_data
    except requests.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return {}
    except AttributeError as e:
        print(f"Erro ao parsear dados dos governadores: {e}")
        return {}

# Função para extrair datas de nomeação dos vice-governadores
def scrape_vice_governors_dates(vice_gov_url, province_name):
    if not vice_gov_url:
        return []
    try:
        full_url = vice_gov_url
        print(f"Acessando vice-governadores para data: {full_url}")
        response = requests.get(full_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        vice_governor_boxes = soup.find_all("div", class_="box_list")
        vice_governors_data = []
        for box in vice_governor_boxes:
            date_elem = box.find(string=re.compile("Data de Nomeação:")).find_next("b")
            print(f"Data: {date_elem.text if date_elem else 'N/A'}")
            if date_elem:
                vice_governors_data.append({
                    "vc_data_nomeacao": clean_text(date_elem.text)
                })
        return vice_governors_data
    except requests.RequestException as e:
        print(f"Erro ao acessar {full_url}: {e}")
        return []
    except AttributeError as e:
        print(f"Erro ao parsear dados dos vice-governadores de {province_name}: {e}")
        return []

# Função para extrair nomes, setores e imagens dos vice-governadores da página de detalhes
def scrape_vice_governors_names_sectors(soup, province_name):
    vice_gov_section = soup.find("h6", string=re.compile(r"Vice-Governadores", re.IGNORECASE))
    vice_governors_data = []
    if vice_gov_section:
        vice_gov_divs = vice_gov_section.find_parent("div", class_=re.compile(r"col-md-4")).find_all("div", class_="hover strip_list")
        print(f"Vice-Governadores para {province_name}: {len(vice_gov_divs)} encontrados")
        for div in vice_gov_divs:
            name_elem = div.find("b", style=re.compile(r"text-transform:\s*uppercase"))
            sector_elem = div.find("small")
            img_elem = div.find("figure").find("img") if div.find("figure") else None
            if name_elem and sector_elem:
                print(f"Nome: {name_elem.text}")
                print(f"Setor: {sector_elem.text}")
                print(f"Imagem: {img_elem['src'] if img_elem else 'N/A'}")
                vice_governors_data.append({
                    "vc_nome": clean_text(name_elem.text),
                    "vc_setor": clean_text(sector_elem.text.replace(f"Vice-Governador da Província de {province_name.lower()}", "").replace(f"Vice-Governadora da Província de {province_name.lower()}", "").strip()),
                    "vc_imagem": clean_text(img_elem["src"] if img_elem else "")
                })
    else:
        print(f"Seção 'Vice-Governadores' não encontrada para {province_name}")
    return vice_governors_data

# Extrair dados dos governadores
governors_data = scrape_governors()

# Iterar sobre os IDs das províncias
for province_id in province_ids:
    url = f"https://iapi.gov.ao/web/provincias-detalhes/{province_id}"
    try:
        # Fazer a requisição HTTP
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parsear o HTML com BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Encontrar o nome da província
        province_name_elem = soup.find("div", class_="titulo-secondary")
        vc_nome = clean_text(province_name_elem.find("h2").text) if province_name_elem else ""

        # Obter dados do governador
        governor_info = governors_data.get(vc_nome, {
            "vc_nome": "",
            "vc_data_nomeacao": "",
            "vc_imagem": "",
            "vice_gov_url": ""
        })
        vc_governador = {
            "vc_nome": governor_info["vc_nome"],
            "vc_data_nomeacao": governor_info["vc_data_nomeacao"],
            "vc_imagem": governor_info["vc_imagem"]
        }

        # Obter nomes, setores e imagens dos vice-governadores da página de detalhes
        vice_gov_names_sectors = scrape_vice_governors_names_sectors(soup, vc_nome)

        # Obter datas de nomeação dos vice-governadores
        vice_gov_dates = scrape_vice_governors_dates(governor_info["vice_gov_url"], vc_nome)

        # Combinar dados dos vice-governadores
        vc_vice_governadores = []
        for i, name_sector in enumerate(vice_gov_names_sectors):
            if i < len(vice_gov_dates):
                vc_vice_governadores.append({
                    "vc_nome": name_sector["vc_nome"],
                    "vc_setor": name_sector["vc_setor"],
                    "vc_data_nomeacao": vice_gov_dates[i]["vc_data_nomeacao"],
                    "vc_imagem": name_sector["vc_imagem"]
                })

        # Encontrar a tabela de municípios
        table = soup.find("table", id="table_id")
        municipalities = []
        if table:
            rows = table.find("tbody").find_all("tr")
            for row in rows:
                cols = row.find_all("td")
                if len(cols) >= 5:
                    vc_nome_municipio = clean_text(cols[0].find("b").text)
                    comunas_text = clean_text(cols[1].find("i").text if cols[1].find("i") else cols[1].text)
                    distritos_text = clean_text(cols[2].find("i").text if cols[2].find("i") else cols[2].text)
                    vc_data_fundacao = clean_text(cols[3].find("i").text if cols[3].find("i") else cols[3].text)
                    vc_administrador = clean_text(cols[4].find("i").text if cols[4].find("i") else cols[4].text)

                    # Processar comunas e distritos
                    vc_comunas = [c.strip() for c in comunas_text.split(",") if c.strip() and c.strip() != "Sem Comunas"]
                    vc_distritos = [d.strip() for d in distritos_text.split(",") if d.strip() and d.strip() != "Sem Distritos"]
                    it_numero_comunas = len(vc_comunas)
                    it_numero_distritos = len(vc_distritos)

                    municipalities.append({
                        "vc_nome": vc_nome_municipio,
                        "vc_comunas": vc_comunas,
                        "it_numero_comunas": it_numero_comunas,
                        "vc_distritos": vc_distritos,
                        "it_numero_distritos": it_numero_distritos,
                        "vc_data_fundacao": vc_data_fundacao,
                        "vc_administrador": vc_administrador
                    })

        # Encontrar informações adicionais
        info_section = soup.find("p", style=re.compile(r"background-color:\s*#FFC107"))
        vc_capital = vc_linguas = vc_densidade_populacional = vc_data_fundacao_provincia = vc_extensao = vc_etnias = ""
        it_numero_municipios = len(municipalities)
        if info_section:
            info_divs = info_section.find_next("div", class_="row").find_all("div", class_="col-md-3")
            print(f"Informações Adicionais para {vc_nome}: {len(info_divs)} divs encontradas")
            for div in info_divs:
                h6 = div.find("h6")
                b = div.find("b")
                if h6 and b:
                    value = clean_text(b.text)
                    print(f"{h6.text}: {value}")
                    if "Capital" in h6.text:
                        vc_capital = value
                    elif "Língua" in h6.text or "Linguas" in h6.text:
                        vc_linguas = value
                    elif "Densidade Populacional" in h6.text:
                        vc_densidade_populacional = value
                    elif "Data de Fundação" in h6.text:
                        vc_data_fundacao_provincia = value
                    elif "Extensão" in h6.text:
                        vc_extensao = value
                    elif "Etnia" in h6.text:
                        vc_etnias = value
                    elif "Nº de Munícipios" in h6.text:
                        it_numero_municipios = int(value) if value.isdigit() else it_numero_municipios
        else:
            print(f"Seção 'Informações Adicionais' não encontrada para {vc_nome}")

        # Adicionar os dados da província
        provinces_data.append({
            "it_id_provincia": province_id,
            "vc_nome": vc_nome,
            "vc_governador": vc_governador,
            "vc_vice_governadores": vc_vice_governadores,
            "vc_capital": vc_capital,
            "vc_linguas": vc_linguas,
            "vc_densidade_populacional": vc_densidade_populacional,
            "vc_data_fundacao_provincia": vc_data_fundacao_provincia,
            "vc_extensao": vc_extensao,
            "vc_etnias": vc_etnias,
            "it_numero_municipios": it_numero_municipios,
            "municipalities": municipalities
        })
        print(f"Extraído: {vc_nome} com {len(municipalities)} municípios")

    except requests.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
    except AttributeError as e:
        print(f"Erro ao parsear dados da província ID {province_id}: {e}")

# Gerar o arquivo JSON
with open("angola_municipios.json", "w", encoding="utf-8") as f:
    json.dump({"provinces": provinces_data}, f, ensure_ascii=False, indent=4)

# Gerar o arquivo PHP
php_output = []
for province in provinces_data:
    municipalities_str = "[\n" + ",\n".join([
        f"            ['vc_nome' => '{m['vc_nome']}', 'vc_comunas' => {json.dumps(m['vc_comunas'])}, 'it_numero_comunas' => {m['it_numero_comunas']}, 'vc_distritos' => {json.dumps(m['vc_distritos'])}, 'it_numero_distritos' => {m['it_numero_distritos']}, 'vc_data_fundacao' => '{m['vc_data_fundacao']}', 'vc_administrador' => '{m['vc_administrador']}']"
        for m in province['municipalities']
    ]) + "\n        ]"
    vice_governadores_str = "[\n" + ",\n".join([
        f"            ['vc_nome' => '{vg['vc_nome']}', 'vc_setor' => '{vg['vc_setor']}', 'vc_data_nomeacao' => '{vg['vc_data_nomeacao']}', 'vc_imagem' => '{vg['vc_imagem']}']"
        for vg in province['vc_vice_governadores']
    ]) + "\n        ]"
    governor_str = f"['vc_nome' => '{province['vc_governador']['vc_nome']}', 'vc_data_nomeacao' => '{province['vc_governador']['vc_data_nomeacao']}', 'vc_imagem' => '{province['vc_governador']['vc_imagem']}']"
    php_output.append(
        f"    [\n"
        f"        'it_id_provincia' => {province['it_id_provincia']},\n"
        f"        'vc_nome' => '{province['vc_nome']}',\n"
        f"        'vc_governador' => {governor_str},\n"
        f"        'vc_vice_governadores' => {vice_governadores_str},\n"
        f"        'vc_capital' => '{province['vc_capital']}',\n"
        f"        'vc_linguas' => '{province['vc_linguas']}',\n"
        f"        'vc_densidade_populacional' => '{province['vc_densidade_populacional']}',\n"
        f"        'vc_data_fundacao_provincia' => '{province['vc_data_fundacao_provincia']}',\n"
        f"        'vc_extensao' => '{province['vc_extensao']}',\n"
        f"        'vc_etnias' => '{province['vc_etnias']}',\n"
        f"        'it_numero_municipios' => {province['it_numero_municipios']},\n"
        f"        'municipalities' => {municipalities_str}\n"
        f"    ]"
    )
php_content = ",\n".join(php_output)

with open("angola_municipios.php", "w", encoding="utf-8") as f:
    f.write("<?php\n\n// Este arquivo é gerado automaticamente pelo script de scraping\n$provinces = [\n")
    f.write(php_content)
    f.write("\n];\n")

print("Scraping concluído. Dados salvos em angola_municipios.json e angola_municipios.php")