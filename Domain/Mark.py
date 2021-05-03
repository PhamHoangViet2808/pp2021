class Mark():
    def __init__(self, id_s, id_c, mark):
        self.id_s = id_s
        self.id_c = id_c
        self.mark = mark
    def print_mark(self):
        print("ID student: " +self.id_s)
        print("ID course: " +self.id_c)
        print("mark: " +self.mark)