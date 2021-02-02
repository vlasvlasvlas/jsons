import pandas as pd
import simplejson as json
pag = list(range(1,64))
print (pag)
datosTotales = pd.DataFrame()
for p in pag:
    archivo = str(p)+'.txt'
    with open(archivo, encoding='utf-8') as f:
        data = json.load(f)
        data = data['listActos']
        df = pd.DataFrame(data)
        datosTotales=datosTotales.append(df,ignore_index=True)
datosTotales["link"] = 'https://www.panamacompra.gob.pa/Inicio/#!/vistaPreviaCP?NumLc=' + datosTotales["NumeroAdquisicion"].astype(str) + '&esap=1&nnc=0&it=1'
datosTotales.index.name = 'id'
print(datosTotales)
datosTotales.to_csv('99.csv')