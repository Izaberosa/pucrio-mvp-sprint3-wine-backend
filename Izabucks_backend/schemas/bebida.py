from typing import List
from pydantic import BaseModel
# import json
# from sqlalchemy import values
from model.bebida import Bebida
# import numpy as np
# import re


class BebidaSchema(BaseModel):
    """ Define como modelo padrao caso nao seja inserido um novo usuario.
    """
    # id: int = 1
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float 
    residual_sugar: float 
    chlorides: float 
    free_sulfurdioxide: float 
    total_sulfurdioxide: float 
    density: float 
    pH: float 
    sulphates: float 
    alcohol: float 
    
    
class BebidaBuscaSchema(BaseModel):
    """ Define a estrutura de pesquisa(busca) deve ser representada. Que será
        feita apenas com base no id do paciente.
    """
    id: int


class ListagemBebidaSchema(BaseModel):
    """ Define como uma listagem de pacientes será retornada.
    """
    bebidas:List[BebidaSchema]


def apresenta_bebidas(bebidas: List[Bebida]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteSchema.
    """
    result = []
    for bebida in bebidas:   
        result.append({
            "id": bebida.id,
            "fixed_acidity": bebida.fixed_acidity,
            "volatile_acidity": bebida.volatile_acidity,
            "citric_acid": bebida.citric_acid,
            "residual_sugar": bebida.residual_sugar,
            "chlorides": bebida.chlorides,
            "free_sulfurdioxide": bebida.free_sulfurdioxide,
            "total_sulfurdioxide": bebida.total_sulfurdioxide,
            "density": bebida.density,
            "pH": bebida.pH,
            "sulphates": bebida.sulphates,
            "alcohol": bebida.alcohol,
            "quality": bebida.quality
        })
        
    return {"bebidas": result}


class BebidaViewSchema(BaseModel):
    """ Define um modelo de como o paciente sera representado.
    """

    id: int = 1
    fixed_acidity: float    
    volatile_acidity: float
    citric_acid: float 
    residual_sugar: float 
    chlorides: float 
    free_sulfurdioxide: float 
    total_sulfurdioxide: float 
    density: float 
    pH: float 
    sulphates: float 
    alcohol: float = None
    


class BebidaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    # message: str
    nome: str

def apresenta_bebida(bebida: Bebida):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "id": bebida.id,
        "fixed_acidity": bebida.fixed_acidity,
        "volatile_acidity": bebida.volatile_acidity,
        "citric_acid": bebida.citric_acid,
        "residual_sugar": bebida.residual_sugar,
        "chlorides": bebida.chlorides,
        "free_sulfurdioxide": bebida.free_sulfurdioxide,
        "total_sulfurdioxide": bebida.total_sulfurdioxide,
        "density": bebida.density,
        "pH": bebida.pH,
        "sulphates": bebida.sulphates,
        "alcohol": bebida.alcohol,
        "quality": bebida.quality
    }
