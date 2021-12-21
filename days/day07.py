from utils.input import Input
from utils import output
positions = Input().list_of_numbers(',')

min_fuel_1 = min_fuel_2 = None

for test_value in range(max(positions) + 1):
    fuel_1 = sum([abs(x-test_value) for x in positions])
    if not min_fuel_1 or min_fuel_1 > fuel_1:
        min_fuel_1 = fuel_1
    fuel_2 = sum([sum(range((abs(x-test_value)) + 1)) for x in positions])
    if not min_fuel_2 or min_fuel_2 > fuel_2:
        min_fuel_2 = fuel_2

output.solution(min_fuel_1, min_fuel_2)
