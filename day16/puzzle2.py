# https://adventofcode.com/2021/day/16

from typing import Tuple


def main():
    # hex = ""
    # with open("input.txt") as file:
    #     for line in file:
    #         hex = line.strip()

    # binary_str = hexToBinary(hex)
    binary_str = "0010001000000000101100111000000000110001000011110110001000000100010010000001000000000001011010110000110011100010010000"
    print(decode_packet(binary_str))


def find_literal_value(binary_str: str) -> Tuple[int, str]:
    binary_ret = ""
    i = 0
    while i <= len(binary_str) - 5:
        do_break = False
        next_5 = binary_str[i:i + 5]
        if next_5[0] == "0":
            do_break = True
        binary_ret += next_5[1:]

        i += 5

        if do_break:
            break

    return binary_to_number(binary_ret), binary_str[i:]


def decode_packet(binary_str: str) -> Tuple[int, str]:
    version = determine_version(binary_str)
    type = determine_type(binary_str)
    payload = binary_str[6:]

    if type == 4:  # literal packet
        literal_value, rest_of_binary = find_literal_value(payload)
        print(literal_value)
        return literal_value, rest_of_binary

    length_type = int(binary_str[6])
    payload = binary_str[7:]

    total_subpacket_length = None
    total_number_of_subpackets = None

    if length_type == 0:
        total_subpacket_length = binary_to_number(payload[0:15])
        payload = payload[15:]
    else:
        total_number_of_subpackets = binary_to_number(payload[0:11])
        payload = payload[11:]

    packet_values = 0
    previous_value = None
    read_number_of_subpackets = 0
    read_subpacket_length = 0

    while should_continue(read_number_of_subpackets, read_subpacket_length, total_number_of_subpackets, total_subpacket_length):

        packet_value, new_payload = decode_packet(payload)
        read_number_of_subpackets += 1
        read_subpacket_length += len(payload) - len(new_payload)

        if type == 0:  # sum packet
            if packet_values == 0:
                packet_values = packet_value
            else:
                packet_values += packet_value
        elif type == 1:  # product packet
            if packet_values == 0:
                packet_values = packet_value
            else:
                packet_values *= packet_value
        elif type == 2:  # minimum packet
            if packet_values == 0:
                packet_values = packet_value
            elif packet_value < packet_values:
                packet_values = packet_value
        elif type == 3:  # maximum packet
            if packet_values == 0:
                packet_values = packet_value
            elif packet_value > packet_values:
                packet_values = packet_value
        # elif type == 4 is before this (literal packet)
        elif type == 5:  # greater than packet
            if previous_value is None:
                previous_value = packet_value
            elif previous_value > packet_value:
                packet_values = 1
        elif type == 6:  # less than packet
            if previous_value is None:
                previous_value = packet_value
            elif previous_value < packet_value:
                packet_values = 1
        elif type == 7:  # equal to packet
            if previous_value is None:
                previous_value = packet_value
            elif previous_value == packet_value:
                packet_values = 1

        payload = new_payload

    return packet_values, payload

def should_continue(read_number_of_subpackets: int, read_subpacket_length: int, total_number_of_subpackets: int, total_subpacket_length: int):
    if total_number_of_subpackets is not None and read_number_of_subpackets >= total_number_of_subpackets:
        return False
    if total_subpacket_length is not None and read_subpacket_length >= total_subpacket_length:
        return False

    return True

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


def hexToBinary(hex: str) -> str:
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
