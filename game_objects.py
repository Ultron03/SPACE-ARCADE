import pygame
from constants import WIDTH, HEIGHT, ENEMY_FORCE
import random
import math


class Explosion(pygame.sprite.Sprite):

    def __init__(self, center, explosion_images):
        super().__init__()
        self.explosion_images = explosion_images
        self.image = self.explosion_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 60
        self.explosion_sounds = [
            pygame.mixer.Sound('game_sounds/explosions/explosion1.wav'),
            pygame.mixer.Sound('game_sounds/explosions/explosion2.wav'),
            pygame.mixer.Sound('game_sounds/explosions/explosion3.wav')
        ]
        self.explosion_sound = random.choice(self.explosion_sounds)
        self.sound_played = False

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_images):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion_images[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
                if not self.sound_played:
                    self.explosion_sound.play()
                    self.sound_played = True

class Explosion2(pygame.sprite.Sprite):

    def __init__(self, center, explosion2_images):
        super().__init__()
        self.explosion2_images = explosion2_images
        self.image = self.explosion2_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 60
        self.explosion2_sounds = [
            pygame.mixer.Sound('game_sounds/explosions/explosion3.wav')
        ]
        self.explosion2_sound = random.choice(self.explosion2_sounds)
        self.sound_played = False

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion2_images):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion2_images[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
                if not self.sound_played:
                    self.explosion2_sound.play()
                    self.sound_played = True

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/bullets/bullet1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y - 10
        self.speed = 10
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/shoot.mp3')
        self.shoot_sound.play()

    def update(self):
        self.rect.move_ip(0, -self.speed)

        if self.rect.top <= 1:
            self.kill()


class BulletRefill(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        self.direction_x = random.choice([-2, 2])
        self.direction_y = random.choice([-2, 2])
        self.sound_effect = pygame.mixer.Sound("game_sounds/refill/bullet_refill.wav")

    def update(self):
        self.rect.y += self.speed * self.direction_y
        self.rect.x += self.speed * self.direction_x
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIDTH)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, HEIGHT)
        if random.randint(0, 50) == 0:
            self.direction_x *= - 1
            self.direction_y *= - 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class HealthRefill(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        self.direction_x = random.choice([-2, 2])
        self.direction_y = random.choice([-2, 2])
        self.sound_effect = pygame.mixer.Sound("game_sounds/refill/health_refill.wav")

    def update(self):
        self.rect.y += self.speed * self.direction_y
        self.rect.x += self.speed * self.direction_x
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIDTH)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, HEIGHT)
        if random.randint(0, 50) == 0:
            self.direction_x *= - 1
            self.direction_y *= - 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class DoubleRefill(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.direction_x = random.choice([-2, 2])
        self.direction_y = random.choice([-2, 2])
        self.sound_effect = pygame.mixer.Sound("game_sounds/refill/double_refill.mp3")

    def update(self):
        self.rect.y += self.speed * self.direction_y
        self.rect.x += self.speed * self.direction_x
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIDTH)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, HEIGHT)
        if random.randint(0, 50) == 0:
            self.direction_x *= - 1
            self.direction_y *= - 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)


WHITE = (255, 255, 255)


