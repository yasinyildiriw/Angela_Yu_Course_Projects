import colorgram

colors = colorgram.extract('art.jpg',30)

rgb_colors = []
def renk_paleti():
    for color in colors :
        rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
        rgb_colors.append(rgb)
    return rgb_colors