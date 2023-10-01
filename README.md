# Условия домашки
Критерий выполнения заданий Результат задания залейте в GitHub и сдайте в виде ссылки на репозиторий.

### Задание 1
Продолжаем работать с проектом из предыдущего домашнего задания. Для модели продуктов реализуйте механизм CRUD, задействовав модуль
django.forms.
- могут создавать новые продукты;
- не могут загружать запрещенные продукты на платформу.

Для исключения загрузки запрещенных продуктов реализуйте валидацию названия и описания продукта таким образом, чтобы нельзя было в них добавлять слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.

### Задание 2
Добавьте новую модель «Версия», которая должна содержать следующие поля:

- продукт,
- номер версии,
- название версии,
- признак текущей версии.

При наличии активной версии реализуйте вывод в список продуктов информации об активной версии.

### Задание 3
Для работы с версиями продукта добавьте реализацию работы с формами. При этом версия может быть внесена только в существующий продукт.

Все созданные формы нужно стилизовать так, чтобы они были в единой стилистике оформления всей платформы. Для этого можно воспользоваться методом
__init__ либо самостоятельно изучить пакет crispy-forms: https://pypi.org/project/django-crispy-forms/.

### Дополнительное задание
Когда статья достигает 100 просмотров, отправлять себе на почту поздравление с достижением.
В один момент времени может быть только одна активная версия продукта, поэтому при изменении версий необходимо проверять, что пользователь в качестве активной версии указал только одну. В случае возникновения ошибки вернуть сообщение пользователю и попросить выбрать только одну активную версию.

Дополнительное задание, помеченное звездочкой, желательно, но не обязательно выполнять.
