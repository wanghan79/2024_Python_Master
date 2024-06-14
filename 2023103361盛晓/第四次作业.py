class RandomStructureIterator:
    def __init__(self, data):
        self._data = data
        self._keys = list(data.keys()) if isinstance(data, dict) else range(len(data))
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._keys):
            key = self._keys[self._index]
            self._index += 1
            return key, self._data[key]
        else:
            raise StopIteration

# Example usage
example_structure = {
    'a': [1, 2.0, 'three'],
    'b': {'c': 3, 'd': [4, 5.0]}
}
generator = RandomStructureGenerator()
random_structure = generator.generate(example_structure)

iterator = RandomStructureIterator(random_structure)
for key, value in iterator:
    print(f"{key}: {value}")

