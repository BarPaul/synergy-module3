def main() -> str:
    '''
    Возращает строку или строки, в которой/ых числа от 1 до 9
    '''
    separator = '\n'
    '''
    separator = ' '
    Для вывода двумерного массива в одну строку
    '''
    matrix= [[j + i * 3 + 1 for j in range(3)] for i in range(3)]
    printable_matrix = [' '.join(map(str, line)) for line in matrix]
    print(separator.join(printable_matrix))
    return separator.join(printable_matrix)


if __name__ == '__main__':
    main()
