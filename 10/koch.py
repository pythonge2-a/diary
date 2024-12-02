import turtle as tu

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

def draw_snowflake(t, size, levels):
    for _ in range(3):
        koch_curve(t, size, levels)
        t.right(120)

if __name__ == "__main__":
    width = 800  # Taille de la fenêtre
    t = tu.Turtle()
    # t.screen.setup(width, width)
    # t.screen.screensize(width * 2, width * 2)  # Agrandir la zone de dessin (canvas)
    t.screen.bgcolor("black")
    t.screen.title("Flocon de Koch")
    t.speed(0)
    t.color("yellow")
    t.pensize(3)

    # Ajuster la position de départ pour centrer le flocon
    t.penup()
    t.goto(-200, 100)  # Position initiale ajustée pour centrer
    t.pendown()

    # Dessiner le flocon
    draw_snowflake(t, width / 2, 3)  # Niveau 3 pour plus de détails

    t.hideturtle()
    t.screen.mainloop()
