# IMPORTACIONES
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Session, select
from database.config import engine, obtener_db
from models.Biblia import Biblia, Testamento, Libro, Capitulo, Versiculo, BibliaRequest, TestamentoRequest, LibroRequest, CapituloRequest, VersiculoRequest, BibliaResponse, TestamentoResponse, LibroResponse, CapituloResponse, VersiculoResponse, VersiculoTextoResponse
from typing import List
from sqlalchemy.exc import SQLAlchemyError

# INICIAR LA API
app = FastAPI(
    title="API Biblia",
    version="1.0.0"
)

# CREAR TODAS LAS TABLAS
SQLModel.metadata.create_all(engine)

# Creaciones (POST)
@app.post("/biblia", response_model=dict, tags=["Crear biblia"])
def crear_biblia(biblia: BibliaRequest, db: Session = Depends(obtener_db)):
    try:
        inserta_biblia = Biblia.model_validate(biblia)
        db.add(inserta_biblia)
        db.commit()
    except SQLAlchemyError as sa_error:
        db.rollback()
        
        # Código de estado 500 (error interno)
        raise HTTPException(
            status_code=500,
            detail=f"Error en la base de de datos: {sa_error}"
        )
    except Exception as error:
        db.rollback()

        # Código de estado 400 (solicitud incorrecta)
        raise HTTPException(
            status_code=400,
            detail=f"Error inesperado: {str(error)}"
        )

    return {"msg": "Biblia creada correctamente"}

@app.post("/testamento", response_model=dict, tags=["Crear testamento"])
def crear_testamento(testamento: TestamentoRequest, db: Session = Depends(obtener_db)):
    try:
        inserta_testamento = Testamento.model_validate(testamento)
        db.add(inserta_testamento)
        db.commit()
    except SQLAlchemyError as sa_error:
        db.rollback()
        
        # Código de estado 500 (error interno)
        raise HTTPException(
            status_code=500,
            detail=f"Error en la base de de datos: {sa_error}"
        )
    except Exception as error:
        db.rollback()

        # Código de estado 400 (solicitud incorrecta)
        raise HTTPException(
            status_code=400,
            detail=f"Error inesperado: {str(error)}"
        )

    return {"msg": "Testamento creado correctamente"}

@app.post("/libro", response_model=dict, tags=["Crear libro"])
def crear_libro(libro: LibroRequest, db: Session = Depends(obtener_db)):
    try:
        inserta_libro = Libro.model_validate(libro)
        db.add(inserta_libro)
        db.commit()
    except SQLAlchemyError as sa_error:
        db.rollback()
        
        # Código de estado 500 (error interno)
        raise HTTPException(
            status_code=500,
            detail=f"Error en la base de de datos: {sa_error}"
        )
    except Exception as error:
        db.rollback()

        # Código de estado 400 (solicitud incorrecta)
        raise HTTPException(
            status_code=400,
            detail=f"Error inesperado: {str(error)}"
        )

    return {"msg": "Libro creado correctamente"}

@app.post("/capitulo", response_model=dict, tags=["Crear capitulo"])
def crear_capitulo(capitulo: CapituloRequest, db: Session = Depends(obtener_db)):
    try:
        inserta_capitulo = Capitulo.model_validate(capitulo)
        db.add(inserta_capitulo)
        db.commit()
    except SQLAlchemyError as sa_error:
        db.rollback()
        
        # Código de estado 500 (error interno)
        raise HTTPException(
            status_code=500,
            detail=f"Error en la base de de datos: {sa_error}"
        )
    except Exception as error:
        db.rollback()

        # Código de estado 400 (solicitud incorrecta)
        raise HTTPException(
            status_code=400,
            detail=f"Error inesperado: {str(error)}"
        )

    return {"msg": "Capitulo creado correctamente"}

@app.post("/versiculo", response_model=dict, tags=["Crear versiculo"])
def crear_versiculo(versiculo: VersiculoRequest, db: Session = Depends(obtener_db)):
    try:
        inserta_versiculo = Versiculo.model_validate(versiculo)
        db.add(inserta_versiculo)
        db.commit()
    except SQLAlchemyError as sa_error:
        db.rollback()
        
        # Código de estado 500 (error interno)
        raise HTTPException(
            status_code=500,
            detail=f"Error en la base de de datos: {sa_error}"
        )
    except Exception as error:
        db.rollback()

        # Código de estado 400 (solicitud incorrecta)
        raise HTTPException(
            status_code=400,
            detail=f"Error inesperado: {str(error)}"
        )

    return {"msg": "Versiculo creado correctamente"}

