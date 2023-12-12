import numpy as np
import pickle


class Model:
    def carrega_modelo(path):
        """ Se o formato for .pkl carrega o arquivo, caso contrario o formato n e suportado.
        """
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        else:
            raise Exception('O formato do arquivo e invalido')
        return model
    
    def preditor(model, form):
        """
        Realiza a predicao do paciente atravez do modelo pronto.
        """
        X_input = np.array([form.fixed_acidity,                          
                            form.volatile_acidity,
                            form.citric_acid,
                            form.residual_sugar,
                            form.chlorides,
                            form.free_sulfurdioxide,
                            form.total_sulfurdioxide,
                            form.density,
                            form.pH,
                            form.sulphates,
                            form.alcohol
                ])
        diagnosis = model.predict(X_input.reshape(1, -1))
        return int(diagnosis[0])