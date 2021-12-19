# day16_1.py

def get_input(filename: str):
    with open(filename) as f:
        return f.readline()


def decode(filename) -> list:
    hex_message = get_input(filename)
    bin_message = str(bin(int(hex_message, 16)))[2:].zfill(len(hex_message * 4))
    bit_generator = get_next_bit(bin_message)
    packet_list = []
    while True:
        try:
            packet = get_packet(bit_generator)
            packet_list.append(packet)
        except StopIteration as error:
            print(f"Whole stream was probably read.\n {error}")
            break
    return packet_list


def get_packet(bit_gen):
    packet = {"version": get_packet_version(bit_gen), "p_type": get_packet_type(bit_gen)}
    if 4 == packet["p_type"]:
        number = get_literal(bit_gen)
        packet["number"] = number
    else:
        packet["sub_packets"] = []
        length_type = get_length_type(bit_gen)
        if "0" == length_type:
            length = get_sub_packets_length(bit_gen)
            sub_packets_gen = iter([next(bit_gen) for _ in range(length)])
            while True:
                try:
                    packet["sub_packets"].append(get_packet(sub_packets_gen))
                except StopIteration:
                    break
        elif "1" == length_type:
            sub_packets_count = get_sub_packets_count(bit_gen)
            for i in range(sub_packets_count):
                packet["sub_packets"].append(get_packet(bit_gen))
    return packet


def get_sub_packets_count(bit_gen):
    return get_field_int(bit_gen, 11)


def get_sub_packets_length(bit_gen):
    return get_field_int(bit_gen, 15)


def get_literal(bit_gen):
    read_more = True
    number = ''
    numbers_count = 0
    while read_more:
        read_more = bool(get_field_int(bit_gen, 1))
        number += get_field_bits(bit_gen, 4)
        numbers_count += 1
    # skip_fields(bit_gen, (3 + 3 + 5 * numbers_count) % 4)
    return int(number, 2)


def get_packet_version(bit_gen):
    return get_field_int(bit_gen, 3)


def get_packet_type(bit_gen):
    return get_field_int(bit_gen, 3)


def get_length_type(bit_gen):
    return get_field_bits(bit_gen, 1)


def get_field_int(bit_gen, bit_count):
    field = get_field_bits(bit_gen, bit_count)
    return int(field, 2)


def get_field_bits(bit_gen, bit_count):
    return "".join([next(bit_gen) for _ in range(bit_count)])


def get_next_bit(binary_message):
    for bit in binary_message:
        yield bit


def skip_fields(bit_gen, bit_count):
    for bit in range(bit_count):
        next(bit_gen)


def add_versions(outer_packet):
    version_sum = 0
    for packet in outer_packet:
        if "sub_packets" in packet:
            version_sum += add_versions(packet["sub_packets"])
        version_sum += packet["version"]
    return version_sum


if __name__ == "__main__":
    packets = decode("input.txt")
    print(packets)
    print(add_versions(packets))
