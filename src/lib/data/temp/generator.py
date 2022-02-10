import json
year = []
gdp = [3.42, 3.9, 4.4, 4.97, 5.54, 6.11, 6.68, 7.25, 7.81, 8.53, 9.25, 14.62,
       18.66, 23.87, 28.85, 34.73, 39.82, 47.04, 52.58, 63.1, 76.09, 91.33, 108.12]

for i in range(1900, 2015, 5):
    year.append(i)

data = []

for i in range(23):
    data.append(
        {
            "year": year[i],
            "gdp": gdp[i]
        })

json_object = json.dumps(data)

f = open("glob_data.json", "w")
f.write(json_object)
f.close()
