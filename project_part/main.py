import random


def transport_matrix(seq: list[int]) -> list[int]:
    return [[seq[j][i] for j in range(len(seq[0]))] for i in range(len(seq))]


def mult_matrix_elems(seq: list[int]) -> list[int]:
    num = int(input('Введите число на которое надо умножить: '))
    return [[seq[i][j] * num for j in range(len(seq[0]))] for i in range(len(seq))]


def matrix_rang(seq: list[int]) -> list[int]:
    cnt = 0
    for row in seq:
        cnt += sum(row) > 0
    return cnt


def matrix_determinant(seq: list[int]) -> int:
    main, second = 1, 1
    for i in range(len(seq)):
        main *= seq[i][i]
        second *= seq[i][~i]
    return main - second


def mult_matrix_self(seq: list[int]):
    sub_matrix = [r.copy() for r in seq]
    mult_matrix = [[0] * len(seq) for _ in range(len(sub_matrix[0]))]
    for i in range(len(seq)):
        for j in range(len(sub_matrix[0])):
            _sum = 0
            for q in range(len(sub_matrix)):
                _sum += seq[i][q] * sub_matrix[q][j]
            mult_matrix[i][j] = _sum
    return mult_matrix


if __name__ == '__main__':
    n, m = int(input('Введите количество строк: ')), int(input('Введите количество столбцов: '))
    matrix = [[random.randrange(10) for _ in range(m)] for _ in range(n)]
    operation = input('Введите операцию: ')
    for r in matrix:
        print(*r)

    funcs = {'транспортирование': transport_matrix, 'умножение': mult_matrix_elems, 'ранг': matrix_rang, 'определитель': matrix_determinant, 'умножение матриц': mult_matrix_self}
    mat = funcs[operation](matrix)
    print()
    if operation in ('ранг', 'определитель'):
        print(mat)
    else:
        for row in mat:
            print(*row)