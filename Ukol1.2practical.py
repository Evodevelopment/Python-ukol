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

