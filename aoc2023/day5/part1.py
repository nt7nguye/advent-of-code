from random import seed
import typing


def to_int_tuple(input: str):
    return [int(num) for num in input.split(' ')]

def sort_by_second_items(arr_of_objs: typing.List[typing.List]):
    return arr_of_objs.sort(key=lambda x: x[1])

def parse_map(input, line_number):
    arr = []
    while line_number < len(input) and input[line_number] != '':
        arr.append(to_int_tuple(input[line_number]))
        line_number += 1
    sort_by_second_items(arr)
    line_number += 2
    return arr, line_number

def convert_num(num, sorted_map):
    for section in sorted_map:
        if num < section[1]:
            return num
        if num >= section[1] and num < section[1] + section[2]:
            return num + section[0] - section[1]
    return num

def convert_arr(arr, sorted_map): 
    return [convert_num(num, sorted_map) for num in arr]

def solve(input):
    i = 0
    seeds = [int(num) for num in input[0].split(' ')[1:]]
    i += 3

    seed_to_soil, i = parse_map(input, i)
    soil_to_fertilizer, i = parse_map(input, i)
    fertilizer_to_water, i= parse_map(input, i)
    water_to_light , i = parse_map(input, i)
    light_to_temperature, i = parse_map(input, i)
    temperature_to_humidity , i = parse_map(input, i)
    humidity_to_location, i =parse_map(input, i)
    
    for sorted_map in [seed_to_soil, soil_to_fertilizer, \
                    fertilizer_to_water, water_to_light, \
                    light_to_temperature, temperature_to_humidity, \
                    humidity_to_location]:
        seeds = convert_arr(seeds, sorted_map)
    return min(seeds)