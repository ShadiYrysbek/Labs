import pygame, sys, math


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()


draw_color = (0, 0, 255)  
bg_color = (0, 0, 0)   
radius = 5           
mode = "free"
start_pos = None  
points = []       


def draw_freehand(color):
    if len(points) > 1:
        pygame.draw.lines(screen, color, False, points, radius)


while True:
    pressed = pygame.key.get_pressed()
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                

            if event.key == pygame.K_f:
                mode = "free"
                print("Режим: свободное рисование")
            elif event.key == pygame.K_t:
                mode = "rect"
                print("Режим: прямоугольник")
            elif event.key == pygame.K_c:
                mode = "circle"
                print("Режим: круг")
            elif event.key == pygame.K_e:
                mode = "eraser"
                print("Режим: ластик")
            # Новые режимы:
            elif event.key == pygame.K_1:
                mode = "square"
                print("Режим: квадрат")
            elif event.key == pygame.K_2:
                mode = "right_triangle"
                print("Режим: прямоугольный треугольник")
            elif event.key == pygame.K_3:
                mode = "equilateral_triangle"
                print("Режим: равносторонний треугольник")
            elif event.key == pygame.K_4:
                mode = "rhombus"
                print("Режим: ромб")

            # Изменение цвета рисования
            elif event.key == pygame.K_r:
                draw_color = (255, 0, 0)
                print("Цвет: красный")
            elif event.key == pygame.K_g:
                draw_color = (0, 255, 0)
                print("Цвет: зелёный")
            elif event.key == pygame.K_b:
                draw_color = (0, 0, 255)
                print("Цвет: синий")

            elif event.key == pygame.K_KP_PLUS and ctrl_held:
                radius += 5
            elif event.key == pygame.K_KP_MINUS and ctrl_held:
                if radius > 5:
                    radius -= 5

  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                start_pos = event.pos

                if mode in ["free", "eraser"]:
                    points = [event.pos]  
                    

        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                if mode in ["free", "eraser"]:
                    points.append(event.pos)
                    

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and start_pos is not None:
                end_pos = event.pos

                current_color = bg_color if mode == "eraser" else draw_color


                if mode == "rect":
                    x = min(start_pos[0], end_pos[0])
                    y = min(start_pos[1], end_pos[1])
                    w = abs(start_pos[0] - end_pos[0])
                    h = abs(start_pos[1] - end_pos[1])
                    pygame.draw.rect(screen, current_color, (x, y, w, h), radius)

                elif mode == "circle":
                    dx = end_pos[0] - start_pos[0]
                    dy = end_pos[1] - start_pos[1]
                    r = int(math.hypot(dx, dy))
                    pygame.draw.circle(screen, current_color, start_pos, r, radius)


                elif mode == "square":
                    dx = end_pos[0] - start_pos[0]
                    dy = end_pos[1] - start_pos[1]
                    side = int(max(abs(dx), abs(dy)))

                    if dx >= 0:
                        x = start_pos[0]
                    else:
                        x = start_pos[0] - side
                    if dy >= 0:
                        y = start_pos[1]
                    else:
                        y = start_pos[1] - side
                    pygame.draw.rect(screen, current_color, (x, y, side, side), radius)


 
                elif mode == "right_triangle":
                    vertex1 = start_pos
                    vertex2 = (end_pos[0], start_pos[1])
                    vertex3 = end_pos
                    pygame.draw.polygon(screen, current_color, [vertex1, vertex2, vertex3], radius)

                elif mode == "equilateral_triangle":
                    ax, ay = start_pos
                    bx, by = end_pos
                    side = math.hypot(bx - ax, by - ay)

                    mx = (ax + bx) / 2
                    my = (ay + by) / 2
                    if side == 0:
                        vertex3 = start_pos
                    else:

                        h = (math.sqrt(3) / 2) * side

                        vx = -(by - ay) / side
                        vy = (bx - ax) / side
                        vertex3 = (mx + vx * h, my + vy * h)
                    pygame.draw.polygon(screen, current_color, [start_pos, end_pos, vertex3], radius)


                elif mode == "rhombus":
                    sx, sy = start_pos
                    ex, ey = end_pos
 
                    v1 = ((sx + ex) / 2, sy)
                    v2 = (ex, (sy + ey) / 2)
                    v3 = ((sx + ex) / 2, ey)
                    v4 = (sx, (sy + ey) / 2)
                    pygame.draw.polygon(screen, current_color, [v1, v2, v3, v4], radius)


                start_pos = None
                points = []


    current_color = bg_color if mode == "eraser" else draw_color
    if mode in ["free", "eraser"] and points:
        draw_freehand(current_color)

    pygame.display.flip()
    clock.tick(60)