from datetime import datetime
from ftplib import FTP
from pprint import pprint
import re


conn = FTP("ftp.datasus.gov.br")
conn.login()
conn.set_pasv(False)
paths_sinan = [
    "/dissemin/publicos/sinan/dados/finais",
    "/dissemin/publicos/sinan/dados/prelim",
]


dict_sinan = {
    "ACBI": "Acidente de trabalho com material biológico",
    "ACGR": "Acidente de trabalho",
    "AIDA": "AIDS em adultos",
    "AIDC": "AIDS em crianças",
    "ANIM": "Acidente por Animais Peçonhentos",
    "ANTR": "Atendimento Antirrabico",
    "BOTU": "Botulismo",
    "CANC": "Cancêr relacionado ao trabalho",
    "CHAG": "Doença de Chagas Aguda",
    "CHIK": "Febre de Chikungunya",
    "COLE": "Cólera",
    "COQU": "Coqueluche",
    "DENG": "Dengue",
    "DERM": "Dermatoses ocupacionais",
    "DIFT": "Difteria",
    "ESPO": "Esporotricose (Epizootia)",
    "ESQU": "Esquistossomose",
    "EXAN": "Doença exantemáticas",
    "FMAC": "Febre Maculosa",
    "FTIF": "Febre Tifóide",
    "HANS": "Hanseníase",
    "HANT": "Hantavirose",
    "HEPA": "Hepatites Virais",
    "HIVA": "HIV em adultos",
    "HIVC": "HIV em crianças",
    "HIVE": "HIV em crianças expostas",
    "HIVG": "HIV em gestante",
    "IEXO": "Intoxicação Exógena",
    "INFL": "Influenza Pandêmica",
    "LEIV": "Leishmaniose Visceral",
    "LEPT": "Leptospirose",
    "LERD": "LER/Dort",
    "LTAN": "Leishmaniose Tegumentar Americana",
    "MALA": "Malária",
    "MENI": "Meningite",
    "MENT": "Transtornos mentais relacionados ao trabalho",
    "NTRA": "Notificação de Tracoma",
    "PAIR": "Perda auditiva por ruído relacionado ao trabalho",
    "PEST": "Peste",
    "PFAN": "Paralisia Flácida Aguda",
    "PNEU": "Pneumoconioses realacionadas ao trabalho",
    "RAIV": "Raiva",
    "ROTA": "Rotavírus",
    "SDTA": "Surto Doenças Transmitidas por Alimentos",
    "SIFA": "Sífilis Adquirida",
    "SIFC": "Sífilis Congênita",
    "SIFG": "Sífilis em Gestante",
    "SRC": "Síndrome da Rubéola Congênia",
    "TETA": "Tétano Acidental",
    "TETN": "Tétano Neonatal",
    "TOXC": "Toxoplasmose Congênita",
    "TOXG": "Toxoplasmose Gestacional",
    "TRAC": "Inquérito de Tracoma",
    "TUBE": "Tuberculose",
    "VARC": "Varicela",
    "VIOL": "Violência doméstica, sexual e ou outras violências",
    "ZIKA": "Zika Vírus",
}

filters = {
}

for opt in paths_sinan:
    conn.cwd(opt)
    for file_dbc in conn.nlst():
        if (date := re.search(r"\d{2,4}", file_dbc)) is not None:
            value_dt = datetime.strptime(date.group(), "%y").strftime("%Y")
            for prefix in dict_sinan:
                if prefix in file_dbc:
                    if dict_sinan[prefix] not in filters:
                        filters.update({
                            dict_sinan[prefix]: {
                                "Ano de Notificação": [],
                                "path_dbc": [],
                                "Unidade Federativa": [],
                                "Região": [],
                            }
                        })
                    else:
                        filters[dict_sinan[prefix]] \
                            ["Ano de Notificação"].append(value_dt)
                        filters[dict_sinan[prefix]] \
                            ["path_dbc"].append(f"{opt}/{file_dbc}")

pprint(filters)
