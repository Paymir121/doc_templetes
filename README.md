# Приложение шаблонизатор

### Описание
Приложение берет Excel файл 'context.xlsx', где заполнены необходимые поля [id, name , data] приобразует этот файл в словарь вида context = {name: data}
Пробигается по всем файлам в папке с *.docx и заменяет все вхождение name на data. В ворд шаблоне поле должно быть оформленно в виде "{{name}}" 
Благодаря этому проекту можно  улучшить комьюните по методичке @Травомана

### Технологии
Ножовка и шашлык

### Запуск проекта в dev-режиме

#### Установите и активируйте виртуальное окружение WINDOWS
```
python3.9 -m venv venv
```

```
source venv/Scripts/activate
```
### Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

#### Установите и активируйте виртуальное окружение MAC OS
```
python3.9 -m venv venv
```

```
source venv/bin/activate
```

# Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
### Авторы
Никки и Никонор