import struct
import csv
import sys

def read_bin_file(bin_file):
    #Читает бинарный файл и извлекает инструкции
    with open(bin_file, 'rb') as f:
        content = f.read()
    return content

def execute_instruction(instruction):
    #Выполняет инструкцию на основе данных
    opcode = instruction[0]
    vector = instruction[1:-4]
    number_bytes = bytes(instruction[-4:])  # Преобразуем последние 4 элемента в bytes
    
    # Декодируем число
    number = struct.unpack('I', number_bytes)[0]
    
    if opcode == 0x01:  # XOR
        return [x ^ number for x in vector]
    elif opcode == 0x02:  # OR
        return [x | number for x in vector]
    return vector

def interpreter(bin_file, result_file, memory_range):
    #Интерпретирует бинарный файл и записывает результат в CSV
    content = read_bin_file(bin_file)
    
    instructions = []
    i = 0
    vector_length = 9  # вектор длины 9 или меньше
    while i < len(content):
        opcode = content[i]
        vector = list(content[i+1:i+1+vector_length])  # Преобразуем байты в список чисел
        number = content[i+1+vector_length:i+5+vector_length]
        
        instructions.append([opcode] + vector + list(number))  # Преобразуем число в список
        i += 5 + vector_length  # Переходим к следующей инструкции
    
    # Запуск интерпретации
    results = []
    for instruction in instructions:
        result_vector = execute_instruction(instruction)
        results.append(result_vector)
    
    # Запись результатов в CSV
    with open(result_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(results)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: py interpreter.py <output.bin> <result.csv>")
        sys.exit(1)
    
    bin_file = sys.argv[1]
    result_file = sys.argv[2]
    
    interpreter(bin_file, result_file, memory_range=None)
