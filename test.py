top_left_corner=(250, 250)
bottom_right_corner=(500, 500)
top_right_corner = (top_left_corner[0] + 250, top_left_corner[1])
bottom_left_corner = (top_left_corner[0], top_left_corner[1] + 250 )

print("TL, BR:")
print(top_left_corner, bottom_right_corner)
print("TR, BL:")
print(top_right_corner, bottom_left_corner)