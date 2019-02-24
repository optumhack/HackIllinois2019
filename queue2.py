class queue:
    def __init__(self, first_value):
        self.first = item(first_value, None, None)
        self.last = self.first
        self.current = None
        self.length = 1
    def push(self, set_value):
        if self.last is None:
            self.first = item(set_value, None, None)
            self.last = self.first
            return
        self.first = item(set_value, self.first, None)
        if self.last.previous is None:
            self.last.previous = self.first
        self.first.next.previous = self.first
        self.length += 1
    def pop(self):
        to_return = self.last.value
        self.last = self.last.previous
        if self.last is None:
            self.length -= 1
            return to_return
        self.last.next = None
        self.length -= 1
        return to_return
    def get_length(self):
        return self.length

class item:
    def __init__(self, set_value, set_next, set_previous):
        self.value = set_value
        self.next = set_next
        self.previous = set_previous
