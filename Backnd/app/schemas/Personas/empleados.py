from pydantic import BaseModel
from datetime import date
from typing import Optional

class EmpleadoBase(BaseModel):
    cod_persona: int
    cod_tipo_empleado: int
    cod_area: int
    cod_tipo_contrato: int
    fecha_salida: Optional[date] = None
    motivo_salida: Optional[str] = None
    fecha_contratacion: date
    salario: float
    estado_empleado: str


class EmpleadoUpdateBase(BaseModel):
    cod_persona: int
    cod_tipo_empleado: int
    cod_area: int
    cod_tipo_contrato: int
    fecha_salida: Optional[date] = None
    motivo_salida: Optional[str] = None
    fecha_contratacion: date
    salario: float
    estado_empleado: str


class EmpleadoDespedir(BaseModel):
    fecha_salida: Optional[date] = None
    motivo_salida: Optional[str] = None


class EmpleadoCreate(EmpleadoBase):
    pass


class EmpleadoUpdate(EmpleadoUpdateBase):
    pass

class EmpleadoResponse(BaseModel):
    cod_empleado: Optional[int] = None
    cod_persona: Optional[int] = None
    cod_tipo_empleado: Optional[int] = None
    cod_area: Optional[int] = None
    cod_tipo_contrato: Optional[int] = None
    fecha_salida: Optional[date] = None
    motivo_salida: Optional[str] = None
    fecha_contratacion: Optional[date] = None
    salario: Optional[float] = None
    estado_empleado: Optional[str] = None

    class Config:
        from_attributes = True


# ------------------------------------------------------------------------------
# TIPOS AUXILIARES
# ------------------------------------------------------------------------------
class NombreTipoEmpleadoBase(BaseModel):
    nombre_tipo_empleado: str

class NombreTipoEmpleadoCreate(NombreTipoEmpleadoBase):
    pass

class NombreTipoEmpleado(NombreTipoEmpleadoBase):
    cod_tipo_empleado: int

    class Config:
        from_attributes = True

class AreasBase(BaseModel):
    nombre_area: str

class AreasCreate(AreasBase):
    pass 

class Areas(AreasBase):
    cod_area: int

    class Config:
        from_attributes = True

class TipoContratoBase(BaseModel):
    tipo_contrato: str

class TipoContratoCreate(TipoContratoBase):
    pass

class TipoContrato(TipoContratoBase):
    cod_tipo_contrato: int

    class Config:
        from_attributes = True