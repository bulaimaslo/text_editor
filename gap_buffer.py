## following instruction: https://ethz.ch/content/dam/ethz/special-interest/infk/chair-program-method/pm/documents/Verify%20This/Challenges%202018/gap-buffer.pdf

class GapBuffer:
    def __init__(self, initial_text=''):
        self.a = list(initial_text) + [''] * 10
        self.l = len(initial_text) #init gap at the end of the text
        self.r = len(self.a) - 1

    # move cursor left by one character
    # abc__def
    # ab__cdef
    def left(self):
        if self.l != 0:
            #swap l - 1 with r
            self.a[self.l-1], self.a[self.r] = self.a[self.r], self.a[self.l-1]
            self.l -= 1
            self.r -= 1
        
    def right(self):
        if self.r < len(self.a) - 1:
            #swap   
            self.a[self.l-1], self.a[self.r] = self.a[self.r], self.a[self.l-1]
            self.l += 1
            self.r += 1
            
    
    def insert(self, char):
        if self.l == self.r:
            self.grow()
        
        self.a[self.l] = char
        self.l += 1

    # Shift the pointers of the gap to include the deleted content.
    def delete(self):
        if self.l > 0:
            self.l -= 1

    def grow(self):
        b = [''] * (len(self.a) + 10)
        
        for i in range(self.l):
            b[i] = self.a[i]
        
        for i in range(self.r, len(self.a)-1):
            b[i+10] = self.a[i]
        
        self.a = b
        self.r += 10

gapBuffer = GapBuffer('hello')
print(gapBuffer.a)
gapBuffer.insert('X')
print(gapBuffer.a)
gapBuffer.left()
print(gapBuffer.a)
gapBuffer.left()
print(gapBuffer.a)
gapBuffer.insert('Y')
gapBuffer.insert('Z')
print(gapBuffer.a)
gapBuffer.delete()
print(gapBuffer.a)
gapBuffer.insert('A')
gapBuffer.insert('B')
gapBuffer.insert('C')
gapBuffer.insert('D')
gapBuffer.insert('E')
gapBuffer.insert('F')
gapBuffer.insert('G')
gapBuffer.insert('H')
gapBuffer.insert('I')
gapBuffer.insert('J')
gapBuffer.insert('K')
gapBuffer.insert('L')
print(gapBuffer.a)




