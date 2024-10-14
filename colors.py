import colorgram

colors = colorgram.extract("image.jpg",40)

colors_list = []
for _ in range(len(colors)):
    colors_list.append((tuple(colors[_].rgb)))

print(colors_list)













