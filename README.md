# Library Console

Консольный менеджер библиотеки. 

### Описание модулей
a. data - пакет с моделями, содержит файлы с классами, атрибуты и методы которых обеспечивают хранение и манипуляцию данными;
b. db - каталог, содержащий json-файл, обеспечивающий хранение данных, при отсутствии файла, он создается при использовании команды 'list';
c. errors - пакет с исключениями, используемыми в проекте;
d. service - пакет с основными функциями приложения, которые обращаются к объектам пакета data, а так же выводят результаты в консоль;
e. tests - тесты;
f. launcher.py - запускает консольный интерфейс и обеспечивает запуск функций из пакета service;


### Запуск
```
python3 launcher.py
```
