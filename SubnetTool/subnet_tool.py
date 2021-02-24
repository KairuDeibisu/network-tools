import sys


def calculate_number_zeros(octet: bytes) -> int:
    """
    Number of zeros in a single octet
    """
    zeros = [zero for zero in octet[2:] if zero == '0']

    if len(zeros) == 1:
        return 8

    return len(zeros)


def hosts_formula(h: int) -> int:
    """
    how many hosts will be allowed on a network that has a certain subnet mask
    """
    return 2 ** h - 2


def decimal_to_binary(subnet) -> tuple[str]:
    """
    format subnet as binary string
    """
    return tuple(bin(int(octet)) for octet in subnet.split("."))


def calculate_number_hosts(subnet):
    """
    number of hosts that a subnet can hold
    """
    octets = decimal_to_binary(subnet)
    total_zeros = [calculate_number_zeros(octet) for octet in octets]
    return hosts_formula(sum(total_zeros))


def main(args=None):

    if len(args) < 2:
        print("Usage: subnet_tools subnet")
        return 1

    subnet = args[-1]

    host = calculate_number_hosts(subnet)

    print(f"\n{subnet} can have {host} hosts\n")


if __name__ == "__main__":
    exit(main(sys.argv))
