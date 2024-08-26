import math

def calculate_final_distance(movements):
    x, y = 0, 0
    
    for movement in movements:
        direction, steps = movement.split()
        steps = int(steps)
        
        if direction == 'UP':
            y += steps
        elif direction == 'DOWN':
            y -= steps
        elif direction == 'LEFT':
            x -= steps
        elif direction == 'RIGHT':
            x += steps
    
    distance = math.sqrt(x**2 + y**2)
    
    print(round(distance))

movements = [
    'UP 5',
    'DOWN 3',
    'LEFT 3',
    'RIGHT 8'
]

calculate_final_distance(movements)
