import struct
import sys

def assemble_instruction(operation, vector, number):
    #Преобразует команду в машинную инструкцию
    opcode = {'xor': 0x01, 'or': 0x02}.get(operation, 0x00)
    vector_bytes = struct.pack(f'{len(vector)}B', *vector)
    number_bytes = struct.pack('I', number)
    return [opcode] + list(vector_bytes) + list(number_bytes)

def parse_asm(file_path):
    #Парсит входной файл 
    instructions = []
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if parts:
                operation = parts[0]
                vector = list(map(int, parts[1].strip('[]').split(',')))
                number = int(parts[2])
                instructions.append((operation, vector, number))
    return instructions

def write_bin_file(instructions, output_file):
    #Записывает инструкции в бинарный файл
    with open(output_file, 'wb') as f:
        for instruction in instructions:
            f.write(bytearray(instruction))

def write_log(instructions, log_file):
    # Записывает лог
    with open(log_file, 'w') as f:
        for i, (operation, vector, number) in enumerate(instructions):
            f.write(f'A = {number}\n')
            f.write(f'Vector = {vector}\n')
            f.write(f'Operation = {operation}\n\n')

def assembler(asm_file, bin_file, log_file):
    #Главная функция
    instructions = []
    asm_instructions = parse_asm(asm_file)
    
    for operation, vector, number in asm_instructions:
        machine_code = assemble_instruction(operation, vector, number)
        instructions.append(machine_code)
    
    write_bin_file(instructions, bin_file)
    write_log(asm_instructions, log_file)
    print(f'Ассемблер завершил работу. Бин: {bin_file}, Лог: {log_file}')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: py assembler.py <task.asm> <output.bin> <log.txt>")
        sys.exit(1)
    
    asm_file = sys.argv[1]
    bin_file = sys.argv[2]
    log_file = sys.argv[3]
    
    assembler(asm_file, bin_file, log_file)
