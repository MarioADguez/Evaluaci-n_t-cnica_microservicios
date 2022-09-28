from fastapi import FastAPI
from Serie_de_fibonacci import serie_fibonacci,records, view_records

description = """
Prueba tecnica Mario Alejandro Domínguez Osorio

"""

app = FastAPI(
    title = "Prueba Tecnica",
    description = description,
    # default_response_class=ORJSONResponse,
    contact = {'name': 'Mario Domínguez', 'email': 'marioalejandrodguez@gmail.com'}
)


@app.get("/")
def read_root() -> dict:
    return {"Bienvenido": "al RESTful API  de Mario Dominguez"}

@app.post("/serie",summary = "endpoint para generar la serie de fibonacci", description = "Serie")
def serie(numero:int=None):
    serie=serie_fibonacci(numero)
    return (serie)

@app.get("/view_records",summary = "endpoint para visualizar el historico de series", description = "Recors")
def view():
    data=view_records()
    if data is None:
        return("No hay historicos")
    else:    
        return(data.to_dict('records'))
    
@app.post("/delete_record",summary = "endpoint para eliminar del registro los numeros", description = "Recors")
def delete(numero:int=None):
    records(numero,save=False)

    return(f"El registro para el numero {numero} fue eliminado")

