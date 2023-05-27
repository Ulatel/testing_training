import sys
print(sys.path)
import api.app as app

app.app.run(debug=True)


