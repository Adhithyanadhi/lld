""" 
Text Editor : LLD

1. user can create a create document
2. add new content
3. edit existing content 
4. styling the content


"""


document
    - id
    - name
    - path
    - size
    - timestamps

word
    - id
    - document_id

char
    - id
    - word_id
    - []style    


Irobot
    - type
    - power
    - path_to_image

Human implements robot
    - get or create()
    - display(x, y)
Dog implements robot
    - get or create()
    - display(x, y)

robot_factory(type)
    case type: <type>.get_or_create()



for i in range(5 lakhs):
    robots.append(robot_factory("human"))

for i in range(5 lakhs):
    robots.append(robot_factory("dog"))

for robot in robots:
    robot.display()




Appliance
    - is_on
    - toggleOnOff()

AirConditioner implements Appliance
    - tempearture

    inc_temp()
    dec_temp()
    swing()




