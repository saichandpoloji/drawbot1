import tkinter as tk
import math
import time

root = tk.Tk()
root.title("Shape Drawer with Hand")
root.geometry("900x500")

canvas = tk.Canvas(root, bg="lightgray", width=600, height=500)
canvas.pack(side="left")

right_panel = tk.Frame(root, bg="white", width=300)
right_panel.pack(side="right", fill="y", padx=20, pady=20)

label = tk.Label(right_panel, text="Type a shape (circle, square, etc.):", bg="white")
label.pack(pady=10)

entry = tk.Entry(right_panel, font=("Arial", 16))
entry.pack(pady=10)

hand = None  

def move_hand(x, y):
    global hand
    if hand is None:
        hand = canvas.create_oval(x-5, y-5, x+5, y+5, fill="black")
    else:
        canvas.coords(hand, x-5, y-5, x+5, y+5)
    canvas.update()
    time.sleep(0.01)  

def draw_line(x1, y1, x2, y2, steps=50):
    for i in range(steps + 1):
        x = x1 + (x2 - x1) * i / steps
        y = y1 + (y2 - y1) * i / steps
        move_hand(x, y)
    canvas.create_line(x1, y1, x2, y2, fill="black", width=3)

def draw_polygon(cx, cy, sides, radius):
    points = []
    for i in range(sides + 1):
        angle = (2 * math.pi * i / sides) - math.pi / 2
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        points.append((x, y))
    for i in range(len(points) - 1):
        draw_line(*points[i], *points[i + 1])

def draw_shape():
    global hand
    canvas.delete("all")
    hand = None

    shape = entry.get().strip().lower()
    cx, cy = 300, 250

    if shape == "circle":
        steps = 100
        r = 60
        for i in range(steps + 1):
            angle = 2 * math.pi * i / steps
            x = cx + r * math.cos(angle)
            y = cy + r * math.sin(angle)
            move_hand(x, y)
        canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline="black", width=3)

    elif shape == "square":
        draw_line(cx - 60, cy - 60, cx + 60, cy - 60)
        draw_line(cx + 60, cy - 60, cx + 60, cy + 60)
        draw_line(cx + 60, cy + 60, cx - 60, cy + 60)
        draw_line(cx - 60, cy + 60, cx - 60, cy - 60)

    elif shape == "rectangle":
        draw_line(cx - 80, cy - 40, cx + 80, cy - 40)
        draw_line(cx + 80, cy - 40, cx + 80, cy + 40)
        draw_line(cx + 80, cy + 40, cx - 80, cy + 40)
        draw_line(cx - 80, cy + 40, cx - 80, cy - 40)

    elif shape == "triangle":
        draw_line(cx, cy - 80, cx + 70, cy + 60)
        draw_line(cx + 70, cy + 60, cx - 70, cy + 60)
        draw_line(cx - 70, cy + 60, cx, cy - 80)

    elif shape == "pentagon":
        draw_polygon(cx, cy, 5, 70)

    elif shape == "hexagon":
        draw_polygon(cx, cy, 6, 70)

    elif shape == "octagon":
        draw_polygon(cx, cy, 8, 70)

    else:
        move_hand(cx, cy)
        canvas.create_text(cx, cy, text=shape, font=("Arial", 36), fill="black")

button = tk.Button(right_panel, text="Draw", font=("Arial", 14), bg="blue", fg="black", command=draw_shape)
button.pack(pady=20)

root.mainloop()
