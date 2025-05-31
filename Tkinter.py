import tkinter as tk
import math
class MovingCircle:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()

        self.circle_pos = [200, 200]
        self.circle_radius = 20
        self.circle = self.canvas.create_oval(
            self.circle_pos[0] - self.circle_radius,
            self.circle_pos[1] - self.circle_radius,
            self.circle_pos[0] + self.circle_radius,
            self.circle_pos[1] + self.circle_radius,
            fill='blue'
        )

        self.target_pos = None
        self.speed = 3

        self.canvas.bind('<Button-1>', self.set_target)

        self.animate()

    def set_target(self, event):
        self.target_pos = [event.x, event.y]
        self.canvas.delete('target')
        self.canvas.create_oval(
            event.x - 5, event.y - 5,
            event.x + 5, event.y + 5,
            fill='red', tags='target'
        )
    def animate(self):
        if self.target_pos:
            dx = self.target_pos[0] - self.circle_pos[0]
            dy = self.target_pos[1] - self.circle_pos[1]
            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance < self.speed:
                self.circle_pos = self.target_pos.copy()
                self.target_pos = None
            else:
                dx = dx / distance * self.speed
                dy = dy / distance * self.speed
                self.circle_pos[0] += dx
                self.circle_pos[1] += dy

            self.canvas.coords(
                self.circle,
                self.circle_pos[0] - self.circle_radius,
                self.circle_pos[1] - self.circle_radius,
                self.circle_pos[0] + self.circle_radius,
                self.circle_pos[1] + self.circle_radius
            )
        self.root.after(20, self.animate)
root = tk.Tk()
app = MovingCircle(root)
root.mainloop()
