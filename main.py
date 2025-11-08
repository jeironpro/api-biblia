# IMPORTACIONES
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session, select
from database.config import engine, obtener_db
from models.Biblia import Biblia, Testamento, Libro, Capitulo, Versiculo, BibliaRequest, TestamentoRequest, LibroRequest, CapituloRequest, VersiculoRequest, BibliaResponse, TestamentoResponse, LibroResponse, CapituloResponse, VersiculoResponse

# INICIAR LA API
app = FastAPI(
    title="API Biblia",
    version="1.0.0"
)

# CREAR TODAS LAS TABLAS
SQLModel.metadata.create_all(engine)

@app.post("/crear_biblia", response_model=dict, tags=["Crear biblia"])
def crear_biblia(biblia: BibliaRequest, db: Session = Depends(obtener_db)):
    inserta_biblia = Biblia.model_validate(biblia)

    db.add(inserta_biblia)
    db.commit()

    return {"msg": "Biblia creada correctamente"}

@app.post("/crear_testamento", response_model=dict, tags=["Crear testamento"])
def crear_testamento(testamento: TestamentoRequest, db: Session = Depends(obtener_db)):
    inserta_testamento = Testamento.model_validate(testamento)

    db.add(inserta_testamento)
    db.commit()

    return {"msg": "Testamento creado correctamente"}

@app.post("/crear_libro", response_model=dict, tags=["Crear libro"])
def crear_libro(libro: LibroRequest, db: Session = Depends(obtener_db)):
    inserta_libro = Libro.model_validate(libro)

    db.add(inserta_libro)
    db.commit()

    return {"msg": "Libro creado correctamente"}

@app.post("/crear_capitulo", response_model=dict, tags=["Crear capitulo"])
def crear_capitulo(capitulo: CapituloRequest, db: Session = Depends(obtener_db)):
    inserta_capitulo = Capitulo.model_validate(capitulo)

    db.add(inserta_capitulo)
    db.commit()

    return {"msg": "Capitulo creado correctamente"}

@app.post("/crear_versiculo", response_model=dict, tags=["Crear versiculo"])
def crear_versiculo(versiculo: VersiculoRequest, db: Session = Depends(obtener_db)):
    inserta_versiculo = Versiculo.model_validate(versiculo)

    db.add(inserta_versiculo)
    db.commit()

    return {"msg": "Versiculo creado correctamente"}

@app.get("/obtener_biblias", response_model=list[BibliaResponse], tags=["Mostrar todas las biblias"])
def obtener_biblias(db: Session = Depends(obtener_db)):
    consulta = select(Biblia)
    resultados = db.exec(consulta).all()
    return resultados

@app.get("/obtener_testamentos", response_model=list[TestamentoResponse], tags=["Mostrar todas los testamentos"])
def obtener_testamentos(db: Session = Depends(obtener_db)):
    consulta = select(Testamento)
    resultados = db.exec(consulta).all()

    return resultados

@app.get("/obtener_libros", response_model=list[LibroResponse], tags=["Mostrar todas los libros"])
def obtener_libros(db: Session = Depends(obtener_db)):
    consulta = select(Libro)
    resultados = db.exec(consulta).all()

    return resultados

@app.get("/obtener_capitulos", response_model=list[CapituloResponse], tags=["Mostrar todas los capitulos"])
def obtener_capitulos(db: Session = Depends(obtener_db)):
    consulta = select(Capitulo)
    resultados = db.exec(consulta).all()

    return resultados

@app.get("/obtener_versiculos", response_model=list[VersiculoResponse], tags=["Mostrar todas los versiculos"])
def obtener_versiculos(db: Session = Depends(obtener_db)):
    consulta = select(Versiculo)
    resultados = db.exec(consulta).all()
    
    return resultados