class queue:
    def __init__(self, first_value):
        self.first = item(first_value, None, None)
        self.last = self.first
        self.current = None
    def push(self, set_value):
        if self.last is None:
            self.first = item(set_value, None, None)
            self.last = self.first
            return
        self.first = item(set_value, self.first, None)
        if self.last.previous is None:
            self.last.previous = self.first
        self.first.next.previous = self.first
    def pop(self):
        to_return = self.last.value
        self.last = self.last.previous
        if self.last is None:
            return to_return
        self.last.next = None
        return to_return



class item:
    def __init__(self, set_value, set_next, set_previous):
        self.value = set_value
        self.next = set_next
        self.previous = set_previous
