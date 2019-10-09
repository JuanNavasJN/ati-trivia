from app import db 
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import Response

Categories = db.category

def getOneCategory(id):
    # print(id)
    category = Categories.find_one({'_id': ObjectId(id)})
    return Response(
        dumps(category),
        mimetype='application/json'
    )

def getAllCategories():
    all_categorys = Categories.find({})
    return Response(
        dumps(all_categorys),
        mimetype='application/json'
    )

def deleteCategory(id):
    Categories.delete_one({'_id': ObjectId(id)})
    categories_db = Categories.find({})

    return Response(
        dumps(categories_db),
        mimetype='application/json'
    )

def createCategory(data):

    category = {
        'name': data['name'],
        # 'image_url': '../../static/img/marcas.png' 
        'image': data['image'],
    }
    Categories.insert(category)
    category_db = Categories.find_one(category)

    return Response(
        dumps(category_db),
        mimetype='application/json'
    )
