def combo(operand, registers):
    if operand <= 3:
        return operand
    if operand <= 6:
        return registers[operand - 4]


def process(registers, program, instruction_pointer, out):
    opcode = program[instruction_pointer]
    operand = program[instruction_pointer + 1]
    combo_operand = combo(operand, registers)
    if opcode == 0:
        registers[0] = int(registers[0] / 2**combo_operand)
    elif opcode == 1:
        registers[1] = registers[1] ^ operand
    elif opcode == 2:
        registers[1] = combo_operand % 8
    elif opcode == 3 and registers[0] != 0:
        instruction_pointer = operand
        return registers, instruction_pointer, out
    elif opcode == 4:
        registers[1] = registers[1] ^ registers[2]
    elif opcode == 5:
        out.append(combo_operand % 8)
    elif opcode == 6:
        registers[1] = int(registers[0] / 2**combo_operand)
    elif opcode == 7:
        registers[2] = int(registers[0] / 2**combo_operand)
    instruction_pointer += 2
    return registers, instruction_pointer, out


with open("input.txt", "r") as file:
    registers_raw, program_raw = file.read().strip().split("\n\n")
registers = [int(rr.split(": ")[1]) for rr in registers_raw.split("\n")]
program = [int(x) for x in program_raw.split(": ")[1].split(",")]
instruction_pointer = 0
out = []
while instruction_pointer < len(program):
    registers, instruction_pointer, out = process(
        registers, program, instruction_pointer, out
    )
out = ",".join([str(x) for x in out])
print(out)
