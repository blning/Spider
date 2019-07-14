import pygame
import sys
import random
from ball import BallClass


# 函数的定义
def main():
    pygame.init()           # 模块初始化
    screen = pygame.display.set_mode((800, 600))    # 设置屏幕的尺寸
    pygame.display.set_caption("Windows屏保")        # 设置屏幕的标题
    balls = []      # 创建一个存放小球对象的列表

    clock = pygame.time.Clock()     # 控制帧速率
    while True:
        screen.fill([255, 255, 255])    # 设置背景颜色

        for ball in balls:          # 遍历存储球列表中球对象
            ball.move()             # 调用球对象的move方法
            ball.draw_ball(screen)    # 调用球对象的绘制方法
            if ball.radius == 0:        # 判断球对象的半径是否为0
                balls.remove(ball)      # 移除半径为0的球对象

        for i in range(len(balls)):       # 遍历存储球对象列表的长度
            for x in range(len(balls)):
                balls[i].eat(balls[x])      # 调用Ball的eat方法

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # 判断是否有鼠标点下和是否点下右键
            elif event.type ==pygame.MOUSEBUTTONDOWN and event.button == 3:

                # 创建圆心点坐标
                center = (random.randint(100, 300), random.randint(100, 300))

                # 小球颜色
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                # 小球半径
                radius = random.randint(10, 50)

                # 小球偏移量
                sx, sy = random.randint(-10, 10), random.randint(-10, 10)

                # 创建小球对象
                ball = Ball(center, color, radius, sx, sy)

                # 把小球对象添加到小球列表中
                balls.append(ball)

        clock.tick(60)           # 设置帧速率
        pygame.display.flip()    # 刷新屏幕


if __name__ == '__main__':
    main()



