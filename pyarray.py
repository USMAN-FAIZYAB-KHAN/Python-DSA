import ctypes

class Array:
    def __init__(self, size):
        self._size = size
        self._elements = (ctypes.py_object * size)()
        self.clear(None)
    
    def __getitem__(self, index):
        assert index >= 0 and index < self._size, "Index out of range"
        return self._elements[index] 

    def __setitem__(self, index, value):
        assert index >= 0 and index < self._size, "Index out of range"
        self._elements[index] = value
    
    def __len__(self):
        return self._size

    def traverse(self):
        for i in range(self._size):
            print(self._elements[i], end=" ")
        print()

    def clear(self, value):
        for i in range(self._size):
            self._elements[i] = value

    
def bubbleSort(arr: list):
    end = len(arr)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(end-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = False
                print(arr)
        end -= 1
    

class Array2D:
    # the time complexity of __init__ is O(rows*cols)
    def __init__(self, rows, cols) -> None:
        self._theRows = Array(rows)
        for i in range(rows):
            self._theRows[i] = Array(cols)

    def numRows(self):
        return len(self._theRows)
    
    def numCols(self):
        return len(self._theRows[0])

    def clear(self, value):
        for i in range(self.numRows()):
            self._theRows[i].clear(value)

    def __getitem__(self, pos):
        assert len(pos) == 2, "Invalid number of array subscripts"
        row = pos[0]
        col = pos[1]
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array subscript out of range"
        return self._theRows[row][col]

    def __setitem__(self, pos, value):
        assert len(pos) == 2, "Invalid number of array subscripts"
        row = pos[0]
        col = pos[1]
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array subscript out of range"
        self._theRows[row][col] = value

    def traverse(self):
        rows = self.numRows()
        cols = self.numCols()
        for i in range(rows):
            for j in range(cols):
                print(self._theRows[i][j], end=" ")
            print()

    def addValue(self, value):
        rows = self.numRows()
        cols = self.numCols()
        for i in range(rows):
            for j in range(cols):
                self._theRows[i][j] += value

    def multiplyValue(self, value):
        rows = self.numRows()
        cols = self.numCols()
        for i in range(rows):
            for j in range(cols):
                self._theRows[i][j] *= value
        
def addMatrix(m1: Array2D, m2: Array2D):
    assert m1.numRows() == m2.numRows() and m1.numCols() == m2.numCols(), "Matrix are not compatible for addition"
    rows = m1.numRows()
    cols = m1.numCols()
    m = Array2D(rows, cols)
    for i in range(rows):
        for j in range(cols):
            m[i, j] = m1[i, j] + m2[i, j]
    return m

def matrixProduct(m1: Array2D, m2: Array2D):
    assert m1.numCols() == m2.numRows(), "Matrices cannot be multiplied"
    r1 = m1.numRows()
    c1 = m1.numCols()
    c2 = m2.numCols()
    m = Array2D(r1, c2)
    m.clear(0)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                m[i,j] += m1[i,k] * m2[k,j]
    return m


# m1 = Array2D(3, 2)
# m1.clear(2)
# m1.traverse()
# m1.multiplyValue(4)
# m1.traverse()

