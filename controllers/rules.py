from app import db 
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import Response

Rules = db.rules

def getOneRule(id):
    print(id)
    rule = Rules.find_one({'_id': ObjectId(id)})
    return Response(
        dumps(rule),
        mimetype='application/json'
    )

def getAllRules():
    all_rules = Rules.find({})
    return Response(
        dumps(all_rules),
        mimetype='application/json'
    )

def deleteRule(id):
    print(id)
    Rules.delete_one({'_id': ObjectId(id)})
    rules_db = Rules.find({})

    return Response(
        dumps(rules_db),
        mimetype='application/json'
    )

def createRule(data):

    rule = {
        'name': data['name'],        
        'description': data['description'],
    }
    Rules.insert(rule)
    rule_db = Rules.find_one(rule)

    return Response(
        dumps(rule_db),
        mimetype='application/json'
    )

def editSorteo(data):
	query = {
		'_id': ObjectId(data['id'])
	}
	new_values = {
		'name': data['name'],
		'description': data['description']
	}

	Rules.replace_one(query, new_values)
	rules_db = Rules.find_one(query)

	return Response(
		dumps(rules_db),
		mimetype='application/json'
	)
