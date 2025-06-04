import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Segment Tree Visualizer")
font = pygame.font.SysFont("Arial", 16)
clock = pygame.time.Clock()

arr = list(range(1, 17))
n = len(arr)
tree = [0] * (4 * n)


def build(v, tl, tr):
    if tl == tr:
        tree[v] = arr[tl]
    else:
        tm = (tl + tr) // 2
        build(v * 2, tl, tm)
        build(v * 2 + 1, tm + 1, tr)
        tree[v] = tree[v * 2] + tree[v * 2 + 1]


def query(v, tl, tr, l, r, path):
    if l > r:
        return 0
    path.append((v, tl, tr))
    if l == tl and r == tr:
        return tree[v]
    tm = (tl + tr) // 2
    left = query(v * 2, tl, tm, l, min(r, tm), path)
    right = query(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, path)
    return left + right


def update(v, tl, tr, pos, new_val, path):
    path.append((v, tl, tr))
    if tl == tr:
        tree[v] = new_val
    else:
        tm = (tl + tr) // 2
        if pos <= tm:
            update(v * 2, tl, tm, pos, new_val, path)
        else:
            update(v * 2 + 1, tm + 1, tr, pos, new_val, path)
        tree[v] = tree[v * 2] + tree[v * 2 + 1]


def draw_tree(v, tl, tr, x, y, dx, visited, lines, circles):
    circles.append((v, tl, tr, x, y))
    if tl != tr:
        tm = (tl + tr) // 2
        left_x, right_x = x - dx, x + dx
        lines.append(((x, y), (left_x, y + 80)))
        lines.append(((x, y), (right_x, y + 80)))
        draw_tree(v * 2, tl, tm, left_x, y + 80, dx // 2, visited, lines, circles)
        draw_tree(v * 2 + 1, tm + 1, tr, right_x, y + 80, dx // 2, visited, lines, circles)



def main():
    build(1, 0, n - 1)
    input_text = ""
    result = ""
    visited = []

    while True:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        if input_text.startswith("set"):
                            _, pos, val = input_text.strip().split()
                            pos, val = int(pos), int(val)
                            arr[pos] = val
                            visited = []
                            update(1, 0, n - 1, pos, val, visited)
                            result = f"Updated arr[{pos}] = {val}"
                        else:
                            l, r = map(int, input_text.strip().split())
                            visited = []
                            res = query(1, 0, n - 1, l, r, visited)
                            result = f"Sum[{l}, {r}] = {res}"
                    except Exception as e:
                        result = "Invalid input. Use 'l r' or 'set pos val'"
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        lines = []
        circles = []
        draw_tree(1, 0, n - 1, WIDTH // 2, 50, 200, visited, lines, circles)

        for (start, end) in lines:
            pygame.draw.line(screen, (0, 0, 0), start, end, 2)

        for (v, tl, tr, x, y) in circles:
            node_color = (0, 255, 0) if (v, tl, tr) in visited else (100, 200, 255)
            pygame.draw.circle(screen, node_color, (x, y), 20)
            label = font.render(str(tree[v]), True, (0, 0, 0))
            screen.blit(label, (x - label.get_width() // 2, y - label.get_height() // 2))

        input_surface = font.render(f"Enter [l r] or set pos val: {input_text}", True, (0, 0, 0))
        screen.blit(input_surface, (50, HEIGHT - 60))
        result_surface = font.render(result, True, (0, 128, 0))
        screen.blit(result_surface, (50, HEIGHT - 30))

        pygame.display.flip()
        clock.tick(30)


main()
