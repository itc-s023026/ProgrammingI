data = [["0001", "Male", "ryo", "miyazato", "Tokyo"]]
data

member_information = {}
for record in data:
    key = (record[0], record[1])
    info = record[2:]
    member_information[key] = info

print("number", "information", sep="\t")
for key, info in member_information.items():
    print(key, info)
