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


#Validação do número do processo:
def validate_numero_processo(value):
    pattern = r'^\d{3}.\d{8}/\d{4}-\d{2}'
    
    if re.fullmatch(pattern, value):
        return value
    else:
        return 'Invalid_Number'


#Validação do lote: 
def validate_lote(value):
    pattern = r'^(L|LT|LOTE|LOT)\s?(\d{2})$'

    match = re.fullmatch(pattern, value, re.IGNORECASE)

    if match:
        return match.group(2)
    else:
        return None
    



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
            return tecnico
        
    return None




def validate_interessado(value):
    if isinstance(value, str) and len(value) > 0:
        return value
    else:
        return 'Invalid_interesting'
    


def validate_data(value):
    pattern = r'^\d{2}/\d{2}/\d{4}$'
    if re.fullmatch(pattern, value):
        return value
    else:
        return 'Invalid_Data'
    

def validate_assunto(value):
    if isinstance(value, str) and len(value) > 0:
        return value
    else:
        return 'Invalid_assunto'
    
def validate_status(atribuido):
    if atribuido:
        return "Atribuido"
    else: 
        return "Atribuir"
   
api_data = [
    {
        "numero_processo": "123.12345678/2024-01",
        "lote": "lote 13",
        "interessado": "Rodovias das colinas",
        "data_entrada": "22/02/2024",
        "assunto": "PROGRAMAÇÃO DOS SERVIÇOS DE CONSERVAÇÃO DE ROTINA",
    },

    {
        "numero_processo": "234.12345678/2024-10",
        "lote": "l16",
        "interessado": "ViaOeste",
        "data_entrada": "10/06/2024",
        "assunto": "INSTALAÇÃO DE SINALIZADORES LUMINOSOS EM VEÍCULOS PRESTADORES DE SERVIÇOS, UTILIZADOS NAS ATIVIDADES DA ARTESP.",
    },

    {
        "numero_processo": "567.12345678/2024-36",
        "lote": "l14",
        "interessado": "Leonardo Hotta",
        "data_entrada": "11/02/2023",
        "assunto": "PROT.SIGA 621104,",
    },

]




# numero_processo = validate_numero_processo(input("Número: "))
# lote = validate_lote(input("Lote: "))
# data = validate_data(input("Data: "))

# if lote:
#     lote = int(lote)
# else:
#     print("Lote inválido")
#     Lote = None

# atribuido = validate_atribuicao(lote)
# interessado = validate_interessado(input("Interessado: "))
# assunto = validate_assunto(input("Assunto: "))
# status = validate_status(atribuido)
for processo in api_data:
    numero_processo = validate_numero_processo(processo["numero_processo"])
    lote = validate_lote(processo["lote"])
    if lote:
        lote = int(lote)
    else: 
        lote = "N/A"
    
    atribuido = validate_atribuicao(lote)
    interessado = validate_interessado(processo["interessado"])
    data = validate_data(processo["data_entrada"])
    status = validate_status(atribuido)
    assunto = validate_assunto(processo["assunto"])


    new_row = pd.DataFrame( [ {
        "Número do Processo": numero_processo,
        "Lote": lote,
        "Atribuição": atribuido,
        "Interessado": interessado,
        "Entrada(Data)": data,
        "Status": status,
        "Assunto": assunto,
    } ] )    
    df = pd.concat([new_row, df], ignore_index=True)


df.to_excel("SEI.xlsx", index=False)
