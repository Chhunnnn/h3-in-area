import h3


def is_h3_in_rectangle(h3_index, top_left, bottom_right):
    # Get the bounding box of the H3 hexagon
    h3_bounding_box = h3.h3_to_geo_boundary(h3_index)

    # Check if any point on the bounding box intersects with the rectangle
    for lat, lon in h3_bounding_box:
        if not (top_left[0] <= lat <= bottom_right[0] and top_left[1] <= lon <= bottom_right[1]):
            return False
    return True


if __name__ == '__main__':
    h3_index_to_check = "8a2a1072b59ffff"
    top_left_coordinate = [40.5, -75.0]
    bottom_right_coordinate = [40.7, -74.0]

    result = is_h3_in_rectangle(h3_index_to_check, top_left_coordinate, bottom_right_coordinate)
    print("Is H3 in Rectangle:", result)
