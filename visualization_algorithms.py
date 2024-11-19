import random_list as rl
import insertion_sort as isort

unsorted_list = rl.make_random_list(1000)
print(f"La lista desordenada es: {unsorted_list}")
sorted_list = isort.insertion_sort_algorithm(unsorted_list)
print(f"\n\nLa lista ordenada es: {sorted_list}")
reverse_sorted_list = isort.reverse_insertion_sort_algorithm(unsorted_list)
print(f"\n\nLa lista ordenada de forma descendente es: {reverse_sorted_list}")


def add_integers(a: list, b: list) -> list:
    if len(a) != len(b):
        raise ValueError("Las listas deben tener la misma longitud")
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result


first_list = rl.make_random_list(10)
second_list = rl.make_random_list(10)
sum_list = add_integers(first_list, second_list)
print(f"\n\nLa suma de las listas {first_list} y {second_list} es: {sum_list}")
