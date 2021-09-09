class MagicList:
    def __init__(self, cls_type = None):
        self._cls_type = cls_type
        self._list = list()

    def _append_magic_item(self):
        append_val = self._cls_type() if self._cls_type else 0
        self._list.append(append_val)

    def __getitem__(self, index):
        if index == len(self._list):
            self._append_magic_item()
        return self._list[index]

    def __setitem__(self, index, value):
        if index == len(self._list):
            self._append_magic_item()
            self._list[index] = value
        else:
            self._list[index] = value
    
    def insert(self, index, value):
        self._list.insert(index, value)

    def append(self, value):
        self.insert(len(self._list), value)

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self._list)
