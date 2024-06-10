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
[maze]: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json