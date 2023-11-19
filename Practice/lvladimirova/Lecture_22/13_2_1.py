import mongoengine as me


class Firms(me.Document):
    inn = me.StringField(required=True, unique=True)
    name = me.StringField(required=True)
    ownership_form = me.StringField(required=True)
    owner_full_name = me.StringField(required=True)
    address = me.StringField(required=True)


conn = me.connect('firms')


def add_company(inn, name, ownership_form, owner_full_name, address):
    company = Firms(inn=inn, name=name, ownership_form=ownership_form,
                    owner_full_name=owner_full_name, address=address)
    company.save()


def search_company(inn):
    company = Firms.objects(inn=inn).first()
    if company:
        return f"Название организации: {company.name}\n" \
               f"Форма собственности: {company.ownership_form}\n" \
               f"ФИО владельца: {company.owner_full_name}\n" \
               f"Адрес: {company.address}"
    else:
        return "Организация с указанным ИНН не найдена."


add_company("1234567890", "ООО Рога и Копыта", "Общество с ограниченной ответственностью",
            "Иванов Иван Иванович", "ул. Тверская, 1")
add_company("9876543210", "ЗАО Атом", "Закрытое акционерное общество",
            "Петров Петр Петрович", "ул. Тихорецкая, 5")
search_inn = "1234567890"
result = search_company(search_inn)
print(result)
