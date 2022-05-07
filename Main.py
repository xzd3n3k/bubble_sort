def bubble_sort(numbers):
    for i in range(len(numbers) - 1):
        for x in range(len(numbers) - 1):
            if numbers[x] > numbers[x + 1]:
                numbers[x], numbers[x + 1] = numbers[x + 1], numbers[x]

    return numbers
