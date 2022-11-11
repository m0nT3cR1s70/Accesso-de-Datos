from logger_base import log

class Persona:
	"""docstring for Persona"""
	persona = 0
	def __init__(self,id_persona=None,nombre=None,apellido=None,email=None):
		Persona.persona += 1
		self._id_persona = id_persona
		self._id_persona = Persona.persona
		self._nombre     = nombre
		self._apellido   = apellido
		self._email      = email

	def __str__(self):
		return f'ID: {self._id_persona} Persona: {self._nombre} {self._apellido} {self._email}'

	## GETS and SETS
	@property
	def id_persona(self):
		return self._id_persona

	@id_persona.setter
	def id_persona(self,id_persona):
		self._id_persona = id_persona



	@property
	def nombre(self):
		return self._nombre

	@nombre.setter
	def nombre(self,nombre):
		self._nombre = nombre


	@property
	def apellido(self):
		return self._apellido

	@apellido.setter
	def apellido(self,apellido):
		self._apellido = apellido


	@property
	def email(self):
		return self._email

	@email.setter
	def email(self,email):
		self._email = email


if __name__ == '__main__':
	persona = Persona(1,'Yizbeleni','Gallardo','yiz@mail.com')
	#print(persona)
	log.debug(persona)
	# SIMULAR un insert
	persona = Persona(2,'Mario','Nieto','yiz@mail.com')
	log.debug(persona)
	# SIMULAR UN DELETE
	persona