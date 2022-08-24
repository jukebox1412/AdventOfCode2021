# https://adventofcode.com/2021/day/17

def main():
    x_low = 287
    x_high = 309
    y_low = -76
    y_high = -48
    print(style_on_it(x_low, x_high, y_low, y_high))
    
def style_on_it(x_low, x_high, y_low, y_high):
    highest_y = 0
    init_vel = [0, 0]
    while(True):
        # for each step
        current_pos = [0, 0]
        current_vel = [init_vel[0], init_vel[1]]
        highest_y_per_current_run = 0
        hit_target = False
        overshot = False
        print(f"Trying for for [{current_vel[0]}, {current_vel[1]}]")

        while(current_pos[0] < x_high and current_pos[1] > y_low): # no point in over shooting
            current_pos[0] += current_vel[0] 
            current_pos[1] += current_vel[1]

            if highest_y_per_current_run < current_pos[1]:
                highest_y_per_current_run = current_pos[1]
            
            if current_pos[1] < highest_y_per_current_run and highest_y_per_current_run < highest_y:
                print(f"\tskipping on [{current_vel[0]}, {current_vel[1]}]")
                break # already passed the possiblity of this being the coordinates

            # check if we hit the goal
            if current_pos[0] >= x_low and current_pos[0] <= x_high and current_pos[1] >= y_low and current_pos[1] <= y_high:
                hit_target = True
                print(f"\thit on [{current_vel[0]}, {current_vel[1]}], highest is {highest_y_per_current_run}")
                break
            
            if current_pos[0] > x_high:
                overshot = True
            
            # decrease x vel by an absolute value
            if current_vel[0] > 0:
                current_vel[0] -= 1
            elif current_vel[0] < 0:
                current_vel += 1
            
            # decrease y vel by 1 because gravity
            current_vel[1] -= 1

        if hit_target and highest_y < highest_y_per_current_run:
            highest_y = highest_y_per_current_run
        
        if hit_target:
            init_vel = [init_vel[0], init_vel[1] + 1]
        else:
            if overshot:
                init_vel = [init_vel[0] + 1, init_vel[1]]

     

    

    return highest_y

main()
