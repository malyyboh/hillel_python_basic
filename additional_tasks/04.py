first_point_coordinate_input = (input("Введіть координати першої точки (x1, y1): "))

first_point_x = 0
first_point_y = 0

for item in first_point_coordinate_input:
    if item.isdigit() and item == first_point_coordinate_input[0]:
        first_point_x = float(item)
    if item.isdigit() and item == first_point_coordinate_input[-1]:
        first_point_y = float(item)

second_point_coordinate_input = (input("Введіть координати другої точки (x2, y2): "))

second_point_x = 0
second_point_y = 0

for item in second_point_coordinate_input:
    if item.isdigit() and item == second_point_coordinate_input[0]:
        second_point_x = float(item)
    if item.isdigit() and item == second_point_coordinate_input[-1]:
        second_point_y = float(item)

distance = ((second_point_x - first_point_x) ** 2 + (second_point_y - first_point_y) ** 2) ** 0.5
print("Відстань між точками:", distance)
