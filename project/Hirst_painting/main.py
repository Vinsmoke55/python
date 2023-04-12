import colorgram

colors=colorgram.extract('hirst.jpg',25)

rgb_colors=[]
for color in colors:
	r=color.rgb.r
	g=color.rgb.g
	b=color.rgb.b
	color_tuple=(r,g,b)
	rgb_colors.append(color_tuple)

print(rgb_colors)


