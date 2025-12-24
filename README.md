# ISO 14443 State Machine
A representation of the ISO 14443 state machine. 

Built to learn the ISO 14443 protocol's methods.

## Usage
`python3 main.py`

To use it, select a machine state and the applicable opcode. 

Some opcodes (`ANTICOLLISION` and `SELECT`) require cascade level parameters represented by their hex values. 

The program prints out the opcode and its parameters in this format: `Hex: [PARAMETER] [OPCODE]`

Sample output: `Hex:  0x20 0x95`