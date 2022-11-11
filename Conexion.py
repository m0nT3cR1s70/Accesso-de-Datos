import psycopg2

class Conexion:
	DATABASE = 'Test'
	HOST     = 'localhost'
	PASSWORD = 'administror'
	PORT     = 5432
	USER     = 'm0nT3cR1s70'

if __name__ == '__main__':

	DATABASE = 'Test'
	HOST     = 'localhost'
	PASSWORD = 'administror'
	PORT     = 5432
	USER     = 'm0nT3cR1s70'
	conexion = psycopg2.connect(database=DATABASE,
		host=HOST,
		password=PASSWORD,
		port=PORT,
		user=USER)