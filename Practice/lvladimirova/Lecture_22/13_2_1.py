import mongoengine as me


class Firms(me.Document):
    inn = me.StringField(max_length=12, required=True, unique=True)
    name = me.StringField(required=True)
    form = me.StringField(required=True)
    director = me.StringField(required=True)
    address = me.StringField(required=True)

    def __repr__(self):
        return ("<Firms(inn='{}', "
                "name='{}', "
                "form='{}', "
                "director='{}', "
                "address='{}')>").format(self.inn, self.name, self.form, self.director, self.address)


me.connect('spisok')

while True:
    inn_input = input("Введите ИНН (или введите 0 для завершения): ")
    if inn_input == "0":
        break
    name_input = input("Введите название компании: ")
    form_input = input("Введите форму собственности: ")
    director_input = input("Введите имя директора: ")
    address_input = input("Введите адрес: ")
    company = Firms(
        inn=inn_input,
        name=name_input,
        form=form_input,
        director=director_input,
        address=address_input
    )

    company.save()

print('Документов в базе: {}'.format(Firms.objects.count()))


def search_company(inn):
    company = Firms.objects(inn=inn).first()
    if company:
        print(f"Название компании: {company.name}")
        print(f"Адрес компании: {company.address}")
        print(f"Форма собственности компании: {company.form}")
        print(f"Владелец компании: {company.director}")
        print(f"Адрес компании: {company.address}")
    else:
        print("Компания с указанным ИНН не найдена.")


if __name__ == "__main__":
    search_inn = input("Введите ИНН для поиска компании: ")
    search_company(search_inn)
    Firms.objects.delete()
