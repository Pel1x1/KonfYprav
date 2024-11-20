import sys
import re

def parse_dictionary(input_text):
    input_text = re.sub(r'/\*.*?\*/', '', input_text, flags=re.DOTALL)

    input_text = re.sub(r'//.*', '', input_text)

    input_text = input_text.strip()

    if not input_text.startswith('$[') or not input_text.endswith(']'):
        raise SyntaxError("Ошибка: Неверный синтаксис. Ожидалось начало '$[' и конец ']'.")

    content = input_text[2:-1].strip()

    entries = content.split(',')
    result = '<dictionary>\n'
    
    for entry in entries:
        entry = entry.strip()
        if ':' not in entry:
            raise SyntaxError(f"Ошибка: Неверный синтаксис в записи: '{entry}'. Ожидалось 'имя : значение'.")
        
        key, value = entry.split(':', 1)
        key = key.strip()
        value = value.strip().strip('"') 

        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', key):
            raise SyntaxError(f"Ошибка: Неверное имя '{key}'. Имя должно начинаться с буквы или '_'.")
        
        result += f'    <entry key="{key}">{value}</entry>\n'

    result += '</dictionary>'
    return result

def main():
    input_text = sys.stdin.read()
    try:
        output = parse_dictionary(input_text)
        print(output)
    except SyntaxError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()

# стандартный ввод
#echo '$[ name : "Ivan", age : 30, address : "Moscow" ]' | py hw3.py
# ввод с +1 полем
#echo '$[ name : "Kostya", age : 19, address : "Russia", sport: "Football" ]' | py hw3.py
# ввод с комментрарием
#echo '/*\nЭто пример конфигурации пользователя\nСодержит информацию о пользователе и его предпочтениях\n*/$[name : "Alex", age : 25, city : "Novosibirsk" ]' | py hw3.py
# ввод с ошибкой в синтаксисе
#echo '$[ age : 80, address : "Italia",  : "Mia", food: "Pizza" ]' | py hw3.py  
# ввод с ошибкой в кодировке
#echo '$[ name : "Ванёк", age : 31, address : "МСК" ]' | py hw3.py 
