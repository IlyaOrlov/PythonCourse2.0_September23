from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
database = client["company_registry"]
collection = database["companies"]


def add_company(inn, name, ownership_form, owner_full_name, address):
    company = {
        "inn": inn,
        "name": name,
        "ownership_form": ownership_form,
        "owner_full_name": owner_full_name,
        "address": address
    }
    collection.insert_one(company)
    print("Данные о юридическом лице успешно добавлены.")


def search_by_inn(inn):
    result = collection.find_one({"inn": inn})
    if result:
        print("Найдены данные о юридическом лице:")
        print("ИНН:", result["inn"])
        print("Название организации:", result["name"])
        print("Форма собственности:", result["ownership_form"])
        print("ФИО владельца:", result["owner_full_name"])
        print("Адрес:", result["address"])
    else:
        print("Данные не найдены.")


if __name__ == "__main__":
    add_company("1234567890", "ООО Рога и Копыта", "Общество с ограниченной ответственностью",
                "Иванов Иван Иванович", "ул. Тверская, 1")
    add_company("9876543210", "ЗАО Атом", "Закрытое акционерное общество",
                "Петров Петр Петрович", "ул. Тихорецкая, 5")
    search_by_inn("1234567890")
    search_by_inn("9876543210")
    search_by_inn("0000000000")  # Несуществующий ИНН
