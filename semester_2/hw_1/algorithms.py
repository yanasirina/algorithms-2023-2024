import copy
import random


def quick_sort(unsorted):
    """ Быстрая сортировка """
    if len(unsorted) <= 1:
        return unsorted
    else:
        q = random.choice(unsorted)
    l_nums = [n for n in unsorted if n < q]

    e_nums = [q] * unsorted.count(q)
    b_nums = [n for n in unsorted if n > q]
    return quick_sort(l_nums) + e_nums + quick_sort(b_nums)


def selection_sort(unsorted):
    """ Сортировка выбором """
    nums = copy.copy(unsorted)
    for i in range(len(nums)):
        index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[index]:
                index = j
        nums[i], nums[index] = nums[index], nums[i]
    return nums


def bubble_sort(unsorted):
    """ Пузырьковая сортировка """
    swap_bool = True
    nums = copy.copy(unsorted)
    while swap_bool:
        swap_bool = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swap_bool = True
    return nums
