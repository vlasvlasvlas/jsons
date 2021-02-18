# PanamaCompras 

## Objetivo

El objetivo de este repo es generar un análisis inicial de la data de contratos covid19 publicada en panamacompra.

Para esto primero se procede a generar un csv con el total de contratos covid19 que contiene las uris de cada contratación.

Luego se procederá a analizar cada contrato.

## 1 generación CSV

La idea del repo es tener disponible el total de compras covid19 de PanamaCompras en formato CSV.

Para esto se descargaron los requests curl del datatables de la página https://www.panamacompra.gob.pa.

ej:
```
curl "https://www.panamacompra.gob.pa/Security/AmbientePublico.asmx/cargarActosOportunidadesDeNegocio" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0" -H "Accept: application/json;charset=utf-8" -H "Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3" --compressed -H "Content-Type: application/x-www-form-urlencoded;charset=UTF-8" -H "Origin: https://www.panamacompra.gob.pa" -H "Connection: keep-alive" -H "Referer: https://www.panamacompra.gob.pa/Inicio/" -H "DNT: 1" -H "Sec-GPC: 1" --data-raw "METHOD=0&VALUE=""{\"BusquedaTipos\":\"True\",\"IdTipoBusqueda\":51,\"title\":\"Rendición de Cuentas COVID-19\",\"Inicio\":\"16112473802514800\"}" > panamacompras_covid_001.json
```

* el script "panamacomprasdf.py" recorre los json descargados y los concatena en un único archivo csv agregandole también la url de acceso a la compra especifica de cada registro.

* Resultado: https://github.com/vlasvlasvlas/panamacompras_covid/blob/main/99.csv

## 2 data profile

En base a los datos del csv listando el total de contratos se corrió un pandas data profile sobre el archivo csv generado.

El resultado está en:

html descargar: https://raw.githubusercontent.com/vlasvlasvlas/panamacompras_covid/main/99.html
html preview: https://htmlpreview.github.io/?https://raw.githubusercontent.com/vlasvlasvlas/panamacompras_covid/main/99.html

## 3 análisis por contrato

TODO: Se realizará un análisis por cada contrato covid19 del listado CSV.

## 4 Adjuntos

Se adjunta una comparativa de las columnas disponibles en un contrato demo covid19 y su relación con un análogo dentro del estandar OCDS.

https://docs.google.com/spreadsheets/d/1D8GiguWcUs6P1pk49nNyzXWgm9WblsoDsDcA6siUHcU/edit#gid=0



