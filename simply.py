PRINT_TIM    = 1
HALT         = 2
PRINT_NUM    = 3
PRINT_SUM    = 4
SAVE         = 5
ADD          = 6
PUSH         = 7
POP          = 8
PRINT_REG    = 9
CALL         = 10
RET          = 11
 ​
ram = [0] * 256
registers = [0] * 8 
​
PC = 0
running = True
​
registers[7] = 255 # SP, in cpu.py F3
​
def load_memory(filename):
    address = 0
    try:
        with open(filename) as file:
            for line in file:
                comment_split = line.split('#')
                possible_number = comment_split[0]
​
                if possible_number == '' or possible_number == '\n':
                    continue
                instruction = int( possible_number)
                ram[address] = instruction
                address += 1

    except IOError:  
        print('I cannot find that file, check the name')
        sys.exit(2)
​
program = [
    PRINT_TIM,
    PRINT_NUM,
    99,
    SAVE,
    2,
    99,
]
​
load_memory(sys.argv[1])
​
# def ram_read()

# def ram_write()

while running:
    command = ram[PC]
​
    if command == PRINT_TIM:
        print('Tim!')
        PC += 1
​
    elif command == PRINT_NUM:
        num = ram[PC + 1]
        print(num)
        PC += 2
​
    elif command == PRINT_SUM:
        first_number = ram[PC + 1]
        second_number = ram[PC + 2]
        print(first_number + second_number)
        PC += 3
​
    elif command == SAVE:
        register = ram[PC + 1]
        number_to_save = ram[PC + 2]
        registers[register] = number_to_save
        PC += 3
​
    elif command == ADD:
        first_register = ram[PC + 1]
        second_register = ram[PC + 2]
        sum = registers[first_register] + registers[second_register]
        registers[first_register] = sum
        PC += 3
​
    elif command == PUSH:
        registers[7] = ( registers[7] -1) % 255
        SP = registers[7]
        # registers[7] = ( SP - 1 ) % 255
​
        register_address = ram[PC + 1]
        value = registers[register_address]
​
        ram[SP] = value
        PC += 2
​
    elif command == POP:
        SP = registers[7]
​
        value = ram[SP]
        register_address = ram[PC + 1]
        registers[register_address] = value
​
       
        registers[7] = ( SP + 1 ) % 255
​
        PC += 2

    elif command == PRINT_REG:
        register_address = ram[pc + 1]
        value_to_print = registers[register_address]
        print(value_to_print)
        pc += 2
​
    elif command == CALL:
        register_address = ram[PC + 1]
        address_to_jump_to = registers[register_address]
        
        # store the address of the next instruction
        next_instruction_address =  PC + 2
        
        registers[7] = (registers[7] -1) % 255
        SP = registers[7]
        ram[SP] = next_instruction_address


        PC = address_to_jump_to

        # set pc to the address to jump to

    elif command == RET:
        SP = registers[7]
        address_to_return_to = ram[SP]

        PC = address_to_return_to

    elif command == HALT:
        running = False
​
    else:
        print('command not recognized: {}'.format(command))
        running = False


# what was the next thing that was to be done after call
# remember the next step after call was run
