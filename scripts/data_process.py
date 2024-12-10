import pandas as pd 
import re


def build_dataframe():
    columns = [
        "Número do Processo",
        "Lote",
        "Atribuição",
        "Interessado",
        "Entrada(Data)",
        "Status",
        "Assunto"
        ]
    return pd.DataFrame(columns=columns)

df = build_dataframe()


def validate_numero_processo(value):
    pattern = r'^\d{3}.\d{8}/\d{4}-\d{2}'
    
    return f"{bool(re.fullmatch(pattern, value)), {value}}"



value = input("Number process: ")
print(validate_numero_processo(value))

def validate_lote(value):
    pattern = r'^(L|LT|LOTE|LOT)\s?(\d{2})$'

    match = re.fullmatch(pattern, value, re.IGNORECASE)

    if match:
        return match.group(2)
    else:
        return None
    

v1 = input("Lote: ")
lote = validate_lote(v1)

if lote:
    lote = int(lote)
else:
    print("Lote inválido")
    Lote = None


def validate_atribuicao(lote):
    atribuition_map = {
        "Cirilo": [1, 16, 22, 28],
        "Luiz": [13, 21, 24, 25, 30],
        "Manuel": [6, 9, 11, 12, 19, 20, 31],
        "Thaís": [3, 7, 23, 27, 29],
    }

    try:
        lote_num = int(lote)
    except ValueError:
        return "Lote inválido"
    
    for tecnico, lotes in atribuition_map.items(): 
        if lote_num in lotes:
            return f"Técnico responsável: {tecnico}"
        
    return "Técnico indefinido"


print(validate_atribuicao(lote))
