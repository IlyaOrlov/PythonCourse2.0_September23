"""   Примеры предметной области, для которых лучше использовать NoSQL

Социальные сети, маркетплэйсы:
1. Слабая реляционность данных.
   Данные пользователей независимы, слабо связаны с другими, сторонними данными.
2. Простота запросов, нет сложных анализов данных, серьезной статистики.
   Практически все запросы пользователей сводятся к типичным и их количество не так велико.
3. Неустойчивость схемы в смысле возможных частых изменений, дополнений.
   Бывает, борьба идет за клиентов, это приводит к новым идеям, возможностям,
   которые нужно быстро реализовать
4. Доступнось при наличии больших объемов данных.
   Скорость решает все! Данные должны быть сразу и все. Доступ к ним не замутнет изворотами логики.
5. Не строгая согласованность, согласованность в конечном счете.
   Где то, что то не поменяется сразу, но и не важно, мы же общаемся а не переводим кучу денег.
   И в конечном итоге все согласуется.
6. Устойчивость к разделению, возможность вертикального и горизонтального расширения.
   При нехватке места или мощности проще расширятся.
7. Хранение данных различных типов, медиафайлы.

Бот "Чуткое ухо"!
База данных хранит все тайные переговоры по мобильной связи.
Простой алгоритм сортировки по критическим фразам.
1. Все что перечисленно выше
2. Может быть представлен огромным словарем
3. Может провоцировать
4. Может работать в оперативной памяти
5. Может быть гибким к ключевым фразам

"""