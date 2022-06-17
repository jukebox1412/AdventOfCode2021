# https://adventofcode.com/2021/day/16

from typing import Tuple


def main():
    hex = "220D69802BE00A0803711E1441B1006E39C318A12730C200DCE66D2CCE360FA0055652CD32966E3004677EDF600B0803B1361741510076254138D8A00E4FFF3E3393ABE4FC7AC10410010799D2A4430003764DBE281802F3102CA00D4840198430EE0E00021D04E3F41F84AE0154DFDE65A17CCBFAFA14ADA56854FE5E3FD5BCC53B0D2598027A00848C63F2B918C7E513DEC3290051B3867E009CCC5FE46BD520007FE5E8AD344B37583D0803E40085475887144C01A8C10FE2B9803B0720D45A3004652FD8FA05F80122CAF91E5F50E66BEF8AB000BB0F4802039C20917B920B9221200ABF0017B9C92CCDC76BD3A8C4012CCB13CB22CDB243E9C3D2002067440400D9BE62DAC4D2DC0249BF76B6F72BE459B279F759AE7BE42E0058801CC059B08018A0070012CEC045BA01006C03A8000D46C02FA000A8EA007200800E00618018E00410034220061801D36BF178C01796FC52B4017100763547E86000084C7E8910AC0027E9B029FE2F4952F96D81B34C8400C24AA8CDAF4F1E98027C00FACDE3BA86982570D13AA640195CD67B046F004662711E989C468C01F1007A10C4C8320008742287117C401A8C715A3FC2C8EB3777540048272DFE7DE1C0149AC8BC9E79D63200B674013978E8BE5E3A2E9AA3CCDD538C01193CFAB0A146006AA00087C3E88B130401D8E304A239802F39FAC922C0169EA3248DF2D600247C89BCDFE9CA7FFD8BB49686236C9FF9795D80C0139BEC4D6C017978CF78C5EB981FCE7D4D801FA9FB63B14789534584010B5802F3467346D2C1D1E080355B00424FC99290C7E5D729586504803A2D005E677F868C271AA479CEEB131592EE5450043A932697E6A92C6E164991EFC4268F25A294600B5002A3393B31CC834B972804D2F3A4FD72B928E59219C9C771EC3DC89D1802135C9806802729694A6E723FD6134C0129A019E600"
    # with open("input.txt") as file:
    #     for line in file:
    #         hex = line.strip()

    binary_str = hexToBinary(hex)
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
