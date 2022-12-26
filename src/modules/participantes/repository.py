from .model import Participante
from ..db.services import DBservices
from .services import ParticipantesServices

class ParticipantesRepository:
    def create(self, participante:Participante):
        # Instanciar DBServices
        db_services=DBservices()
        # Ejecutar .execute_db de la instancia de DBServices con el INSERT
        db_services.execute_db(f"INSERT INTO participantes(nombre,apellido,dni,temperatura) VALUES('{participante.nombre}','{participante.apellido}', '{participante.dni}', {participante.temperatura})")
