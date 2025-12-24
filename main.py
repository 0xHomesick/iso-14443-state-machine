from enum import Enum, Flag
import inquirer

class State (Enum):
    IDLE:str = "Idle"
    READY:str = "Ready"
    ACTIVE:str = "Active"
    HALT:str = "Halt"
    
class Opcode(Enum):
    REQA:hex = 0x26
    WUPA:hex = 0x52
    HLTA:hex = 0X50 #parameter 0X00
    ANTICOLLISION:hex = 0x20 #parameter 0x93, 0x95, 0x97 (cascade levels)
    SELECT:hex = 0x70 #same params as anticollision
    
def select_state()->State:
    state = inquirer.list_input("Select state", choices=[state.name for state in State])
    return State[state]


def select_opcode(state:State)->Opcode:
    match state.name:
        case "IDLE":
            opcode = inquirer.list_input("Select opcode", choices=[op.name for op in Opcode if op.name in {"REQA", "WUPA"}])
        case "READY":
            opcode = inquirer.list_input("Select opcode", choices=[op.name for op in Opcode if op.name in {"ANTICOLLISION"}])
        case "ACTIVE":
            opcode = inquirer.list_input("Select opcode", choices=[op.name for op in Opcode if op.name in {"SELECT"}])
        case "HALT":
            opcode = inquirer.list_input("Select opcode", choices=[op.name for op in Opcode if op.name in {"WUPA"}])
        case _:
            pass
    return Opcode[opcode]


def select_parameters(opcode:Opcode)->int:
    cascade_choices = [0x93, 0x95, 0x97]
    match opcode.name:
        case "REQA":
            pass
        case "WUPA":
            pass
        case "HTLA":
            opcode = 0x00
        case "ANTICOLLISION":
            return inquirer.list_input("Select parameter", choices=[hex(param) for param in cascade_choices])
        case "SELECT":
            return inquirer.list_input("Select parameter", choices=[hex(param) for param in cascade_choices])
        case _:
            pass

def main():
    while (True):
        state = select_state()
        opcode = select_opcode(state)
        parameter = select_parameters(opcode)
        print("Hex: ", parameter, hex(opcode.value), "\n")
    

if __name__ == "__main__":
    main()