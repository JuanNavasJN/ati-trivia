from app import db 
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import Response

Trivias = db.trivias

def getOneTrivia(id):
    print(id)
    trivia = Trivias.find_one({'_id': ObjectId(id)})
    return Response(
        dumps(trivia),
        mimetype='application/json'
    )

def getAllTrivias():
    all_trivias = Trivias.find({})
    return Response(
        dumps(all_trivias),
        mimetype='application/json'
    )

def createTrivia(data):

    trivia = {
        'question': data['question']
    }
    Trivias.insert(trivia)
    trivia_db = Trivias.find_one(trivia)

    return Response(
        dumps(trivia_db),
        mimetype='application/json'
    )
