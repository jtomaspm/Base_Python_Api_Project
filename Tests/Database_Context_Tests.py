from src.DAL.DataContext.Database_Context import Database_Context


class Database_Context_Tests:
    def __init__(self):
        self.demo_config = {
            "host" : "localhost",
            "user" : "root",
            "passwd" : "Cr0ssr0ads1!",
            "database" : "demo"
        }
    

    def Test_Database_Config_Gets_Loaded(self):
        #ARRANGE
        config = self.demo_config
        #ACT
        db_ctx = Database_Context(config)
        #ASSERT
        assert db_ctx.config == config


    def Test_Select_Person_Query(self):
        #ARRANGE
        config = self.demo_config
        #ACT
        db_ctx = Database_Context(config)
        i = 0
        with db_ctx.cursor() as (_, cursor):
            cursor.execute("SELECT * FROM Person")
            for p in cursor:
                i += 1
                print(p)
        #ASSERT
        assert i != 0

    def test_create_db(self):
        ctx = Database_Context(self.demo_config)
        with ctx.cursor() as (cnx, cursor):
            table_name = "Person"
            table_description = (
                "  `id` int(11) NOT NULL AUTO_INCREMENT,"
                "  `name` varchar(14) NOT NULL,"
                "  `age` int(3) NOT NULL,"
                "  PRIMARY KEY (`id`)"
            )
            query = (
                "CREATE TABLE `{}` ("
                "{}"
                ") ENGINE=InnoDB"
            ).format(table_name, table_description)
            #query = (
                #"CREATE TABLE `Person` ("
                #"  `id` int(11) NOT NULL AUTO_INCREMENT,"
                #"  `name` varchar(14) NOT NULL,"
                #"  `age` int(3) NOT NULL,"
                #"  PRIMARY KEY (`id`)"
                #") ENGINE=InnoDB"
                #)
            print(query)

            cursor.execute(query)

    def run(self):
        self.Test_Database_Config_Gets_Loaded()
        self.Test_Select_Person_Query()

