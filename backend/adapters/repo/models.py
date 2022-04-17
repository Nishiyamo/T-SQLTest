from sqlalchemy import Column, String, Float, Date

class Customer:
    __tablename__ = "Customer"
    CustomerId = Column()
    CustomerName = Column()

class Item:
    __tablename__ = "Item"
    ItemId = Column()
    VersionNbr = Column() #Version of the iteam
    DeletedFlag = Column() #Status of the item active =1
    ItemDocumentNbr = Column() #Hash of a item
    CustomerId = Column() #Id of customer
    CreateDate = Column()
    UpdateDate = Column()

