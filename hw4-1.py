# Напишите функцию для транспонирования матрицы

def trans_matrix(matrix):
    t_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return t_matrix


m = [[1, 2, 3], [4, 5, 6]]
print(trans_matrix(m))
