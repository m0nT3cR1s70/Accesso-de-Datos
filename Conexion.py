import psycopg2 as bd
from logger_base import log
import sys

class Conexion:
	_DATABASE = 'Test'
	_HOST     = 'localhost'
	_PASSWORD = 'administror'
	_PORT     = 5432
	_USER     = 'm0nT3cR1s70'
	_conexion = None
	_cursor   = None

	@classmethod
	def obtenerConexion(cls):
		if cls._conexion is None:
			try:
				cls._conexion = bd.connect(
					database  = cls._DATABASE,
					host      = cls._HOST,
					password  = cls._PASSWORD, 
					port      = cls._PORT,
					user      = cls._USER
				)
				log.debug(f'Conexion exitosa {cls._conexion}')
				return cls._conexion
			except Exception as e:
				log.error(f'Ocurrion una exception {e} conexion') 
				sys.exit()
		else:
			return cls._conexion

	@classmethod
	def obtenerCursor(cls):
		if cls._cursor is None:
			try:
				cls._cursor = cls.obtenerConexion().cursor()
				log.debug(f'Cursor abierto {cls._cursor}')
			except Exception as e:
				log.error(f'Ocurrion una exception {e} cursor')
				sys.exit()
		else:
			return cls._cursor




if __name__ == '__main__':
	conexion = Conexion()
	#conexion.obtenerconexion()
	conexion.obtenerCursor()