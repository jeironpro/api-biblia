from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Biblia(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    version: str
    idioma: str = Field(default="es")

    testamentos: List["Testamento"] = Relationship(
        back_populates="biblia"
    )

class Testamento(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    abreviatura: str
    biblia_id: int = Field(foreign_key="biblia.id")

    biblia: Optional[Biblia] = Relationship(
        back_populates="testamentos"
    )
    libros: List["Libro"] = Relationship(
        back_populates="testamento"
    )

class Libro(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(unique=True)
    abreviatura: str
    orden: int
    testamento_id: int = Field(foreign_key="testamento.id")

    testamento: Optional[Testamento] = Relationship(
        back_populates="libros"
    )
    capitulos: List["Capitulo"] = Relationship(
        back_populates="libro"
    )

class Capitulo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    numero: int
    libro_id: int = Field(foreign_key="libro.id")

    libro: Optional[Libro] = Relationship(
        back_populates="capitulos"
    )
    versiculos: List["Versiculo"] = Relationship(
        back_populates="capitulo"
    )

class Versiculo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    numero: int
    texto: str
    capitulo_id: int = Field(foreign_key="capitulo.id")

    capitulo: Optional[Capitulo] = Relationship(
        back_populates="versiculos"
    )

class BibliaRequest(SQLModel):
    version: str = Field(description="Nombre o versión de la Biblia")
    idioma: str = Field(default="es", description="Abreviatura del idioma de la Biblia")

class TestamentoRequest(SQLModel):
    nombre: str = Field(description="Nombre del testamento")
    abreviatura: str = Field(description="Abreviatura del testamento")
    biblia_id: int = Field(description="ID de la Biblia a la que pertenece")

class LibroRequest(SQLModel):
    nombre: str = Field(min_length=1, description="Nombre del libro")
    abreviatura: str = Field(min_length=2, max_length=10)
    orden: int = Field(gt=0, description="Orden dentro del testamento")
    testamento_id: int = Field(description="ID del testamento")

class CapituloRequest(SQLModel):
    numero: int = Field(gt=0, description="Número del capítulo")
    libro_id: int = Field(description="ID del libro")

class VersiculoRequest(SQLModel):
    numero: int = Field(gt=0, description="Número del versículo")
    texto: str = Field(min_length=1, description="Texto del versículo")
    capitulo_id: int = Field(description="ID del capítulo")

class BibliaResponse(SQLModel):
    id: int
    version: str
    idioma: str

class TestamentoResponse(SQLModel):
    id: int
    nombre: str
    abreviatura: str
    biblia_id: int

class LibroResponse(SQLModel):
    id: int
    nombre: str
    abreviatura: str
    orden: int
    testamento_id: int

class CapituloResponse(SQLModel):
    id: int
    numero: int
    libro_id: int

class VersiculoResponse(SQLModel):
    id: int
    numero: int
    texto: str
    capitulo_id: int

class VersiculoTextoResponse(SQLModel):
    numero: int
    texto: str