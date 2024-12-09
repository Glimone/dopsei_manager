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


def validate_number_process(value):
    pattern = 