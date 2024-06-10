## [Home 1][home-1]
```
while not at_goal():
   move()
```
___

## [Home 2][home-2]
```
while not at_goal():
   move()
```
___

## [Home 3][home-3]
```
while front_is_clear():
    move()
turn_left()
move()
```
___

## [Home 4][home-4]
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    while front_is_clear():
        move()
    if right_is_clear():
        turn_right()
    else:
        turn_left()
```
___

## [Around 1][around-1]
```
put("token")
move()
while not object_here():
    while front_is_clear():
        move()
    turn_left()
```
___

## [Around 1 variable][around-1-variable]
```
put("token")
move()
while not object_here():
    if front_is_clear():
        move()
    else:
        turn_left()
```
___

## [Around 1 apple][around-1-apple]
```
def move_or_turn():
    if front_is_clear():
        move()
    else:
        turn_left()

move()
while not at_goal():
    if object_here("apple"):
        take()
    move_or_turn()
```
___

## [Around 2][around-2]
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_or_turn():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

put("token")
move()
while not object_here("token"):
    move_or_turn()
```
___

## [Around 3][around-3]
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_or_turn():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

def first_step():
    put("token")
    if front_is_clear():
        move()
    else:
        turn_left()
        move()
        
first_step()
while not object_here("token"):
    move_or_turn()
```
___


## [Around 4][around-4]
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_or_turn():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
def first_step():
    put("token")
    while not front_is_clear():
        turn_left()
    move()
        
first_step()
while not object_here("token"):
    move_or_turn()
```
___

## [Center 1][center-1]
```
def turn_around():
    turn_left()
    turn_left()

def get_length():
    length = 0
    while front_is_clear():
        move()
        length += 1
    turn_around()
    return length
    

def go_to_middle():
    middle = int(get_length()/2)
    for i in range(0, middle):
        move()
              
go_to_middle()
put("token")
```
___

## [Center 2][center-2]
```
def get_distance():
    length = 0
    while front_is_clear():
        move()
        length += 1
    return length
    
def move_distance(distance):
    for i in range(0, distance):
        move()

def go_to_middle():
    width = int(get_distance()/2)
    turn_left()
    height = int(get_distance()/2)
    turn_left()
    move_distance(width)
    turn_left()
    move_distance(height)
              
go_to_middle()
put("token")
```
___

## [Harvest 1][harvest-1]
```
def turn_right():
    turn_left()
    turn_left()    
    turn_left()

def move_distance(distance):
    for i in range(0, distance):
        move()

def align(row):
    if row % 2 == 0:
        turn_right()
    else:
        turn_left()
    
def harvest_row():
    for i in range(0,5):
        take()
        move()
        
def go_to_next_row(row):
    take()
    align(row)
    move()
    align(row)
        
move_distance(2)
turn_left()
move_distance(2)
for row in range(0,6):
    harvest_row()
    go_to_next_row(row)
```
___

## [Harvest 2][harvest-2]
```
def turn_right():
    turn_left()
    turn_left()    
    turn_left()

def move_distance(distance):
    for i in range(0, distance):
        move()

def align(row):
    if row % 2 == 0:
        turn_right()
    else:
        turn_left()

def take_all():
    while object_here():
        take()
        
def harvest_row():
    for i in range(0,5):
        take_all()
        move()
      
def go_to_next_row(row):
    take_all()
    align(row)
    move()
    align(row)
        
move_distance(2)
turn_left()
move_distance(2)
for row in range(0,6):
    harvest_row()
    go_to_next_row(row)
```
___

## [Harvest 3][harvest-3]
```
def turn_right():
    turn_left()
    turn_left()    
    turn_left()

def move_distance(distance):
    for i in range(0, distance):
        move()

def align(row):
    if row % 2 == 0:
        turn_right()
    else:
        turn_left()

def take_all_plant_one():
    while object_here():
        take()
    put("carrot")

def harvest_row():
    for i in range(0,5):
        take_all_plant_one()
        move()
      
def go_to_next_row(row):
    take_all_plant_one()
    align(row)
    move()
    align(row)
        
move_distance(2)
turn_left()
move_distance(2)
for row in range(0,6):
    harvest_row()
    go_to_next_row(row)
```
___

## [Hurdle 1][hurdle-1]
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()
```
___

## [Hurdle 2][hurdle-2]
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()
```
___

## [Hurdle 3][hurdle-3]
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()
```
___

## [Hurdle 4][hurdle-4]
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    while wall_on_right():
        move()
    
def land():
    while front_is_clear():
        move()
    
def hurdle():
    turn_left()
    jump()
    turn_right()
    move()
    turn_right()
    land()
    turn_left()

while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()
```
___

## [Maze Solution][maze]

```
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():  
    move()
turn_left()
   
        
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```
[home-1]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Home%201&url=worlds%2Ftutorial_en%2Fhome1.json
[home-2]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Home%202&url=worlds%2Ftutorial_en%2Fhome2.json
[home-3]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Home%203&url=worlds%2Ftutorial_en%2Fhome3.json
[home-4]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Home%204&url=worlds%2Ftutorial_en%2Fhome4.json
[around-1]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Around%201&url=worlds%2Ftutorial_en%2Faround1.json
[around-1-variable]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Around%201%20-%20variable&url=worlds%2Ftutorial_en%2Faround1b.json
[around-1-apple]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Around%201%20-%20apple&url=worlds%2Ftutorial_en%2Faround1c.json
[around-2]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Around%202&url=worlds%2Ftutorial_en%2Faround2.json
[around-3]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Around%203&url=worlds%2Ftutorial_en%2Faround3.json
[around-4]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Around%204&url=worlds%2Ftutorial_en%2Faround4.json
[center-1]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Center%201&url=worlds%2Ftutorial_en%2Fcenter1.json
[center-2]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Center%202&url=worlds%2Ftutorial_en%2Fcenter2.json
[harvest-1]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Harvest%201&url=worlds%2Ftutorial_en%2Fharvest1.json
[harvest-2]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Harvest%202&url=worlds%2Ftutorial_en%2Fharvest2.json
[harvest-3]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Harvest%203&url=worlds%2Ftutorial_en%2Fharvest3.json
[hurdle-1]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
[hurdle-2]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
[hurdle-3]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
[hurdle-4]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
[maze]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json