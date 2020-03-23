import base64
import json

i="makan"
# some JSON:
x = { "name":"John", "age":i, "city":"New York"}

# parse x:
y = json.dumps(x)

# the result is a Python dictionary:
print(y)

#print(base64.encodestring(data))