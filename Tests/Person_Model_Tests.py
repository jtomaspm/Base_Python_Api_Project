from src.DAL.DataContext.Database_Context import Database_Context
from src.DAL.Models.Person import Person

class Person_Model_Tests:
    def __init__(self):
        self.demo_config = {
            "host" : "localhost",
            "user" : "root",
            "passwd" : "Cr0ssr0ads1!",
            "database" : "demo"
        }
        self.ctx = Database_Context(self.demo_config)

    def Test_Create_Table(self):
        person = Person(self.ctx)
        person.create_table()

    def Test_Insert(self):
        person_data = {
            'name' : 'test',
            'age' : 21
        }
        person = Person(self.ctx)
        res = person.new(person_data)
        res = person.new(person_data)
        res = person.new(person_data)
        res = person.new(person_data)
        res = person.delete("id <= 2")

        assert res != None

    def run(self):
        self.Test_Create_Table()
        self.Test_Insert()