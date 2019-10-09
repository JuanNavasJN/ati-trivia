from app import db 
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import Response

Premios = db.premios

def getAllPremios():
	all_premios = Premios.find({})
	return Response(
		dumps(all_premios),
		mimetype='application/json'
	)


def createPremio(data):
	print(data)
	premio = {
		'tipo': data['tipo'],
		'puntos': data['puntos'],
		'descripcion': data['descripcion']
	}
	Premios.insert(premio)
	premio_db = Premios.find_one(premio)

	return Response(
		dumps(premio_db),
		mimetype='application/json'
	)


def deletePremio(data):
	Premios.delete_one(({'_id': ObjectId(data['id'])}))
	premio_db = Premios.find({})

	return Response(
		dumps(premio_db),
		mimetype='application/json'
	)


def editPremio(data):
	query = {
		'_id': ObjectId(data['id'])
	}
	new_values = {
		'tipo': data['tipo'],
		'puntos': data['puntos'],
		'descripcion': data['descripcion']
	}

	Premios.replace_one(query, new_values)
	premios_db = Premios.find_one(query)

	return Response(
		dumps(premios_db),
		mimetype='application/json'
	)