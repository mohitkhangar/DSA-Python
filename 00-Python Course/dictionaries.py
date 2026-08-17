marks = {"harry": 34, "jack": 45, "lily":94}
#print(marks, type(marks))
print(marks["harry"])
marks["harry"]=36
print(marks)
print(marks.keys())
print(marks.values())
marks.pop("lily")
print(marks)
marks.clear()
print(marks)