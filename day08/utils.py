import numpy as np


def load_numpy_array(filename: str):
    return np.array(
        [
            [
                digit
                for
                digit
                in row
            ]
            for row
            in (np.loadtxt(filename, dtype=str))],
        dtype=np.int8
    )
