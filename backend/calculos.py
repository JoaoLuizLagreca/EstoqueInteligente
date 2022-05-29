import datetime
import json
import pandas as pd

class Calculos ():

    def calculaEstado(self, peso, peso_medio):
        quantidade = peso / peso_medio

        df_calculo_estado = pd.DataFrame(quantidade)
        quantidade = df_calculo_estado.to_json(orient="records")
        parsed = json.loads(quantidade)
        json_calculo_estado = json.dumps(parsed, indent=4)

        print(json_calculo_estado)

        return json_calculo_estado
        #data estado
