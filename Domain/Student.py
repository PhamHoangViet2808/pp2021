class Student():
    def __init__(self, id, name, dob):
        self.s_id = id
        self.s_name = name
        self.dob = dob
    def print_St(self):
        print("ID student : " + self.s_id)
        print("Name student : " + self.s_name)
        print("Dob student : " + self.dob)