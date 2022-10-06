from class_drawing import drawing
from base import Session, engine, Base

#Base.metadata.create_all(engine)

session = Session()

#dwg1 = drawing("C2010001", "A")
#session.add(dwg1)
#session.commit()
if session.query(drawing).filter(drawing.dwg_num == 'C200345566A1').first():
    print(f'<h1>Drawing Number is Good for Construction</h1>')
else:
    print(f'<h1>This drawing is Not Good for Construction</h1>')

content = session.query(drawing).filter(drawing.dwg_num.like('%345%')).all()
print(content)
session.close()
