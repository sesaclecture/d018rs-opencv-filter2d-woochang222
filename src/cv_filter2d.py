import numpy as np

def identity_kernel() -> np.array:
    # 중심값만 1인 아이덴티티 커널
    arr = [[0, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]
    return np.array(arr, dtype=np.float32)

def ones_kernel() -> np.array:
    # 모든 값이 1인 커널 (합산 효과)
    arr = [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]]
    return np.array(arr, dtype=np.float32)

def original_kernel() -> np.array:
    # 원본을 그대로 반환하는 커널은 아이덴티티 커널과 동일
    arr = [[0, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]
    return np.array(arr, dtype=np.float32)

def doubling_kernel() -> np.array:
    # 중심값만 2인 커널 (픽셀값을 2배로)
    arr = [[0, 0, 0],
           [0, 2, 0],
           [0, 0, 0]]
    return np.array(arr, dtype=np.float32)
