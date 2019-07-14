import pygame
from math import sqrt

class Ball:
    # 在初始化方法中定义小球的圆心点坐标，颜色，小球半径，小球在x轴和y轴的偏移量
    def __init__(self, center, color, radius, sx, sy):
        self.center = center
        self.color = color
        self.radius = radius
        self.sx = sx
        self.sy = sy

    def draw_ball(self, screen):    # 定义画小球的方法
        pygame.draw.circle(screen, self.color, self.center, self.radius)

    def move(self):        # 定义小球移动的方法
        x, y = self.center[0], self.center[1]     # 获得小球x方向与y方向上的坐标值
        x += self.sx        # 设置小球在x方向上的偏移量
        y += self.sy        # 设置小球在y方向上的偏移量
        self.center = (x, y)    # 小球移动之后的坐标要重新赋给小球的圆心坐标

        # 如果小球到达左右边界（水平方向），就将偏移量改为相反数
        if x + self.radius >= 800 or x -self.radius <= 0:
            self.sx = -self.sx

        # 如果小球到达上下边界（垂直方向），就将偏移量改为相反数
        if y + self.radius >= 600 or y - self.radius <= 0:
            self.sy = -self.sy

    def eat(self, other):       # 定义大球吃小球的方法
        # 计算两个小球的圆心距
        a = sqrt((self.center[0] - other.center[0]) ** 2 + (self.center[1] - other.center[1]) ** 2)

        if a < self.radius + other.radius and self.radius > other.radius:   # 判断圆心距是否大于两球的半径之和、当前球的半径是否大于另一个球的半径
            self.radius += other.radius         # 当前球的半径（大球）加上另一个球的半径（小球）
            other.radius = 0                    # 将小球半径设置为0
            if self.radius > 100:               # 判断大球半径是否大于100
                self.radius = 10                # 将大球半径设置为0（’自爆‘）
        if a < self.radius + other.radius and self.radius < other.radius:
            other.radius += self.radius
            self.radius = 0
            if other.radius > 100:
                other.radius = 10