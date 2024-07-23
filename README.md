# Library Console

Консольный менеджер библиотеки. Позволяет вести каталог книг. Пользователь может просматривать каталог, добавлять, удалять, искать книги, а также менять статус книг при их выдаче и возврате.

### Описание модулей
- data - пакет с моделями, содержит файлы с классами, атрибуты и методы которых обеспечивают хранение и манипуляцию данными;
- db - каталог, содержащий json-файл, обеспечивающий хранение данных, при отсутствии файла, он создается при использовании команды 'list';
- errors - пакет с исключениями, используемыми в проекте;
- service - пакет с основными функциями приложения, которые обращаются к объектам пакета data, а так же выводят результаты в консоль;
- tests - тесты;
- launcher.py - запускает консольный интерфейс и обеспечивает запуск функций из пакета service.


### Запуск
```
python3 launcher.py
```
### Внимание!
Разработано на Linux. Возможна некорретная работа на Windows (у меня нет машины на Windows, не могу проверить).

### Почему так спроектировано
- Данные и методы, которые их напрямую изменяют, содержатся в отдельном классе (слое).
- Функции, которые взаимодействуют с интерфесом классов, находятся в отдельном слое.
- При каждой операции данные считываются из файла и сохраняются в файл после каждого изменения. Это уберегает от потери изменений при случайной работе в двух экземплярах приложения. Данные сохраняются даже если из приложения вышли некорретно.
