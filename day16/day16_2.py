# day16_2.py
from day16_1 import decode
from math import prod


def perform_operations_on_packets(outer_packet):
    packets_values = []
    for packet in outer_packet["sub_packets"]:
        if packet["p_type"] == 4:
            packets_values.append(packet["number"])
        else:
            packets_values.append(perform_operations_on_packets(packet))

    result = 0
    match outer_packet["p_type"]:
        case 0:
            result = sum(packets_values)
        case 1:
            result = prod(packets_values)
        case 2:
            result = min(packets_values)
        case 3:
            result = max(packets_values)
        case 5:
            result = int(packets_values[0] > packets_values[1])
        case 6:
            result = int(packets_values[0] < packets_values[1])
        case 7:
            result = int(packets_values[0] == packets_values[1])

    return result


if __name__ == "__main__":
    packets = decode("input.txt")
    print(packets)
    print(perform_operations_on_packets(packets[0]))
