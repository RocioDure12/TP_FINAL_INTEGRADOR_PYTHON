from .model import Participante

class ParticipantesServices:
    
    def generate_sql_from_obj(self, participante:Participante):
        sql="SET"
        sql+=f"nombre = '{participante.nombre}',"
        sql += f"apellido = '{participante.apellido}',"
        sql += f"dni = '{participante.dni}',"
        sql += f"temperatura = '{participante.temperatura}'"
        return sql
    
    def generate_obj_from_row(self, row:dict) -> Participante:
        participante=Participante()
        participante.id=row["id"]
        participante.nombre=row["nombre"]
        participante.dni=row["dni"]
        participante.temperatura=row["temperatura"]
        return participante
        
        