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
        return f'Número do lote: {match.group(2)}'
    else:
        return None
    

v1 = input("Lote: ")
print(validate_lote(v1))




