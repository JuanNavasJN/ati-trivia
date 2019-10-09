from app import db 
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import Response

Sorteos = db.sorteos

def getAllSorteos():
	all_sorteos = Sorteos.find({})
	return Response(
		dumps(all_sorteos),
		mimetype='application/json'
	)


def createSorteo(data):
	premio_db = db.premios.find_one({'_id': ObjectId(data['premio'])})
	if (data['tipo'] == 'ranking'):
		sorteo = {
			'tipo': data['tipo'],
			'premio': premio_db,
			'descripcion': data['descripcion'],
			'fecha': data['fecha']
		}
	else:
		sorteo = {
			'tipo': data['tipo'],
			'premio': premio_db,
			'descripcion': data['descripcion'],
			'trivia': data['trivia'],
			'hora_inicio': data['hora_inicio'],
			'hora_fin': data['hora_fin'],
			'frecuencia': data['frecuencia']
		}

	Sorteos.insert(sorteo)
	sorteo_db = Sorteos.find_one(sorteo)

	return Response(
		dumps(sorteo_db),
		mimetype='application/json'
	)


def deleteSorteo(data):
	Sorteos.delete_one(({'_id': ObjectId(data['id'])}))
	sorteo_db = Sorteos.find({})

	return Response(
		dumps(sorteo_db),
		mimetype='application/json'
	)


def editSorteo(data):
	query = {
		'_id': ObjectId(data['id'])
	}
	new_values = {
		'tipo': data['tipo'],
		'premio': data['premio'],
		'descripcion': data['descripcion'],
		'fecha': data['fecha'],
		'trivia': data['trivia'],
		'hora_inicio': data['hora_inicio'],
		'hora_fin': data['hora_fin'],
		'frecuencia': data['frecuencia']
	}

	Sorteos.replace_one(query, new_values)
	sorteos_db = Sorteos.find_one(query)

	return Response(
		dumps(sorteos_db),
		mimetype='application/json'
	)