# 1- bibliotecas
import json             # leitor e escritor de json
import pytest           # engine
import requests         # framework

# 2- classe (opcional no Python)

# 2.1 - atribuições ou variáveis
user_id = 129910301             
user_username = "maysacampos"               
user_firstName = "maysa"             
user_lastName = "campos"       
user_email = "maysacampos@hotmail.com"                 
user_password = "teste123"   
user_phone = "988012245"
user_userStatus = 1   

# informações em comum
url = "https://petstore.swagger.io/v2/user"            
headers = { "Content-Type": "application/json" } 

# 2.2 - funções / métodos

def test_post_user():
    # configura
    # dados de entrada estão no arquivo json
    user = open("./fixtures/json/user1.json")  
    data = json.loads(user.read()) 

  # executa
    response = requests.post(                   # executo o método post com as informações a seguir
        url=url,                                # endereço
        headers=headers,                        # cabeçalho / informaçoes extras da mensagem
        data=json.dumps(data),                  # a mensagem = json
        timeout=5                               # tempo limite da transmissão, em segundos
    )
    
    response_body = response.json() 
    response_body = response.json()  # Mova essa linha para cima
    assert response.status_code == 200
    assert response_body["code"] == 200  
    assert response_body["type"] == "unknown"
    assert response_body["message"] == str(user_id)

def test_get_user():
    
    response = requests.get(
        url = f"{url}/{user_username}",  
        headers = headers
    )
    
    response_body = response.json()    
    assert response.status_code == 200
    assert response_body["id"] == user_id
    assert response_body["username"] == user_username
    assert response_body["firstName"] == user_firstName
    assert response_body["lastName"] == user_lastName
    assert response_body["email"] == user_email
    assert response_body["password"] == user_password
    assert response_body["phone"] == user_phone
    assert response_body["userStatus"] == user_userStatus

def test_put_user():
    
    user = open("./fixtures/json/user2.json")
    data = json.loads(user.read())    
   
    response = requests.put(
        url = f"{url}/{user_username}",
        headers = headers,
        data = json.dumps(data),
        timeout = 5
    )
   
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["code"] == 200
    assert response_body["type"] == "unknown"
    assert response_body["message"] == str(user_id)   

def test_delete_user():
    
    response = requests.delete(
        url = f"{url}/{user_username}",
        headers = headers
    )
    
    response_body = response.json()
    
    assert response.status_code == 200   
    assert response_body["code"] == 200  
    assert response_body["type"] == "unknown"
    assert response_body["message"] == str(user_username)

