# https://adventofcode.com/2021/day/16

from typing import Tuple


def main():
    hex = ""
    with open("input.txt") as file:
        for line in file:
            hex = line.strip()
            
    binary_str = hexToBinary(hex)
    print(decode_packet(binary_str))

def find_literal_hex_value(hex: str) -> Tuple[int, str]:
    binary_ret = ""
    i = 0
    while i < len(hex) - 5:
        do_break = False
        next_5 = hex[i:i + 5]
        if next_5[0] == "0":
            do_break = True
        binary_ret += next_5[1:]

        i += 5

        if do_break:
            break
    
    return binary_to_number(binary_ret), hex[i:]

def decode_packet(binary_str:str) -> Tuple[int, str]:
    version = determine_version(binary_str)
    type = determine_type(binary_str)
    payload = binary_str[6:]
    

    if type == 4:
        literal_value, rest_of_hex = find_literal_hex_value(payload)
        return version, rest_of_hex

    length_type = int(binary_str[6])
    payload = binary_str[7:]

    total_subpacket_length = None
    number_of_subpackets = None

    if length_type == 0:
        total_subpacket_length = binary_to_number(payload[0:15])
        payload = payload[15:]
    else:
        number_of_subpackets = binary_to_number(payload[0:11])
        payload = payload[11:]
    
    sum_of_versions = version
    print(version)
    while len(payload) > 6:
        new_sum_of_versions, new_payload = decode_packet(payload)
        print(new_sum_of_versions)
        sum_of_versions += new_sum_of_versions
        payload = new_payload

    return sum_of_versions, payload
    

    

def binary_to_number(hex: str) -> int:
    ret = 0
    power = len(hex) - 1
    for i in range(0, len(hex)):
        ret += int(hex[i]) * (2 ** (power - i)) 
    return ret

def determine_version(hex: str) -> int:
    first_three_characters = hex[0:3]
    return binary_to_number(first_three_characters)

def determine_type(hex: str) -> int:
    next_three_characters = hex[3:6]
    return binary_to_number(next_three_characters)

def hexToBinary(hex:str) -> str:
    hexDict = dict()
    hexDict["0"] = "0000"
    hexDict["1"] = "0001"
    hexDict["2"] = "0010"
    hexDict["3"] = "0011"
    hexDict["4"] = "0100"
    hexDict["5"] = "0101"
    hexDict["6"] = "0110"
    hexDict["7"] = "0111"
    hexDict["8"] = "1000"
    hexDict["9"] = "1001"
    hexDict["A"] = "1010"
    hexDict["B"] = "1011"
    hexDict["C"] = "1100"
    hexDict["D"] = "1101"
    hexDict["E"] = "1110"
    hexDict["F"] = "1111"
    ret = ""

    for char in hex:
        ret += hexDict[char]
    return ret
    

main()