# Obtenciones (GET)
@app.get("/biblias", response_model=List[BibliaResponse], tags=["Mostrar todas las biblias"])
def obtener_biblias(db: Session = Depends(obtener_db)):
    try:
        consulta = select(Biblia)
        resultados = db.exec(consulta).all()
        return resultados
    except SQLAlchemyError as sa_error:
        # Código de estado 500 (error interno)
        raise HTTPException(
            status_code=500,
            detail="Error al consultar las Biblias en la base de datos"
        )
    except Exception as error:
        # Código de estado 500 (error interno)
        raise HTTPException(
            status_code=500,
            detail=f"Error inesperado: {str(error)}"
        )

@app.get("/testamentos", response_model=List[TestamentoResponse], tags=["Mostrar todas los testamentos"])
def obtener_testamentos(db: Session = Depends(obtener_db)):
    try:
        consulta = select(Testamento)
        resultados = db.exec(consulta).all()
        return resultados
    except SQLAlchemyError as sa_error:
        # Código de estado 500 (error interno)
        raise HTTPException(
            status_code=500,
            detail="Error al consultar los testamentos en la base de datos"
        )
    except Exception as error:
        # Código de estado 500 (error interno)
        raise HTTPException(
            status_code=500,
            detail=f"Error inesperado: {str(error)}"
        )

@app.get("/libros", response_model=List[LibroResponse], tags=["Mostrar todas los libros"])
def obtener_libros(db: Session = Depends(obtener_db)):
    try:
        consulta = select(Libro)
        resultados = db.exec(consulta).all()
        return resultados
    except SQLAlchemyError as sa_error:
        # Código de estado 500 (error interno)
        raise HTTPException(
            status_code=500,
            detail="Error al consultar los libros en la base de datos"
        )
    except Exception as error:
        # Código de estado 500 (error interno)
        raise HTTPException(
            status_code=500,
            detail=f"Error inesperado: {str(error)}"
        )

@app.get("/capitulos", response_model=List[CapituloResponse], tags=["Mostrar todas los capitulos"])
def obtener_capitulos(db: Session = Depends(obtener_db)):
    try:
        consulta = select(Capitulo)
        resultados = db.exec(consulta).all()
        return resultados
    except SQLAlchemyError as sa_error:
        # Código de estado 500 (error interno)
        raise HTTPException(
            status_code=500,
            detail="Error al consultar los capitulos en la base de datos"
        )
    except Exception as error:
        # Código de estado 500 (error interno)
        raise HTTPException(
            status_code=500,
            detail=f"Error inesperado: {str(error)}"
        )

@app.get("/versiculos", response_model=List[VersiculoResponse], tags=["Mostrar todas los versiculos"])
def obtener_versiculos(db: Session = Depends(obtener_db)):
    try:
        consulta = select(Versiculo)
        resultados = db.exec(consulta).all()
        return resultados
    except SQLAlchemyError as sa_error:
        # Código de estado 500 (error interno)
        raise HTTPException(
            status_code=500,
            detail="Error al consultar los versiculos en la base de datos"
        )
    except Exception as error:
        # Código de estado 500 (error interno)
        raise HTTPException(
            status_code=500,
            detail=f"Error inesperado: {str(error)}"
        )

# Obtenciones por ID (GET)
@app.get("/versiculos/{capitulo_id}", response_model=List[VersiculoTextoResponse])
def obtener_rango_versiculos(capitulo_id: int, inicio: int, fin: int, db: Session = Depends(obtener_db)):
    if inicio > fin:
        raise HTTPException(
            status_code=400, 
            detail="El versiculo inicial no puede ser mayor que el final"
        )
    
    # Verificar existencia del capitulo
    consulta_capitulo = select(Capitulo).where(Capitulo.id == capitulo_id)
    resultado_capitulo = db.exec(consulta_capitulo).first()

    if not resultado_capitulo:
        raise HTTPException(
            status_code=400,
            detail=f"No es encontró el capitulo con id {capitulo_id}"
        )
    
    # Consultar el rango si el capitulo existe
    consulta_rango = select(Versiculo).where(Versiculo.capitulo_id == capitulo_id, Versiculo.numero >= inicio, Versiculo.numero <= fin)
    resultados = db.exec(consulta_rango).all()

    if not resultados:
        raise HTTPException(
            status_code=404,
            detail="No se encontraron versículos en el rango indicado"
        )
    
    return resultados