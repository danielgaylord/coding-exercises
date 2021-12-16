import unittest

# Read puzzle input and return as usable data structure
def parse_input(file):
    hex_vals = []
    with open(file, 'r') as input:
        for line in input:
            hex_vals.extend([char for char in line.rstrip()])
    return hex_vals

def get_ver_ID(packet):
    version = int(packet[0:3], 2)
    typeID = int(packet[3:6], 2)
    return version, typeID, packet[6:]

def get_lit_val(packet):
    lit_val = ""
    while packet[0] == "1":
        lit_val += "".join(packet[1:5])
        packet = packet[5:]
    lit_val += "".join(packet[1:5])
    packet = packet[5:]
    return int(lit_val, 2)


def packet_decoder(file):
    hex_vals = parse_input(file)
    packet = f'{int("".join(hex_vals), 16):0>{4 * len(hex_vals)}b}'
    total_ver = 0
    
    version, typeID, packet = get_ver_ID(packet)
    total_ver += version
    if typeID == 4:
        get_lit_val(packet)
    else:
        pass


    return total_ver

# Practicing unit testing on given test input and expected results
class Day16Tests(unittest.TestCase):
    def test_packet_decoder_part1(self):
        self.assertEqual(packet_decoder('Advent of Code/test.txt'), 16)
    
    def test_packet_decoder_part2(self):
        self.assertEqual(packet_decoder('Advent of Code/test.txt'), 16)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    print(packet_decoder('Advent of Code/test.txt'))
    #print(packet_decoder('Advent of Code/2021-Day16.txt'))
    
    # Part 2 solution
    #print(packet_decoder('Advent of Code/test.txt'))
    #print(packet_decoder('Advent of Code/2021-Day16.txt'))
        