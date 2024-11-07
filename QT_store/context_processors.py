from .models import *
from .mongo import MongoDB

def categories(request, collection_name="categories"):  # Задаем значение по умолчанию для имени коллекции
    mongo = MongoDB()
    
    # Получаем коллекцию по имени
    collection = mongo.get_collection(collection_name)
    
    # Извлекаем все категории из коллекции, сортируя по полю "id"
    categories = list(collection.find().sort("id", 1))
    
    mongo.close()  # Закрываем соединение

    return {'categories': categories}