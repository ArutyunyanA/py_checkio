""""We need to fly home as cheaply as possible so that more money is left for gifts. 
Aunt Lidia asked for different kinds of cheeses, and Vasia wanted a new toy car. 
I’ve been looking at the schedule for quite a while and I’m starting to think that 
some planes are flying in vain".

As the input you get the flight schedule as an list, each element of which 
is the price of a direct flight between 2 cities (list of 3 elements - 2 city 
names as a string, and a flight price).

Planes fly in both directions and the price in both directions is the same. There is 
a possibility that there are no direct flights between cities.

Find the price of the cheapest flight between cities that are given as the 2nd 
and 3rd arguments. In case the flight can not be performed, return 0.
"""

def cheapest_flight(costs: list, a: str, b: str) -> int:
    # your code here
    return 0


print("Example:")
print(cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C"))

# These "asserts" are used for self-checking
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C") == 70
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A") == 70
)
assert (
    cheapest_flight(
        [
            ["A", "C", 40],
            ["A", "B", 20],
            ["A", "D", 20],
            ["B", "C", 50],
            ["D", "C", 70],
        ],
        "D",
        "C",
    )
    == 60
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F") == 0
)
assert (
    cheapest_flight(
        [["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D"
    )
    == 25
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
