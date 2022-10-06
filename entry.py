from class_drawing import drawing
from base import Session, engine, Base

#Base.metadata.create_all(engine)

session = Session()

#dwg1 = drawing("C2010001", "A")
#session.add(dwg1)
#session.commit()
match_dwg = session.query(drawing).filter(drawing.dwg_num == 'C200345566').order_by(-drawing.created).first()
if 'A1' == match_dwg.revision:
    print(f'<h1>{match_dwg.dwg_num}{match_dwg.revision} is Good for Construction</h1>')
else:
    print(f'<h1>This drawing is Not Good for Construction</h1>')

#content = session.query(drawing).filter(drawing.dwg_num.like('%345%')).first()
#print(content)
print(session.query(drawing).order_by(drawing.created.desc()).all())
session.close()
