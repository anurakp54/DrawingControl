from class_drawing import drawing
from base import Session, engine, Base

Base.metadata.create_all(engine)

session = Session()

dwg1 = drawing("C2010001", "A")
#session.add(dwg1)
#session.commit()

content = session.query(drawing).all()
print(content)
session.close()