class ExtraScore(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.original_image = image
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.speed = 2
        self.rect.x = x
        self.rect.y = y
        self.direction_x = 0
        self.direction_y = 1
        self.sound_effect = pygame.mixer.Sound("game_sounds/refill/extra_score.mp3")

    def update(self):
        self.rect.y += self.speed * self.direction_y

        if self.rect.bottom >= HEIGHT + 100:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player:

    def __init__(self):
        self.rect = pygame.Rect(WIDTH//2 - 100, HEIGHT - 100, 100, 100)
        self.speed = 10
        self.image = pygame.image.load('images/spaceship_red.png').convert_alpha()
        self.image = pygame.transform.scale(pygame.image.load('images/spaceship_red.png').convert_alpha(),(64,64))
        self.original_image = self.image.copy()
        self.direction = 'down'

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = 'left'
            self.image = pygame.transform.flip(self.original_image, True, False)

    def move_right(self):
        if self.rect.right < WIDTH:
            self.rect.x += self.speed
            self.direction = 'right'
            self.image = self.original_image

    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.speed
            self.direction = 'up'

    def move_down(self):
        if self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
            self.direction = 'down'

    def stop(self):
        pass

    def stop_left(self):
        pass

    def stop_right(self):
        pass

    def stop_up(self):
        pass

    def stop_down(self):
        pass


class Enemy1(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 4
        self.direction = random.choice([(-1, -1), (-1, 1), (1, -1), (1, 1)])

    def update(self, enemy_group):
        dx, dy = self.direction
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

        if self.rect.left < 5:
            self.rect.left = 5
            self.direction = random.choice([(1, 0), (0, -1), (0, 1), (1, -1), (1, 1)])
        elif self.rect.right > WIDTH - 5:
            self.rect.right = WIDTH - 5
            self.direction = random.choice([(-1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1)])

        if self.rect.top < 5:
            self.rect.top = 5
            self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (1, 1), (-1, 1)])
        elif self.rect.bottom > HEIGHT - 5:
            self.rect.bottom = HEIGHT - 5
            self.direction = random.choice([(1, 0), (-1, 0), (0, -1), (1, -1), (-1, -1)])

        collided_with = pygame.sprite.spritecollide(self, enemy_group, False)
        for other_enemy in collided_with:
            if other_enemy != self:
                distance_vec = pygame.math.Vector2(other_enemy.rect.center) - pygame.math.Vector2(self.rect.center)
                distance = distance_vec.length()
                angle = distance_vec.angle_to(pygame.math.Vector2(1, 0))

                repel_vec = pygame.math.Vector2(1, 0).rotate(angle)
                repel_vec *= (1 - (distance / (self.rect.width + other_enemy.rect.width)))
                repel_vec *= ENEMY_FORCE

                self_dir = pygame.math.Vector2(self.direction)
                other_dir = pygame.math.Vector2(other_enemy.direction)

                if distance != 0:
                    new_dir = self_dir.reflect(distance_vec).normalize()
                    other_new_dir = other_dir.reflect(-distance_vec).normalize()

                    self.direction = new_dir.x, new_dir.y
                    other_enemy.direction = other_new_dir.x, other_new_dir.y

                self.rect.move_ip(-repel_vec.x, -repel_vec.y)
                other_enemy.rect.move_ip(repel_vec.x, repel_vec.y)


class Enemy2(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 4
        self.direction = random.choice([(-1, 0), (1, 0)]) 
        self.shoot_timer = 0
        self.shots_fired = 0

    def update(self, enemy_group, enemy_bullets_group, player):
        if self.shots_fired < 10:
            dx, dy = self.direction
            self.rect.x += dx * self.speed
            self.rect.y = max(self.rect.y, 5)

            if self.rect.left < 5:
                self.rect.left = 5
                self.direction = (1, 0)
            elif self.rect.right > WIDTH - 5:
                self.rect.right = WIDTH - 5
                self.direction = (-1, 0)

            collided_with = pygame.sprite.spritecollide(self, enemy_group, False)
            for other_enemy in collided_with:
                if other_enemy != self:
                    distance_vec = pygame.math.Vector2(other_enemy.rect.center) - pygame.math.Vector2(self.rect.center)
                    distance = distance_vec.length()
                    angle = distance_vec.angle_to(pygame.math.Vector2(1, 0))

                    repel_vec = pygame.math.Vector2(1, 0).rotate(angle)
                    repel_vec *= (1 - (distance / (self.rect.width + other_enemy.rect.width)))
                    repel_vec *= ENEMY_FORCE

                    self_dir = pygame.math.Vector2(self.direction)
                    other_dir = pygame.math.Vector2(other_enemy.direction)

                    if distance != 0:
                        new_dir = self_dir.reflect(distance_vec).normalize()
                        other_new_dir = other_dir.reflect(-distance_vec).normalize()

                        self.direction = new_dir.x, new_dir.y
                        other_enemy.direction = other_new_dir.x, other_new_dir.y

                    self.rect.move_ip(-repel_vec.x, -repel_vec.y)
                    other_enemy.rect.move_ip(repel_vec.x, repel_vec.y)

            self.shoot_timer += 1
            if self.shoot_timer >= 60:
                bullet = Enemy2Bullet(self.rect.centerx, self.rect.bottom)
                enemy_bullets_group.add(bullet)
                self.shoot_timer = 0
                self.shots_fired += 1
        else:
            self.speed = 10
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            direction = pygame.math.Vector2(dx, dy).normalize()

            self.rect.x += direction.x * self.speed
            self.rect.y += direction.y * self.speed

class Enemy2Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/bullets/bullet4.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y + 10
        self.speed = 8
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/shoot2.mp3')
        self.shoot_sound.play()

    def update(self):
        self.rect.move_ip(0, self.speed)

        if self.rect.top > HEIGHT:
            self.kill()


class BlackHole(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.original_image = image
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction_x = 0
        self.direction_y = 1
        self.angle = 0
        self.speed = 2
        self.sound_effect = pygame.mixer.Sound("game_sounds/damage/black_hole.mp3")

    def update(self):
        self.rect.y += self.speed * self.direction_y

        if self.rect.bottom >= HEIGHT + 300:
            self.kill()

        self.angle = (self.angle - 1) % 360
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Meteors(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.original_image = image
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction_x = 1
        self.direction_y = 1
        self.angle = 0
        self.speed = 2

    def update(self):
        self.rect.x += self.speed * self.direction_x
        self.rect.y += self.speed * self.direction_y
        if self.rect.bottom >= HEIGHT + 50 or self.rect.right >= WIDTH + 50:
            self.kill()

        self.angle = (self.angle - 1) % 360
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Meteors2(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.original_image = image
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction_x = 0
        self.direction_y = 1
        self.angle = 0
        self.speed = 2

    def update(self):
        self.rect.y += self.speed * self.direction_y

        if self.rect.bottom >= HEIGHT + 300:
            self.kill()

        self.angle = (self.angle - 1) % 360
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)



class Enemy1(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 4
        self.direction = random.choice([(-1, -1), (-1, 1), (1, -1), (1, 1)])

    def update(self, enemy_group):
        dx, dy = self.direction
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

        if self.rect.left < 5:
            self.rect.left = 5
            self.direction = random.choice([(1, 0), (0, -1), (0, 1), (1, -1), (1, 1)])
        elif self.rect.right > WIDTH - 5:
            self.rect.right = WIDTH - 5
            self.direction = random.choice([(-1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1)])

        if self.rect.top < 5:
            self.rect.top = 5
            self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (1, 1), (-1, 1)])
        elif self.rect.bottom > HEIGHT - 5:
            self.rect.bottom = HEIGHT - 5
            self.direction = random.choice([(1, 0), (-1, 0), (0, -1), (1, -1), (-1, -1)])

        collided_with = pygame.sprite.spritecollide(self, enemy_group, False)
        for other_enemy in collided_with:
            if other_enemy != self:
                distance_vec = pygame.math.Vector2(other_enemy.rect.center) - pygame.math.Vector2(self.rect.center)
                distance = distance_vec.length()
                angle = distance_vec.angle_to(pygame.math.Vector2(1, 0))

                repel_vec = pygame.math.Vector2(1, 0).rotate(angle)
                repel_vec *= (1 - (distance / (self.rect.width + other_enemy.rect.width)))
                repel_vec *= ENEMY_FORCE

                self_dir = pygame.math.Vector2(self.direction)
                other_dir = pygame.math.Vector2(other_enemy.direction)

                if distance != 0:
                    new_dir = self_dir.reflect(distance_vec).normalize()
                    other_new_dir = other_dir.reflect(-distance_vec).normalize()

                    self.direction = new_dir.x, new_dir.y
                    other_enemy.direction = other_new_dir.x, other_new_dir.y

                self.rect.move_ip(-repel_vec.x, -repel_vec.y)
                other_enemy.rect.move_ip(repel_vec.x, repel_vec.y)


class Boss1(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 6
        self.direction = random.choice([(-1, 0), (1, 0)]) 
        self.shoot_timer = 0
        self.shots_fired = 0

    def update(self, enemy_bullets_group, player):
        self.rect.x += math.sin(pygame.time.get_ticks() * 0.01) * 3
        self.rect.y += math.sin(pygame.time.get_ticks() * 0.01) * 3
        if self.shots_fired < 20:
            dx, dy = self.direction
            self.rect.x += dx * self.speed
            self.rect.y = max(self.rect.y, 50)

            if self.rect.left < 5:
                self.rect.left = 5
                self.direction = (1, 0)
            elif self.rect.right > WIDTH - 5:
                self.rect.right = WIDTH - 5
                self.direction = (-1, 0)

            self.shoot_timer += 1
            if self.shoot_timer >= 60:
                bullet1 = Boss1Bullet(self.rect.centerx - 20, self.rect.bottom)
                bullet2 = Boss1Bullet(self.rect.centerx + 20, self.rect.bottom)
                bullet3 = Boss1Bullet(self.rect.centerx, self.rect.bottom)
                enemy_bullets_group.add(bullet1, bullet2, bullet3)
                self.shoot_timer = 0
                self.shots_fired += 1
        else:
            self.speed = 10
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            direction = pygame.math.Vector2(dx, dy).normalize()

            self.rect.x += direction.x * self.speed
            self.rect.y += direction.y * self.speed


class Boss1Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/bullets/bulletboss1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y + 10
        self.speed = 10
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/boss1shoot.mp3')
        self.shoot_sound.play()

    def update(self):
        self.rect.move_ip(0, self.speed)

        if self.rect.top > HEIGHT:
            self.kill()

class Boss2(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5
        self.direction = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)])
        self.direction_x, self.direction_y = self.direction
        self.shoot_timer = 0
        self.shots_fired = 0

    def update(self, enemy_bullets_group, player):
        self.rect.x += math.sin(pygame.time.get_ticks() * 0.01) * 2
        self.rect.y += math.sin(pygame.time.get_ticks() * 0.01) * 2
        if self.shots_fired < 20:
            dx, dy = self.direction
            if self.direction in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
                self.speed = 5 / math.sqrt(2)
            else:
                self.speed = 5
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed

            if self.rect.left < 5:
                self.rect.left = 5
                self.direction_x = 1
                if self.direction_y == 0:
                    self.direction_y = 1
            elif self.rect.right > WIDTH - 5:
                self.rect.right = WIDTH - 5
                self.direction_x = -1
                if self.direction_y == 0:
                    self.direction_y = 1
            elif self.rect.top < 70:
                self.rect.top = 70
                self.direction_y = 1
                if self.direction_x == 0:
                    self.direction_x = 1
            elif self.rect.bottom > HEIGHT - 5:
                self.rect.bottom = HEIGHT - 5
                self.direction_y = -1
                if self.direction_x == 0:
                    self.direction_x = 1

            self.direction = (self.direction_x, self.direction_y)
            self.shoot_timer += 1
            if self.shoot_timer >= 100:
                dx = player.rect.centerx - self.rect.centerx
                dy = player.rect.centery - self.rect.centery
                direction = pygame.math.Vector2(dx, dy).normalize()
                bullet = Boss2Bullet(self.rect.centerx, self.rect.bottom, direction)
                enemy_bullets_group.add(bullet)
                self.shoot_timer = 0
                self.shots_fired += 1
        else:
            if self.speed != 5:
                self.speed = 5 / math.sqrt(2)
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            direction = pygame.math.Vector2(dx, dy).normalize()

            self.rect.x += direction.x * self.speed
            self.rect.y += direction.y * self.speed

            self.direction_x = direction.x / abs(direction.x) if direction.x != 0 else 0
            self.direction_y = direction.y / abs(direction.y) if direction.y != 0 else 0
            self.direction = (self.direction_x, self.direction_y)


class Boss2Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):
        super().__init__()
        self.image_orig = pygame.image.load('images/bullets/bulletboss2.png').convert_alpha()
        self.image = self.image_orig
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y + 10
        self.speed = 11
        self.direction = direction
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/boss2shoot.mp3')
        self.shoot_sound.play()

    def update(self):
        self.rect.move_ip(self.direction.x * self.speed, self.direction.y * self.speed)

        angle = math.atan2(self.direction.y, self.direction.x)
        angle = math.degrees(angle)

        self.image = pygame.transform.rotate(self.image_orig, -angle)


        self.rect = self.image.get_rect(center=self.rect.center)

        if self.rect.top > HEIGHT:
            self.kill()

class Boss3(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5
        self.direction = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)])
        self.direction_x, self.direction_y = self.direction
        self.shoot_timer = 0
        self.shots_fired = 0
        self.teleport_timer = 0
        self.teleport_interval = 160

    def update(self, enemy_bullets_group, player):
        self.rect.x += math.sin(pygame.time.get_ticks() * 0.01) * 2
        self.rect.y += math.sin(pygame.time.get_ticks() * 0.01) * 2
        if self.shots_fired < 20:
            dx, dy = self.direction
            if self.direction in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
                self.speed = 5 / math.sqrt(2)
            else:
                self.speed = 5
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed

            if self.rect.left < 5:
                self.rect.left = 5
                self.direction_x = 1
                if self.direction_y == 0:
                    self.direction_y = 1
            elif self.rect.right > WIDTH - 5:
                self.rect.right = WIDTH - 5
                self.direction_x = -1
                if self.direction_y == 0:
                    self.direction_y = 1
            elif self.rect.top < 70:
                self.rect.top = 70
                self.direction_y = 1
                if self.direction_x == 0:
                    self.direction_x = 1
            elif self.rect.bottom > HEIGHT - 5:
                self.rect.bottom = HEIGHT - 5
                self.direction_y = -1
                if self.direction_x == 0:
                    self.direction_x = 1

            self.direction = (self.direction_x, self.direction_y)
            self.shoot_timer += 1
            if self.shoot_timer >= 120:
                dx = player.rect.centerx - self.rect.centerx
                dy = player.rect.centery - self.rect.centery
                direction = pygame.math.Vector2(dx, dy).normalize()
                bullet = Boss3Bullet(self.rect.centerx, self.rect.bottom, direction)
                enemy_bullets_group.add(bullet)
                self.shoot_timer = 0
                self.shots_fired += 1
        else:
            if self.speed != 5:
                self.speed = 5 / math.sqrt(2)
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            direction = pygame.math.Vector2(dx, dy).normalize()

            self.rect.x += direction.x * self.speed
            self.rect.y += direction.y * self.speed

            self.direction_x = direction.x / abs(direction.x) if direction.x != 0 else 0
            self.direction_y = direction.y / abs(direction.y) if direction.y != 0 else 0
            self.direction = (self.direction_x, self.direction_y)

        self.teleport_timer += 1
        if self.teleport_timer >= self.teleport_interval:
            self.rect.centerx = random.randint(50, WIDTH - 50)
            self.rect.centery = random.randint(100, HEIGHT - 100)
            self.teleport_timer = 0


class Boss3Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):
        super().__init__()
        self.image_orig = pygame.image.load('images/bullets/bulletboss3.png').convert_alpha()
        self.image = self.image_orig
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y + 10
        self.speed = 15
        self.direction = direction
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/boss2shoot.mp3')
        self.shoot_sound.play()

    def update(self):
        self.rect.move_ip(self.direction.x * self.speed, self.direction.y * self.speed)

        angle = math.atan2(self.direction.y, self.direction.x)
        angle = math.degrees(angle)

        self.image = pygame.transform.rotate(self.image_orig, -angle)


        self.rect = self.image.get_rect(center=self.rect.center)

        if self.rect.top > HEIGHT:
            self.kill()