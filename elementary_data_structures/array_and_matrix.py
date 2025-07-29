class Array:
    def __init__(self, capacity: int = 1):
        # underlying storage
        self._capacity = capacity
        self._count = 0
        self._data = [None] * capacity

    def __len__(self) -> int:
        return self._count

    def __getitem__(self, index: int):
        if not 0 <= index < self._count:
            raise IndexError('Index out of bounds')
        return self._data[index]

    def __setitem__(self, index: int, value):
        if not 0 <= index < self._count:
            raise IndexError('Index out of bounds')
        self._data[index] = value

    def append(self, value) -> None:
        # grow if needed
        if self._count == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._count] = value
        self._count += 1

    def insert(self, index: int, value) -> None:
        if not 0 <= index <= self._count:
            raise IndexError('Index out of bounds')
        if self._count == self._capacity:
            self._resize(self._capacity * 2)
        # shift elements right
        for i in range(self._count, index, -1):
            self._data[i] = self._data[i-1]
        self._data[index] = value
        self._count += 1

    def delete(self, index: int):
        if not 0 <= index < self._count:
            raise IndexError('Index out of bounds')
        # shift elements left
        for i in range(index, self._count - 1):
            self._data[i] = self._data[i+1]
        self._data[self._count - 1] = None
        self._count -= 1

        # optionally shrink storage to save space
        if 0 < self._count < self._capacity // 4:
            self._resize(self._capacity // 2)

    def _resize(self, new_capacity: int):
        new_storage = [None] * new_capacity
        for i in range(self._count):
            new_storage[i] = self._data[i]
        self._data = new_storage
        self._capacity = new_capacity

    def __repr__(self):
        return f'Array({[self._data[i] for i in range(self._count)]})'

class Matrix:
    def __init__(self, rows: int, cols: int, default=0):
        self.rows = rows
        self.cols = cols
        self._data = [[default] * cols for _ in range(rows)]

    def get(self, i: int, j: int):
        return self._data[i][j]

    def set(self, i: int, j: int, value):
        self._data[i][j] = value

    def insert_row(self, index: int, row: list = None):
        if row is None:
            row = [0] * self.cols
        if len(row) != self.cols:
            raise ValueError('Row length must be exactly number of columns')
        self._data.insert(index, row)
        self.rows += 1

    def delete_row(self, index: int):
        self._data.pop(index)
        self.rows -= 1

    def insert_col(self, index: int, col: list = None):
        if col is None:
            col = [0] * self.rows
        if len(col) != self.rows:
            raise ValueError('Column length must be exactly number of rows')
        for r in range(self.rows):
            self._data[r].insert(index, col[r])
        self.cols += 1

    def delete_col(self, index: int):
        for r in range(self.rows):
            self._data[r].pop(index)
        self.cols -= 1

    def __repr__(self):
        return '\n'.join(str(row) for row in self._data)

# Array usage
arr = Array()
arr.append(10)
arr.append(20)
arr.append(30)
print(arr)           # Array([10, 20, 30])
arr.insert(1, 99)
print(arr[1])        # 99
arr.delete(2)
print(len(arr))      # 3
print(arr)           # Array([10, 99, 30])

# Matrix usage
m = Matrix(2, 3, default=0)
# set some values
m.set(0, 1, 5)
m.set(1, 2, 9)
print(m)
# → [0, 5, 0]
#   [0, 0, 9]

# insert a new row at top
m.insert_row(0, [1,2,3])
print(m)
# → [1, 2, 3]
#   [0, 5, 0]
#   [0, 0, 9]

# delete the last column
m.delete_col(2)
print(m)
# → [1, 2]
#   [0, 5]
#   [0, 0]
