def add(*args):
    matrix_shapes = {
        tuple(len(i) for i in matrix)
        for matrix in args
    }

    if len(matrix_shapes) > 1:
        raise ValueError("Given matrices are not the same size!")
    
    return [
        [sum(values) for values in zip(*m)]
        for m in zip(*args)
    ]
    