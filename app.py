from flask import Flask, jsonify

# Create a New Flask App Instance called app;Instance is a general term in programming to refer to a singular version.
app = Flask(__name__)

# This __name__ variable denotes the name of the current function. 
# You can use the __name__ variable to determine if your code is being run from the command line or if it has been 
# imported into another piece of code. Variables with underscores before/after them are called magic methods in Python
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

# Create Flask Routes, First, we need to define the starting point, also known as the root. 
# To do this, we'll use the function @app.route('/')
@app.route('/')

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
# The forward slash inside of the app.route denotes we want to put our data at the root of our routes. 
# Commonly known as the highest level of hierarchy in any computer system.

# Precip Route 
@app.route("/api/v1.0/precipitation")

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# Stations Route 
@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Precip Tobs 
@app.route("/api/v1.0/tobs")

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Statistics Route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

# The process of running a Flask app is a bit different from how we've run Python files. First, use the command line 
# to navigate to the folder where we've saved our code.
# export FLASK_APP=app.py
# set FLASK_APP=app.py


# Then use flask run to run app, after exported
# flask run

# "Running on" followed by an address. This should be your localhost address and a port number.
#localhost:5000
