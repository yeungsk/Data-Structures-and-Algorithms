from typing import Optional

#
# 1) Insertion, deletion and random access of array
# 2) Assumes int for element type

class MyArray(object):
    """
    A simple wrapper around List.
    You cannot have -1 in the array
    """
    def __init__(self, capacity:int):
        self._data = []
        self._count = 0
        self._capacity = capacity

    def __getitem__(self, position:int) -> int:
        return self._data[position]

    def find(self, index:int) -> Optional[int]:
        if index >= self._count or index <= -self._count:
            return None
        return self._data[index]


    def delete(self, index:int) -> bool:
        if index >= self._count or index <= -self._count:
            return False

        self._data[index:-1] = self._data[index+1:]
        self._count -=1

        # 真正将数据删除并覆盖原来的数据
        self._data = self._data[0:self._count]
        print('delete function', self._data)
        return True

    def insert(self, index:int, value:int) -> bool:
        # 数组空间已满
        if self._capacity == self._count:
            return False
        # 插入位置大于当前的元素个数，可以插入最后的位置
        if index >= self._count:
            self._data.append(value)
        # 如果位置小于0，可以插入第0个位置
        elif index <0:
            print(index)
            self._data.insert(0,value)
        else:
            # 挪动 index至_count位 到 index+1至_count+1位
            # 插入第index
            self._data[index+1:self._count+1] = self._data[index:self._count]
            self._data[index] = value

        self._count += 1
        return True

    def insert_to_tail(self, value:int) -> bool:
        if self._count == self._capacity:
            return False
        if self._count == len(self._data):
            self._data.append(value)
        else:
            self._data[self._count] = value
        self._count += 1

    def __repr__(self) -> str:
        return " ".join(str(num) for num in self._data[:self._count])

    def print_all(self):
        for num in self._data[:self._count]:
            print(f"{num}", end= " ")
        print("\n", flush=True)

    def __len__(self):
        return self._count


def test_myarray():
    array_a = MyArray(6)
    for num in range(6):
        array_a.insert_to_tail(num)
    for num in range(6):
        assert array_a[num] == num
    assert array_a.find(0) == 0
    array_a.delete(0)
    for num in range(1,6):
        assert array_a[num-1] == num
    array_a.insert(3,0)
    array_a.insert(-1,0)
    array_a.insert(100,10000)
    print(array_a)
    #assert array_a[3] == 0
    #assert array_a.find(3) == 0
    #assert len(array_a) == 8
    #array_a.print_all()



