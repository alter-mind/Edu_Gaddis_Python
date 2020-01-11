# Эта программа наносит звезды созвездия Ориона,
# названия звёзд и линии созвездия.
import turtle

# Задать размер окна
turtle.setup(500, 600)

# Установить черепаху
turtle.penup()
turtle.speed(1)
turtle.left(120)
turtle.bgcolor('black')
turtle.pencolor('white')
# turtle.hideturtle()

# Создать именованные константы для звёздных координат
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# Нанести звёзды и названия
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) # Левое плечо
turtle.dot()
turtle.write('Бетельгейзе')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) # Правое плечо
turtle.dot()
turtle.write('Хатиса')
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y) # Левая звезда в поясе
turtle.dot()
turtle.write('Альнитак')
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y) # Средняя звезда в поясе
turtle.dot()
turtle.write('Альнилам')
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y) # Правая звезда в поясе
turtle.dot()
turtle.write('Минтака')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) # Левое колено
turtle.dot()
turtle.write('Саиф')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y) # Парвое колено
turtle.dot()
turtle.write('Саиф')

# Нанести линии созвездия
turtle.pencolor('gray')
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.penup()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)

turtle.hideturtle()
turtle.done()