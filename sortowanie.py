import random
import time


def make_list():
    lista = []
    for i in range(100):
        lista.append(random.randrange(100))
    return lista

# lista = [1,2,3,4,5]
def bubblesort(lista):
    returned_list = lista.copy()
    for i in range(len(returned_list)):
        for j in range(len(returned_list)):
            if returned_list[i] < returned_list[j]:
                returned_list[i], returned_list[j] = returned_list[j], returned_list[i]
    return returned_list


def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        end_list = lista[-1]
        middle_list = [end_list]
        lesser_list = []
        greater_list = []
        for i in range(len(lista) - 1):
            if lista[i] <= end_list:
                lesser_list.append(lista[i])
            else:
                greater_list.append(lista[i])
        returned_list = quick_sort(lesser_list) + middle_list + quick_sort(greater_list)
        return returned_list


def insertion_sort(lista):
    returned_list = lista.copy()
    index = 0
    marker = 0
    while index < len(returned_list)-1:
        if returned_list[index] <= returned_list[index + 1]:
            index += 1
            marker = index
        else:
            while returned_list[index] > returned_list[index + 1]:
                returned_list[index + 1], returned_list[index] = returned_list[index], returned_list[index + 1]
                if index != 0:
                    index -= 1
                else:
                    pass
            index = marker
    return returned_list


def main():
    lista = make_list()
    lista_copy = lista.copy()
    lista_copy2 = lista.copy()
    print("wygenerowano listę")

    start = time.time()
    bubble_sort_sorted_list = bubblesort(lista)
    end = time.time()
    print("Czas sortowania bąbelkowego ", end - start, ' sek.')

    start = time.time()
    quick_sort_sorted_list = quick_sort(lista_copy)
    print(quick_sort_sorted_list)
    end = time.time()
    print("Czas sortowania quick-sort ", end - start, ' sek.')

    start = time.time()
    insertion_sorted_list = insertion_sort(lista_copy2)
    end = time.time()
    print("Czas sortowania przez wstawianie ", end - start, ' sek.')

    if bubble_sort_sorted_list and quick_sort_sorted_list == insertion_sorted_list:
        print('takie same')


if __name__ == '__main__':
    main()
