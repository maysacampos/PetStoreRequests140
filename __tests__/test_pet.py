# 1- bibliotecas
import json             # leitor e escritor de json
import pytest           # engine
import requests         # framework

# 2- classe (opcional no Python)

# 2.1 - atribuições ou variaveis
# consulta e resultado esperado
pet_id = 129910301              # codigo do animal
pet_name = "Jade"               # nome do animal
pet_category_id = 1             # codigo categoria do animal
pet_category_name = "dog"       # titulo da categoria
pet_tag_id = 1                  # código do rótulo
pet_tag_name = "vacinado"       # titulo do rotulo
pet_status = "available"        # status do animal


# informações em comum
url = 'https://petstore.swagger.io/v2/pet'          # endereço
headers = { 'Content-Type': 'application/json' }    # formato dos dados trafegados


# 2.2 - funções / metodo

def test_post_pet():             #test_post_store e test_post_user
    # configura
    # dados de entrada estão no arquivo json
    pet=open('./fixtures/json/pet1.json')
    data=json.loads(pet.read())  # ler o conteudo 
    # dados de saida 

    # executa
    response = requests.post(                   # executo o método post com as informações a seguir
        url=url,                                # endereço
        headers=headers,                        # cabeçalho / informaçoes extras da mensagem
        data=json.dumps(data),                  # a mensagem = json
        timeout=5                               # tempo limite da transmissão, em segundos
    )

    # valida
    response_body = response.json()             # cria uma variavel e carrega a resposta em formato json

    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['category']['name'] == pet_category_name
    assert response_body['tags'][0]['name'] == pet_tag_name


  # test GET
    
def test_get_pet():
    # Configura
    # Dados de Entrada e Saída / Resultado Esperado estão na seção de atributos antes das funções

    # Executa
    response = requests.get(
        url=f'{url}/{pet_id}', # chama o endereço do get/consulta passando o código do animal
        headers=headers
        # não tem corpo da mensagem / body
    )

    # Valida
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['name'] == pet_name
    assert response_body['category']['id'] == pet_category_id
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['status'] == 'available'


