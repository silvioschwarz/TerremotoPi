import sqlite3
import numpy as np
from datetime import *

now = datetime.now()
sec = now.second
minute = now.minute
hour = now.hour
microsec = now.microsecond
totalTime = ((hour * 3600) + (minute * 60) + (sec)) *1000 + (microsec)
con = sqlite3.connect("./data/accelerationDB.db")
print("{}".format(totalTime))
#df = pd.read_sql_query('SELECT Time, X, Y, Z from acceleration where rowid > "{}" AND rowid <= "{}";'.format(totalTime-200000, totalTime), con)

#print(np.min(df["X"])
