
#inition position
old_position = 0;

## remap the position to -180~180 deg on a circle 
def remap_circle(position):
    position %= 360
    if position > 180:
        position -= 360
    elif position <= -180:
        position += 360
    return position

## calculate the minimum path from old position to new position on a circle
def get_dir_n_path(new_position):
    global old_position
    new_position = remap_circle(new_position)
    dif = new_position - old_position
    dif = remap_circle(dif)
    old_position = new_position
    return dif

