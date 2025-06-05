from sqlmodel import SQLModel, Field

class TestTable(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

print(f"Inside test_model.py: SQLModel.metadata.tables before TestTable: {list(SQLModel.metadata.tables.keys())}")
# Definition of TestTable happens here, populating metadata
print(f"Inside test_model.py: SQLModel.metadata.tables after TestTable: {list(SQLModel.metadata.tables.keys())}")
