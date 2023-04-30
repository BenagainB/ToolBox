#SubnetCalculator.py

def convert_binary_to_decimal(binary):
    bin_octet = []
    if "." in binary:
        bin_octet = binary.split(".")
        dec_octet = []
        for section in bin_octet:
            j = 7
            temp = 0
            for i in range(0,8):
                if section[i] == '1':
                    temp = temp + 2**j
                j -= 1
            dec_octet.append(temp)
        converted = ("".join(str(dec_octet[0]) + "." + str(dec_octet[1]) +
                             "." + str(dec_octet[2]) + "." + str(dec_octet[3])))
        return converted
    else:
        bin_octet.append(binary[0:8])
        bin_octet.append(binary[8:16])
        bin_octet.append(binary[16:24])
        bin_octet.append(binary[24:32])
        dec_octet = []
        for section in bin_octet:
            j = 7
            temp = 0
            for i in range(0,8):
                if section[i] == '1':
                    temp = temp + 2**j
                j -= 1
            dec_octet.append(temp)
        converted = ("".join(str(dec_octet[0]) + "." + str(dec_octet[1]) +
                             "." + str(dec_octet[2]) + "." + str(dec_octet[3])))
        return converted

def convert_decimal_to_binary(decimal):
    temp_array = decimal.split(".")
    dec_octet = [int(i) for i in temp_array]
    bin_complete = []
    for i in range(0,4):
        bin_octet = ""
        dec_int = dec_octet[i]
        if dec_int > 127:
            bin_octet = bin_octet + '1'
            dec_int = dec_int - 128
        else:
            bin_octet = bin_octet + '0'
        if dec_int > 63:
            bin_octet = bin_octet + '1'
            dec_int = dec_int - 64
        else:
            bin_octet = bin_octet + '0'
        if dec_int > 31:
            bin_octet = bin_octet + '1'
            dec_int = dec_int - 32
        else:
            bin_octet = bin_octet + '0'
        if dec_int > 15:
            bin_octet = bin_octet + '1'
            dec_int = dec_int - 16
        else:
            bin_octet = bin_octet + '0'
        if dec_int > 7:
            bin_octet = bin_octet + '1'
            dec_int = dec_int - 8
        else:
            bin_octet = bin_octet + '0'
        if dec_int > 3:
            bin_octet = bin_octet + '1'
            dec_int = dec_int - 4
        else:
            bin_octet = bin_octet + '0'
        if dec_int > 1:
            bin_octet = bin_octet + '1'
            dec_int = dec_int - 2
        else:
            bin_octet = bin_octet + '0'
        if dec_int == 1:
            bin_octet = bin_octet + '1'
        else:
            bin_octet = bin_octet + '0'
        bin_complete.append(bin_octet)
    converted = ("".join(bin_complete[0] + "." + bin_complete[1] +
                        "." + bin_complete[2] + "." + bin_complete[3]))
    return converted

def identify_IP_address_class(address):
    #check if dec or bin using regex
    all_octets = address.split('.')
    first_octet = int(all_octets[0])
    if first_octet in range(0,128):
        return 'Class A'
    elif first_octet in range(128, 192):
        return 'Class B'
    elif first_octet in range(192, 224):
        return 'Class C'
    elif first_octet in range(224, 240):
        return 'Class D'
    elif first_octet in range(240, 255):
        return 'Class E'

def determine_max_number_of_hosts(mask):
    bits_for_hosts = 32 - int(mask.replace('/','')) # 32 total bits available
    num_hosts = 2**bits_for_hosts
    num_hosts -= 2  # broadcast and network addresses removed
    return num_hosts

def convert_subnet_mask_short_to_binary(short):
    short = int(short)
    mask_no_dot = ""
    mask_no_dot = "1" * short
    mask_no_dot = mask_no_dot + ("0" * (32-short))
    mask_dot = (mask_no_dot[0:8] + "." + mask_no_dot[8:16] +
                "." + mask_no_dot[16:24] + "." + mask_no_dot[24:32])
    return mask_dot

def calculate_network_address(binary_address, subnet_mask):
    network_address = ""
    for i in range(0, len(binary_address)):
        if binary_address[i] == subnet_mask[i]:
            network_address = network_address + binary_address[i]
        else:
            network_address = network_address + '0'
    return network_address

def calculate_host_min_address(network_address):
    octets = network_address.split(".")
    host_min_address = (octets[0] + "." + octets[1] + "." +
                        octets[2] + "." + str(int(octets[3])+1))
    return host_min_address

def calculate_host_max_address(network_address, num_hosts):
    octets = network_address.split(".")
    temp_octet2 = int(octets[2])
    temp_octet3 = int(octets[3])
    #print(int(num_hosts / 256))
    higher_octet = int(num_hosts / 256)
    if temp_octet2 + higher_octet < 256:
        temp_octet2 = temp_octet2 + higher_octet
    temp_octet3 = temp_octet3 + (num_hosts - higher_octet * 256)
    """host_max_address = (octets[0] + "." + octets[1] + "." +
                        octets[2] + "." + str(int(octets[3])+ num_hosts))"""
    host_max_address = (octets[0] + "." + octets[1] + "." +
                        str(temp_octet2) + "." + str(temp_octet3))
    return host_max_address

def calculate_broadcast_address(host_max_address):
    octets = host_max_address.split(".")
    broadcast_address = (octets[0] + "." + octets[1] + "." +
                        octets[2] + "." + str(int(octets[3])+ 1))
    return broadcast_address

