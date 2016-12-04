class BinarySearch(list):
instantiate the variables a and b and arguement
    def __init__(self, a, b, *args):

        list.__init__(self, *args)
        self.items_length = a
        self.step = b
        end = self.items_length * self.step
        for i in range(self.step, end + 1, self.step):
            self.append(i)
    def length(self):
        return len(self)

    def search(self, value, start=0, end=None, count=0):
        if not end:
            end = self.length - 1

        if value == self[start]:
            return {'index': start, 'count': count}
        elif value == self[end]:
            return {'index': end, 'count': count}

        mid = (start + end)
        if value == self[mid]:
            return {'index': mid, 'count': count}
        elif value > self[mid]:
            start = mid + 1
        elif value < self[mid]:
            end = mid - 1

        if start >= end:
            return {'index': -1, 'count': count}
        count += 1
        return self.search(value, start, end, count)
