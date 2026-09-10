class SumTree:
    """
    Binary Sum-Tree for Prioritized Experience Replay (PER) O(log N) sampling.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.tree = [0.0] * (2 * capacity)
        self.data = [None] * capacity
        self.write_idx = 0
        self.count = 0

    def total_priority(self):
        return self.tree[1]

    def update(self, idx, priority):
        tree_idx = idx + self.capacity
        change = priority - self.tree[tree_idx]
        self.tree[tree_idx] = priority
        while tree_idx > 1:
            tree_idx //= 2
            self.tree[tree_idx] += change

    def add(self, priority, data_item):
        idx = self.write_idx
        self.data[idx] = data_item
        self.update(idx, priority)
        self.write_idx = (self.write_idx + 1) % self.capacity
        self.count = min(self.count + 1, self.capacity)

    def sample(self, value):
        idx = 1
        while idx < self.capacity:
            left = 2 * idx
            right = left + 1
            if value <= self.tree[left]:
                idx = left
            else:
                value -= self.tree[left]
                idx = right
        data_idx = idx - self.capacity
        return data_idx, self.tree[idx], self.data[data_idx]
