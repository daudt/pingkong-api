print('Executing app/models/test_model.py')
from sqlmodel import SQLModel, Field

class TestTable(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
print('Finished executing app/models/test_model.py')
