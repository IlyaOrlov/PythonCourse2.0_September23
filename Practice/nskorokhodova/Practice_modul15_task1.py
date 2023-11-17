Привести два примера предметной области, для представления которых лучше использовать NoSQL-подход.
Аргументировать ответ, используя критерии выбора между SQL и NoSQL.


1.  Социальные сети.
Социальные сети характеризуются большим объемом данных, высокой скоростью их прихода и изменения,
а также необходимостью горизонтального масштабирования.
В такой предметной области лучше использовать NoSQL-подход, так как он позволяет эффективно
обрабатывать и хранить большие объемы данных с использованием горизонтального масштабирования.
NoSQL базы данных обеспечивают отказоустойчивость и высокую производительность,
что очень важно для социальных сетей с миллионами пользователей.
2. Маркетплэйс ( типа Ozon, Wildberries  и т.д.)
Здесь требуется высокая скорость, т.к. может поступать много запросов, нужно
делать много изменений ( добавлять/удалять поставщиков, товары и т.д.),
поэтому лучше использовать NoSQL.
Но в то же время много различных взаимосвязей товары - цены, покупатели - заказы,
покупатели - статус заказа  и т.д. и большое количество потенциальных запросов
( поиск товаров, поиск продавца и т.д.)  - решает более эффективно SQL.
В целом, более предпочтительно использовать метод NoSQL.
