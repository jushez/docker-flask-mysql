from app import app, db
from counter.models import *

@app.route('/')
def init():
	counter = Counter.query.first()
	if not counter:
		counter = Counter(1)
		db.session.add(counter)
		db.session.commit()
	else:
		counter.counter += 1
		db.session.commit()
	return "<h1>Coutner: " + str(counter.count) + "</h1>"
