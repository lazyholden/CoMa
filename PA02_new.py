def convert_to_standard(a1, a2, b1, b2):
    return min(a1, b1), min(a2, b2), max(a1, b1), max(a2, b2)

def intersects(h, a1, a2, b1, b2):
    # Construct the four-points of the Rh rectangle
    rh_bl = (0, 0)
    rh_br = (6, 0)
    rh_tr = (6, h)
    rh_tl = (0, h)
    # Check if any of these points is within the target rectangle
    for x, y in [rh_bl, rh_br, rh_tr, rh_tl]:
        if a1 <= x <= b1 and a2 <= y <= b2:
            return True 
    return False

def get_delta_x1(a1, b1):
    return min(b1, 6) - max(a1, 0) + 1
    
def get_delta_x2(h, a2, b2):
    return min(b2, h) - max(a2, 0) + 1

def get_lattice_point_number(h, a1, a2, b1, b2):
    if h < 0:
        return 'Die Eingabe ist fehlerhaft.'
    a1, a2, b1, b2 = convert_to_standard(a1, a2, b1, b2)
    if not intersects(h, a1, a2, b1, b2):
        return 'Der Schnitt der gegebenen Rechtecke ist leer.'
    else:
        delta_x1 = get_delta_x1(a1, b1)
        delta_x2 = get_delta_x2(h, a2, b2)
        count = (delta_x1) * (delta_x2)
        return f'Die Zahl der Gitterpunkte im resultierenden Rechteck betraegt {count}.'