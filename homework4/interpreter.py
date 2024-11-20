def interpret(binary_file, result_file):
    stack = []
    memory = [0] * 256  # Пример памяти размером 256 байт
    
    with open(binary_file, 'rb') as f:
        while True:
            byte = f.read(1)
            if not byte:
                break
            
            opcode = struct.unpack('>B', byte)[0]
            
            if opcode == 0x94:  # LOAD_CONST
                const_value = struct.unpack('>H', f.read(2))[0]
                stack.append(const_value)
            elif opcode == 0x07:  # READ_MEM
                offset = struct.unpack('>H', f.read(2))[0]
                if not stack:
                    print("Ошибка: стек пуст перед операцией READ_MEM.")
                    return
                address = stack.pop() + offset
                stack.append(memory[address])
            elif opcode == 0x97:  # WRITE_MEM
                offset = struct.unpack('>H', f.read(2))[0]
                if len(stack) < 2:
                    print("Ошибка: недостаточно элементов в стеке для WRITE_MEM.")
                    return
                value_to_write = stack.pop()
                address = stack.pop() + offset
                memory[address] = value_to_write
            elif opcode == 0x34:  # XOR
                if len(stack) < 2:
                    print("Ошибка: недостаточно элементов в стеке для XOR.")
                    return
                value1 = stack.pop()
                value2 = stack.pop()
                stack.append(value1 ^ value2)

    with open(result_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(memory)):
            writer.writerow([i, memory[i]])