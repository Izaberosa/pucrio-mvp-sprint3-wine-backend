from asyncore import loop
# import json
from urllib import response
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from urllib.parse import unquote
from numpy import indices
import requests
import pprint
import pandas
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from model.__init__ import db_url

from model import Session, Bebida, Model
from logger import logger
from schemas import *
from flask_cors import CORS



info = Info(title="HEART DISEASES", version="1.0.1")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
bebida_tag = Tag(name="Bebida", description="Adicao, visualizacao e remoção de pacientes a base de dados")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/bebida', tags=[bebida_tag],
          responses={"200": BebidaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def predict(form: BebidaSchema):
    """Adiciona um novo Bebida à base de dados

    Retorna uma representação dos pacientes.
    """
    # Carregando o modelo ML
    ml_path = 'ml_model/KNN.pkl'
    modelo = Model.carrega_modelo(ml_path)

    bebida = Bebida(
        fixed_acidity = form.fixed_acidity,
        volatile_acidity = form.volatile_acidity,
        citric_acid = form.citric_acid,
        residual_sugar = form.residual_sugar,
        chlorides = form.chlorides,
        free_sulfurdioxide = form.free_sulfurdioxide,
        total_sulfurdioxide = form.total_sulfurdioxide,
        density = form.density,
        pH = form.pH,
        sulphates = form.sulphates,
        alcohol = form.alcohol,
        quality = Model.preditor(modelo, form))
    
    logger.debug(f"Adicionando paciente de nome: '{bebida.fixed_acidity}'")
    
    try:
        # criando conexão com o banco
        session = Session()
        # adicionando bebida
        session.add(bebida)
        # efetivando o comando de adição de novo bebida na tabela
        session.commit()
        logger.debug(f"Adicionado bebida de nome: '{bebida.fixed_acidity}'")
        return apresenta_bebida(bebida), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Esse bebida ja existe no banco :/"
        logger.warning(f"Erro ao adicionar o bebida '{bebida.fixed_acidity}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "O bebida não foi salvo no banco :/"
        logger.warning(f"Erro ao adicionar o bebida '{bebida.fixed_acidity}', {error_msg}")
        return {"mesage": error_msg}, 400
    

@app.delete('/bebida', tags=[bebida_tag],
            responses={"200": BebidaDelSchema, "404": ErrorSchema})
def del_bebida(query: BebidaDelSchema):
    """Deleta um bebida a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    bebida_id = (query.nome)
    print(bebida_id)
    logger.debug(f"Deletando dados sobre bebida #{bebida_id}")
    # criando conexão com o banco
    session = Session()
    # fazendo a remoção
    count = session.query(Bebida).filter(Bebida.fixed_acidity == bebida_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletando paciente #{bebida_id}")
        return {"mesage": "Bebida foi removida", "id": bebida_id}
    else:
        # se o paciente não foi encontrado
        error_msg = "Bebida não foi encontrado no banco :/"
        logger.warning(f"Erro ao deletar o bebida #'{bebida_id}', {error_msg}")
        return {"mesage": error_msg}, 404

    

@app.get('/bebida', tags=[bebida_tag],
         responses={"200": ListagemBebidaSchema, "404": ErrorSchema})
def get_bebida():
    """Faz a busca por todos os bebidas cadastrados no banco de dados.

    Retorna uma representação da lista de bebidas.
    """
    
    logger.debug(f"Coletando bebidas ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    bebidas = session.query(Bebida).order_by(Bebida.id.asc()).all()

    if not bebidas:
        # se não há bebidas cadastrados
        return {"bebidas": []}, 200
    else:
        logger.debug(f"%d bebidas encontrados" % len(bebidas))
        # retorna a representação do paciente
        print(bebidas)
        return apresenta_bebidas(bebidas), 200