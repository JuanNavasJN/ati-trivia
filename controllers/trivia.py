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

# def getOneTrivia(category):
#     print(id)
#     trivia = Trivias.find_one({'_id': ObjectId(id)})
#     return Response(
#         dumps(trivia),
#         mimetype='application/json'
#     )

def getAllTrivias():
    all_trivias = Trivias.find({})
    return Response(
        dumps(all_trivias),
        mimetype='application/json'
    )

def deleteTrivia(id):
    Trivias.delete_one({'_id': ObjectId(id)})
    trivias_db = Trivias.find({})

    return Response(
        dumps(trivias_db),
        mimetype='application/json'
    )

def createTrivia(data):

    trivia = {
        "question": data['question'],
        "category": data['category'],
        "correct": data['correct'],
        "image": data['image'],
        "audio": data['audio'],
        "options": data['options']
    }

    Trivias.insert(trivia)
    trivia_db = Trivias.find_one(trivia)

    return Response(
        dumps(trivia_db),
        mimetype='application/json'
    )

def editTrivia(data):
    query = {
        '_id': ObjectId(data['id'])
    }
    trivia = Trivias.find_one({'_id': ObjectId(data['id'])})
    trivia['question'] = data['question']
    trivia['category'] = data['category']
    trivia['correct'] = data['correct']
    trivia['options'] = data['options']

    Trivias.replace_one(query, trivia)
    trivias_db = Trivias.find_one(query)

    return Response(
        dumps(trivias_db),
        mimetype='application/json'
    )