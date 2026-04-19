from pyspark.sql.datasource import DataSource, DataSourceReader
from pyspark.sql.types import StructType
import faker as f
import os


     

class SimpleReader(DataSourceReader):

    def __init__(self, schema, options):
        self.schema = schema
        self.options = options

    def read(self, partition):
        new_variable = 59
        fake = f.Faker('en_IN')
        number_of_rows = int(self.options.get('number_of_rows', 100))
        for i in range(number_of_rows):
            yield(i, fake.first_name(), fake.last_name())

class SimpleSource(DataSource):
    @classmethod
    def name(cls):
        return "simple"

    def schema(self):
        return 'id int, first_name string, last_name string'
    
    def reader(self, schema: StructType):
        return SimpleReader(schema, self.options)
