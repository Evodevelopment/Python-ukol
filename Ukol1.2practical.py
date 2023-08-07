• Implement a function, that will find all odd integer numbers from interval <1; 100 000>, and stores them into a list.
Implementujte funkci, která najde všechny lichá čísla v intervalu <1; 100 000>, a uloží je jako list.

def find_odd_numbers():
    return [num for num in range(1, 100001) if num % 2 != 0]

odd_numbers = find_odd_numbers()
odd_numbers[:10], len(odd_numbers)  # Displaying the first 10 odd numbers and the total count for validation.

#RESULT
([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 50000)

#Implement a function, that generates infinite sequence of odd numbers. 
#Implementujte funkci, která generuje nekonečnou řadu lichých čísel.
def generate_odd_numbers():
    num = 1
    while True:
        if num % 2 != 0:
            yield num
        num += 1

# To demonstrate the generator, let's get the first 10 odd numbers from it.
odd_generator = generate_odd_numbers()
first_10_odd_numbers = [next(odd_generator) for _ in range(10)]
first_10_odd_numbers


#Write a regular expression, that matches protocol, IPv4 address, and port from the string below. There can be any protocol, IPv4 address, and any port on the input. Protocol and port are optional parts and can be missing. For the string below, it must match groups “protocol=udp”, “ipv4=127.0.0.1”, “port=53” :
Napište regulární výraz, který nalezne protokol, IPv4 adresu a port z řetězce níže.
Na vstupu se může vyskytnout libovolný protokol, IPv4 adresa a libovolný port.
Protokol a port jsou volitelné části a nemusí se vyskytnout. V řetězci níže musí regulární výraz najít skupiny “protocol=udp”, “ipv4=127.0.0.1”, “port=53”:
 “udp://127.0.0.1:53”

import re

input_string = "udp://127.0.0.1:53"
pattern = r"(?:(protocol=[a-zA-Z]+)://)?(ipv4=\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?::(port=\d+))?"

matches = re.search(pattern, input_string)

if matches:
    matched_groups = matches.groups()
else:
    matched_groups = None

matched_groups


#
