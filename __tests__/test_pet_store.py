# 1- bibliotecas
import json             # leitor e escritor de json
import pytest           # engine
import requests         # framework
from datetime import datetime 

# 2- classe (opcional no Python)

# 2.1 - atribuições ou variaveis
# consulta e resultado esperado
store_id = 1                                       # n do pedido
store_petId = 450                          # n do pet
store_quantity = 1                                 # quantidade do pet
store_shipDate = "2024-06-07T14:01:53.199+0000"       # data de envio            
store_status = "placed"                            # situacao do pedido
store_complete = True                            # se foi concluido

def normalize_date(date_str):
    """Converte a data do formato +0000 para o formato Z."""
    if date_str.endswith('+0000'):
        return date_str[:-5] + 'Z'
    return date_str

# informações em comum
url = "https://petstore.swagger.io/v2/store"            
headers = { "Content-Type": "application/json" } 

def test_post_store():
    # configura
    # dados de entrada estão no arquivo json
    store = open("./fixtures/json/store.json")  
    data = json.loads(store.read())  

  # executa
    response = requests.post(           
        url = f"{url}/order",                      
        headers = headers,              
        data = json.dumps(data),        
        timeout = 5                    
    )

    # valida
    response_body = response.json()             # cria uma variavel e carrega a resposta em formato json
    
    assert response.status_code == 200
    assert response_body["id"] == store_id
    assert response_body["petId"] == store_petId
    assert response_body["quantity"] == store_quantity
    assert response_body["shipDate"] == store_shipDate
    assert response_body["status"] == store_status
    assert response_body["complete"] == store_complete 
   
def test_get_store():
    
    response = requests.get(
        url = f"{url}/order/{store_id}", 
        headers = headers 
    )
    
    response_body = response.json()
    
    assert response.status_code == 200
    assert response_body["id"] == store_id
    assert response_body["petId"] == store_petId
    assert response_body["quantity"] == store_quantity
    assert response_body["shipDate"] == store_shipDate
    assert response_body["status"] == store_status
    assert response_body["complete"] == store_complete 
    
    
def test_delete_store():
    
    response = requests.delete(
        url = f"{url}/order/{store_id}",   
        headers = headers
    )
    
    response_body = response.json()
    
    assert response.status_code == 200   
    assert response_body["code"] == 200  
    assert response_body["type"] == "unknown"
    assert response_body["message"] == str(store_id)
   





