## Описать процесс тестирования "Платежи"
Для тестирования будем использовать следующие техники тест дизайна:
- Доменное тестирование(Граничные значения и Классы эквивалентности)
- Диаграмму переходов и переходов
- Причина следствие

Для интеграционного тестирования будем использовать техинку "Подход большого взрыва"

В качестве документации будем использовать:
- Основные формы - чек листы
- Взаимодействие между модулями - тест кейсы.

Основные риски:
- Документ не создается
- Уменьшающийся платеж(рассрочка) функционирует не корректно
## Чек лист

1) Зайти на finance.dev.fabrique.studio
2) Проверить наличие поле входа
3) Авторизация email, password 
4) Проверить наличие полей таблицы Источник, Статус, Сумма, Дата, Статья/Контрагент, Описание
5) При нажатии кнопки "Добавить платеж" переход на форму добавления платежа
6) Доход, имеет поля Описание, Статус, Сумма план,Сумма факт, Статус оплаты, Дата план, Дата факт, Источник, Источник, уточнение, Статус документов, Юридическое лицо, Контрагент, Счет отправителя, Счет получателя, Тэги
7) Расход, имеет поля Описание, Статус, Сумма план,Сумма факт, Статус оплаты, Дата план, Дата факт, Статья расходов, Статья расходов, уточнение, Юридическое лицо, Контрагент, Счет отправителя, Счет получателя, Тэги
7) Перевод средств, имеет поля Описание, Статус, Сумма план,Сумма фактб, Комиссия, Статус оплаты, Дата план, Дата факт, Счет отправителя, Счет получателя, Тэги
8) При выбранном Существующиего платежа "Доход","Расход","Перевод средств" Пункты формы совпадают с макетом, описанным выше



## Тест кейс
Авторизация 
1) Зайти на finance.dev.fabrique.studio
2) Проверить наличие поле входа
3) Авторизация
4) Проверить, что вы на главной странице

Проверка формы

1) Проверить наличие полей таблицы 6*
2) Должна быть кнопка "Добавить платёж"
3) Должна кнопка перехода на другую странцу "1", "2", "3"

Добавление платежа

1) Нажимаем на кнопку добавления платежа
2) Проверяем, что действительно появилось форма или какое то конкретное поле
3) Добавляем описание (
4) Нажимаем кнопку обновить/создание счёта
5) Сохраняем url,а именно номер платежа (н.п.:'975')
6) Проверка наличия сообщения о дабовлентии
7) Переход на гл. странцу из breadcrumbs
8) Проверка наличия поля поиска
9) Поиск платежа в филтьре( по описанию ) из шага 3
10) Переход по единственной найденной вриации.
11) Проверка url, что нынешний url совподает с сохраненнием из шага 5

## Команды для запуска через pytest основных тестов .mark
```
pytest -v -s --tb=line --language=en -m all_test
```

