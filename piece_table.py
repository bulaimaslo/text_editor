class PieceTable:
    def __init__(self, initial_text=''):
        self.original = initial_text
        self.add = ''
        self.pieces = [(self.original, 0, len(initial_text))]
        self.undo_stack = []
        self.redo_stack = []

    def insert(self, text, pos):
        start = len(self.add)
        self.add += text
        self.pieces.append((self.add, start, len(text)))
        self._reorder_pieces(pos)
        self.undo_stack.append(('insert', pos, len(text)))
        self.redo_stack.clear()

    def delete(self, pos, length):
        deleted_pieces = self.pieces[pos:pos+length]
        del self.pieces[pos:pos+length]
        
        self.undo_stack.append(('delete', pos, deleted_pieces))
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            return
        
        operation, pos, data = self.undo_stack.pop()
        if operation == 'insert':
            self.delete(pos, data)
        elif operation == 'delete':
            for piece in reversed(data):
                self.pieces.insert(pos, piece)
        self.redo_stack.append((operation, pos, data))

    def redo(self):
        if not self.redo_stack:
            return

        operation, pos, data = self.redo_stack.pop()

        if operation == 'insert':
            self.insert(self.add[data[0]:data[0]+data[1]], pos)
        elif operation == 'delete':
            self.delete(pos, len(data))

        self.undo_stack.append((operation, pos, data))

    def _reorder_pieces(self, pos):
        self.pieces = sorted(self.pieces, key=lambda x: x[1])

    def get_text(self):
        return ''.join(buffer[start:start+length] for buffer, start, length in self.pieces)


pieceTable = PieceTable('hello')
pieceTable.insert(' world', 5)
pieceTable.delete(0, 1)
print(pieceTable.get_text())
pieceTable.undo()
print(pieceTable.get_text())
pieceTable.redo()
print(pieceTable.get_text())