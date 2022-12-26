from modules.participantes.model import Participante
from modules.db.services import DBservices 

participante=Participante()
participante.nombre="Lor"
participante.apellido="d"
participante.dni="458485"
participante.temperatura=45

db_services=DBservices()
db_services.execute_db( f"INSERT INTO participantes(nombre,apellido,dni,temperatura) VALUES('{participante.nombre}','{participante.apellido}', '{participante.dni}', {participante.temperatura})")

# ATENCION! db/services.py, en execute_db, falta connection.commit() antes de cursor.close()
# Asi se debe hacer
from modules.participantes.repository import ParticipantesRepository
participantes_repository = ParticipantesRepository()
participantes_repository.create(participante)

