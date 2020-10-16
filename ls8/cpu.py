"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram[0] * 256
        self.reg = [0] * 8
        self.PC = 0
        self.SP = 0xF3
        pass

    def ram_read(self, MAR):
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        try:
            with open(filename) as file:
                for line in file:
                    comment_split = line.split('#')
                    possible_number = comment_split[0]
                    if possible_number == '' or possible_number == '\n':
                        continue
                    instruction = int( possible_number)
                    self.ram[address] = instruction
                    address += 1

        except IOError:  
            print('I cannot find that file, check the name')
            sys.exit(2)

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            mul = self.reg[reg_a] * self.reg[reg_b]
            self.reg[reg_a] = mul
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        LDI = 0b10000010
        PRN = 0b01000111
        HLT = 0b00000001
        MUL = 0b10100010
        # day 3
        PUSH = 0b01000101
        POP = 0b01000110

        running = True

        while running:
            command = self.ram[self.PC]
            a = self.ram_read(self.PC + 1)
            b = self.ram_read(self.PC + 2)

            if command == LDI:
                self.reg[a] = b
                self.PC += 3
            elif command == PRN:
                print(self.reg[a])
                self.PC += 2
            elif command == MUL:
                self.alu("MUL", a,b)
                self.PC += 3
            elif command == PUSH:
                SP = (SP % 255) - 1
                self.ram[SP] = self.reg[a]
                self.PC += 2
            elif command == POP:
                self.reg[a] = self.ram[SP]
                SP = (SP % 255) + 1
                self.PC += 2

            elif command == HLT:
                running = False
            else:
                print('Command not recognized')
                running = False
    


    pass
            # elif command == CALL:
            #     print('call')