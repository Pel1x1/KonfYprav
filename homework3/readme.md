# Установка
1. Установка программы и переход в директорию
   ```bash
   git clone <URL репозитория>
   cd <директория проекта>
   ```
2. Создайте и активируйте виртуальное окружение:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate     # Для Windows
   ```
3. Установите необходимые зависимости :
   ```bash
   Зависимости не требуются
   ```

# Запуск скрипта

Скрипт принимает текст конфигурационного файла через стандартный ввод и выводит xml в стандартный вывод.

```bash
echo 'входные данные' | py hw3.py
```

### Пример 1
```
#стандартный ввод
#echo '$[ name : "Ivan", age : 30, address : "Moscow" ]' | py hw3.py
```
![image](https://github.com/user-attachments/assets/e30e96d0-f374-416e-9c17-5b1e5210b529)

### Пример 2
```
# ввод с +1 полем
#echo '$[ name : "Kostya", age : 19, address : "Russia", sport: "Football" ]' | py hw3.py
```
![image](https://github.com/user-attachments/assets/b285891c-de60-4584-ab97-90c06061f998)


### Пример 3
```
# ввод с комментрарием
#echo '/*\nЭто пример конфигурации пользователя\nСодержит информацию о пользователе и его предпочтениях\n*/$[name : "Alex", age : 25, city : "Novosibirsk" ]' | py hw3.py
```
![image](https://github.com/user-attachments/assets/0a2daca8-30b1-4959-af38-b78c92fe3a12)

### Пример 4
```
# ввод с ошибкой в синтаксисе
#echo '$[ age : 80, address : "Italia",  : "Mia", food: "Pizza" ]' | py hw3.py  
```
![image](https://github.com/user-attachments/assets/5202a6a9-5c62-4923-843e-a60dfc365818)


### Пример 5
```
# ввод с ошибкой в кодировке
#echo '$[ name : "Ванёк", age : 31, address : "МСК" ]' | py hw3.py 
```
# ввод с ошибкой в кодировке
#echo '$[ name : "Ванёк", age : 31, address : "МСК" ]' | py hw3.py 


# Тесты

Шаги запуска тестов:
1. Установить библиотеку pytest (необходимо, если не сделано ранее):
   ```bash
   pip install pytest
   ```
   
2. Для запуска тестирования необходимо запустить следующий скрипт:
   ```shell
   py unittests.py
   ```

## Прохождение тестов:
![image](https://github.com/user-attachments/assets/785fcee7-2ab0-4fb0-84cd-f32518086fd0)
