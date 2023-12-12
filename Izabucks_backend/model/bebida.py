from sqlalchemy import Column, Integer, Float

from model import Base

class Bebida(Base):
    __tablename__ = 'bebida'

    id = Column("pk_bebida", Integer, primary_key=True)    
    fixed_acidity = Column(Float)      
    volatile_acidity = Column(Float)
    citric_acid = Column(Float)
    residual_sugar = Column(Float)
    chlorides = Column(Float)
    free_sulfurdioxide = Column(Float)
    total_sulfurdioxide = Column(Float)
    density = Column(Float)
    pH = Column(Float)
    sulphates = Column(Float)
    alcohol = Column(Float)
    quality = Column(Integer, nullable=True)
    




    def __init__(self, fixed_acidity:float, volatile_acidity:float, citric_acid:float, 
                 residual_sugar:float, chlorides:float, 
                 free_sulfurdioxide:float, total_sulfurdioxide:float, density:float,
                 pH:float, sulphates:float, alcohol:float, quality:int):
        """
        Cria um Paciente

        Arguments:
            
            nome: nome do paciente.
            idade: idade do paciente.
            sexo: sexo do paciente(0 = masculino, 1 = feminino).
            dor_toraxica: dor no peito, (0 = assintomático, 1 = sintomático).
            PressaoArt_Repouso: pressão arterial(mm Hg) medida em repouso (na admissão ao hospital) 
            colesterol: valor do colesterol sérico em mg/dl
            glicemia_jejum: valor da glicemia aferida em jejum(0 <= 120mg/dl, 1 >= 120mg/dl)
            ecg_repouso: eletrocardiograma em repouso (0 = sem alterações, 1 = alterado)
            fcm: frequência cardíaca máxima alcançada
            resultado: resultado onde (1 = possui doênças cardíacas, 0 = ausência de doênças cardiovasculares)
        """
        self.fixed_acidity = fixed_acidity
        self.volatile_acidity = volatile_acidity
        self.citric_acid = citric_acid
        self.residual_sugar = residual_sugar
        self.chlorides = chlorides
        self.free_sulfurdioxide = free_sulfurdioxide
        self.total_sulfurdioxide = total_sulfurdioxide
        self.density = density
        self.pH = pH
        self.sulphates = sulphates
        self.alcohol = alcohol
        self.quality = quality