import sys
import struct
#py assembler.py input.asm output.bin log.txt
#py interpreter.py output.bin result.csv

def assemble(input_file, output_file, log_file):
    instructions = []
    with open(input_file, 'r') as f:
        for line in f:
            # Удаляем комментарии и лишние пробелы
            line = line.split(';')[0].strip()
            if not line:  # Пропускаем пустые строки
                continue
            
            parts = line.split()
            command = parts[0]
            operands = list(map(int, parts[1:]))
            
            if command == "LOAD_CONST":
                instructions.append(struct.pack('>B', 0x94))  # LOAD_CONST opcode
                instructions.append(struct.pack('>H', operands[0]))  # Constant
                instructions.append(struct.pack('>H', 0))  # Padding
            elif command == "READ_MEM":
                instructions.append(struct.pack('>B', 0x07))  # READ_MEM opcode
                instructions.append(struct.pack('>H', operands[0]))  # Offset
                instructions.append(struct.pack('>H', 0))  # Padding
            elif command == "WRITE_MEM":
                instructions.append(struct.pack('>B', 0x97))  # WRITE_MEM opcode
                instructions.append(struct.pack('>H', operands[0]))  # Offset
                instructions.append(struct.pack('>H', 0))  # Padding
            elif command == "XOR":
                instructions.append(struct.pack('>B', 0x34))  # XOR opcode
                instructions.append(struct.pack('>H', 0))  # Padding
                instructions.append(struct.pack('>H', 0))  # Padding

    with open(output_file, 'wb') as f:
        for instr in instructions:
            f.write(instr)

    with open(log_file, 'w') as log:
        for i, instr in enumerate(instructions):
            log.write(f"Instruction {i}: {instr.hex()}\n")

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    log_file = sys.argv[3]
    assemble(input_file, output_file, log_file)