def solve_simple_subnet(address):
    parts = address.split("/")
    #Step1 Convert to Binary
    bin_address = convert_decimal_to_binary(parts[0])
    subnet_mask = convert_subnet_mask_short_to_binary(parts[1])
    #Step2 Calculate the Network (Subnet) Address
    network_address = convert_binary_to_decimal(calculate_network_address(bin_address, subnet_mask))
    num_hosts = determine_max_number_of_hosts(parts[1])
    host_min_address = calculate_host_min_address(network_address)
    host_max_address = calculate_host_max_address(network_address, num_hosts)
    broadcast_address = calculate_broadcast_address(host_max_address)
    return num_hosts, network_address, broadcast_address, host_min_address, host_max_address

print("Section 1: IPv4 Addresses")
print("Question 1")
section1_question1 = '11000000.10101000.00000000.00000001'
print(section1_question1, "converts to:", convert_binary_to_decimal(section1_question1))
print("Question 2")
section1_question2 = '192.172.34.1'
print(section1_question2, "converts to:", convert_decimal_to_binary(section1_question2))
print("Question 3")
section1_question3 = '11100000.00011000.00000001.00001111'
print(section1_question3, "converts to:", convert_binary_to_decimal(section1_question3))
print("Question 4")
section1_question4 = '192.168.1.1'
print(section1_question4, "converts to:", convert_decimal_to_binary(section1_question4))
print("Question 5")
section1_question5 = '192.158.1.3'
print(section1_question5, "converts to:", convert_decimal_to_binary(section1_question5))
print('')

print("Section 2: Identifying IPv4 Classes & Calculating Host")
print("Question 1")
section2_question1 = '192.1.1.0'
print(section2_question1, "belongs to", identify_IP_address_class(section2_question1))
print("Question 2")
section2_question2 = '10.255.255.0'
print(section2_question2, "belongs to", identify_IP_address_class(section2_question2))
print("Question 3")
section2_question3 = '222.224.224.254'
print(section2_question3, "belongs to", identify_IP_address_class(section2_question3))
print("Question 4")
section2_question4 = '4.4.4.4'
print(section2_question4, "belongs to", identify_IP_address_class(section2_question4))
print("Question 5")
section2_question5 = '2.2.2.1'
print(section2_question5, "belongs to", identify_IP_address_class(section2_question5))
print('')

print("Calculating Hosts in CIDR")
print("Question 1")
sectionCIDR_question1 = '/22'
print("maximum number of hosts in a", sectionCIDR_question1 , "is:", determine_max_number_of_hosts(sectionCIDR_question1), "possible hosts")
print("Question 2")
sectionCIDR_question2 = '/16'
print("maximum number of hosts in a", sectionCIDR_question2 , "is:", determine_max_number_of_hosts(sectionCIDR_question2), "possible hosts")
print("Question 3")
sectionCIDR_question3 = '/8'
print("maximum number of hosts in a", sectionCIDR_question3 , "is:", determine_max_number_of_hosts(sectionCIDR_question3), "possible hosts")
print("Question 4")
sectionCIDR_question4 = '/10'
print("maximum number of hosts in a", sectionCIDR_question4 , "is:", determine_max_number_of_hosts(sectionCIDR_question4), "possible hosts")
print("Question 5")
sectionCIDR_question5 = '/19'
print("maximum number of hosts in a", sectionCIDR_question5 , "is:", determine_max_number_of_hosts(sectionCIDR_question5), "possible hosts")
print('')

print("Calculating Simple Subnets")
directions = """You need to determine:
• Number of hosts
• The network address
• The broadcast address
• The host minimum address (AKA the first host address in the subnet)
• The host maximum address (AKA the last host address in the subnet)"""
simple_subnet_parts = ["Number of hosts:", "Network address:", "Broadcast address:", "Host min address:", "Host max address:"]
print(directions, "\n")
simple_subnet_question1 = "192.168.10.44/29"
print("For", simple_subnet_question1)
simple_subnet_answer1 = solve_simple_subnet(simple_subnet_question1)
for i in range(0, len(simple_subnet_parts)):
    print(simple_subnet_parts[i], simple_subnet_answer1[i])
print()

simple_subnet_question2 = "10.10.5.20/18"
print("For", simple_subnet_question2)
simple_subnet_answer2 = solve_simple_subnet(simple_subnet_question2)
for i in range(0, len(simple_subnet_parts)):
    print(simple_subnet_parts[i], simple_subnet_answer2[i])
print()

simple_subnet_question3 = "146.187.130.81/23"
print("For", simple_subnet_question3)
simple_subnet_answer3 = solve_simple_subnet(simple_subnet_question3)
for i in range(0, len(simple_subnet_parts)):
    print(simple_subnet_parts[i], simple_subnet_answer3[i])
print()

simple_subnet_question4 = "145.16.25.18/21"
print("For", simple_subnet_question4)
simple_subnet_answer4 = solve_simple_subnet(simple_subnet_question4)
for i in range(0, len(simple_subnet_parts)):
    print(simple_subnet_parts[i], simple_subnet_answer4[i])
print()

test = "138.101.114.250/25"
print("For", test)
test_answer = solve_simple_subnet(test)
for i in range(0, len(simple_subnet_parts)):
    print(simple_subnet_parts[i], test_answer[i])
#print(solve_simple_subnet(test))
