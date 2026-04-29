import pygame
import random
import math

pygame.init()
WIDTH, HEIGHT = 480, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaga Near-Arcade Clone")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

# Load YOUR provided images
player_img = pygame.transform.scale(pygame.image.load("Capture.PNG"), (50, 50))
enemy_img = pygame.transform.scale(pygame.image.load("Capture.PNG2.PNG"), (50, 50))
boss_img = pygame.transform.scale(pygame.image.load("enemy_custom.png"), (70, 70))
bullet_img = pygame.transform.scale(pygame.image.load("bullet.png"), (8, 16))
explosion_img = pygame.transform.scale(pygame.image.load("explosion.png"), (40, 40))

# Player
player = pygame.Rect(WIDTH//2 - 25, HEIGHT - 70, 50, 50)
player_speed = 5
lives = 3
score = 0

# Bullets
bullets = []
enemy_bullets = []

# Effects
explosions = []

# Enemies
enemies = []
level = 1
captured = False  # for future tractor beam

# Spawn formation

def spawn_wave():
    enemies.clear()
    for i in range(8):
        enemies.append({
            "rect": pygame.Rect(random.randint(0, WIDTH), -50, 50, 50),
            "target_x": 30 + i * 50,
            "target_y": 80,
            "type": "enemy",
            "state": "enter",
            "t": 0
        })

    enemies.append({
        "rect": pygame.Rect(WIDTH//2, -80, 70, 70),
        "target_x": WIDTH//2,
        "target_y": 40,
        "type": "boss",
        "state": "enter",
        "t": 0,
        "hp": 3
    })

spawn_wave()

state = "menu"

# Bezier function

def bezier(p0, p1, p2, t):
    return (1 - t)**2 * p0 + 2 * (1 - t) * t * p1 + t**2 * p2

running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if state == "menu":
                state = "game"
            elif state == "gameover":
                pygame.quit()

    if state == "menu":
        screen.blit(font.render("PRESS ANY KEY", True, (255,255,255)), (150,300))
        pygame.display.flip()
        continue

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:
            bullets.append(pygame.Rect(player.x + 20, player.y, 8, 16))

    for b in bullets[:]:
        b.y -= 8
        if b.y < 0:
            bullets.remove(b)

    # Enemy logic
    for enemy in enemies:
        if enemy["state"] == "enter":
            enemy["t"] += 0.02
            t = enemy["t"]
            enemy["rect"].x = int(bezier(enemy["rect"].x, WIDTH//2, enemy["target_x"], t))
            enemy["rect"].y = int(bezier(-50, HEIGHT//3, enemy["target_y"], t))
            if t >= 1:
                enemy["state"] = "idle"

        elif enemy["state"] == "idle":
            if random.random() < 0.002:
                enemy["state"] = "dive"
                enemy["t"] = 0

        elif enemy["state"] == "dive":
            enemy["t"] += 0.05
            enemy["rect"].x += int(math.sin(enemy["t"] * 3) * 6)
            enemy["rect"].y += 5

            if random.random() < 0.03:
                enemy_bullets.append(pygame.Rect(enemy["rect"].x, enemy["rect"].y, 6, 12))

            if enemy["rect"].y > HEIGHT:
                enemy["state"] = "return"

        elif enemy["state"] == "return":
            enemy["rect"].y -= 4
            if enemy["rect"].y <= enemy["target_y"]:
                enemy["state"] = "idle"

    for eb in enemy_bullets[:]:
        eb.y += 6
        if eb.y > HEIGHT:
            enemy_bullets.remove(eb)

    # Collisions
    for b in bullets[:]:
        for enemy in enemies[:]:
            if b.colliderect(enemy["rect"]):
                bullets.remove(b)
                if enemy["type"] == "boss":
                    enemy["hp"] -= 1
                    if enemy["hp"] <= 0:
                        enemies.remove(enemy)
                        score += 500
                else:
                    enemies.remove(enemy)
                    score += 100
                explosions.append({"x": enemy["rect"].x, "y": enemy["rect"].y, "t": 10})
                break

    for eb in enemy_bullets[:]:
        if player.colliderect(eb):
            enemy_bullets.remove(eb)
            lives -= 1
            if lives <= 0:
                state = "gameover"

    for ex in explosions[:]:
        ex["t"] -= 1
        if ex["t"] <= 0:
            explosions.remove(ex)

    if len(enemies) == 0:
        level += 1
        spawn_wave()

    # Draw
    screen.blit(player_img, (player.x, player.y))

    for b in bullets:
        screen.blit(bullet_img, (b.x, b.y))

    for eb in enemy_bullets:
        screen.blit(bullet_img, (eb.x, eb.y))

    for enemy in enemies:
        if enemy["type"] == "boss":
            screen.blit(boss_img, (enemy["rect"].x, enemy["rect"].y))
        else:
            screen.blit(enemy_img, (enemy["rect"].x, enemy["rect"].y))

    for ex in explosions:
        screen.blit(explosion_img, (ex["x"], ex["y"]))

    screen.blit(font.render(f"Score: {score}", True, (255,255,255)), (10,10))
    screen.blit(font.render(f"Lives: {lives}", True, (255,255,255)), (10,30))
    screen.blit(font.render(f"Level: {level}", True, (255,255,255)), (10,50))

    if state == "gameover":
        screen.blit(font.render("GAME OVER", True, (255,0,0)), (170,300))

    pygame.display.flip()

pygame.quit()

