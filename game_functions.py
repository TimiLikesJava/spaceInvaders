import sys

import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(settings , screen , ship , bullets):
     for event in pygame.event.get(): # event is any action occuring in the window
            if event.type == pygame.QUIT: # If the user hits the close button, the game will close
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event , settings , screen , ship , bullets)

            elif event.type == pygame.KEYUP:
                check_keyup_events(event , ship)

            

def check_keydown_events(event , settings , screen , ship , bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True # Move ship to the right
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True # Move ship to the left
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings , screen , ship , bullets)
    elif event.key == pygame.K_q:
            sys.exit()
                
def check_keyup_events(event , ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(settings , screen , ship , bullets , aliens):
    screen.fill(settings.background) # To apply background
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme() # display ship
    aliens.draw(screen) # display alien

    pygame.display.flip() # To render the game after every action

def update_bullets(settings , screen , ship , bullets , aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0: # Disappeared to the top of screen
            bullets.remove(bullet)

    check_bullet_alien_collisions(settings , screen , ship , bullets , aliens)
    
    print(len(bullets))



def fire_bullet(settings , screen , ship , bullets):
    if len(bullets) < settings.bullets_allowed:
            new_bullet = Bullet(settings , screen , ship)
            bullets.add(new_bullet) # puts bullets in group

def get_number_aliens_x(settings , alien_width):
    space_x = settings.width - 2 * alien_width
    no_aliens_x = int(space_x / (2 * alien_width))
    return no_aliens_x

def create_alien(settings , screen , aliens , aliens_no , no_rows):
    alien = Alien(settings , screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * aliens_no
    alien.y = alien.rect.height + 2 * alien.rect.height * no_rows
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(settings , screen , ship , aliens):
    alien = Alien(settings , screen) 
    no_aliens_x = get_number_aliens_x(settings , alien.rect.width)
    number_rows = get_number_rows(settings , ship.rect.height , alien.rect.height)

    for row_number in range(number_rows):
        for aliens_no in range(no_aliens_x):
            create_alien(settings , screen , aliens , aliens_no , row_number)

def get_number_rows(settings , ship_height , alien_height):
    space_y = (settings.height - (3 * alien_height) - ship_height)
    no_rows = int(space_y / (2 * alien_height))
    return no_rows

def update_aliens(settings ,screen ,  ship , bullets , aliens , stats):
    check_fleet_edges(settings , aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship , aliens):
        ship_hit(settings , screen , ship , bullets , aliens , stats)

    check_aliens_bottom(settings , screen , ship , bullets , aliens , stats)

def check_fleet_edges(settings , aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings , aliens)
            break

def change_fleet_direction(settings , aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def check_bullet_alien_collisions(settings , screen , ship  , bullets , aliens):
    collisions = pygame.sprite.groupcollide(bullets , aliens , True , True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(settings , screen , ship , aliens)

def ship_hit(settings , screen , ship , bullets , aliens , stats):
    if stats.ships_left > 0:
        stats.ships_left -= 1

        aliens.empty()
        bullets.empty()
        
        create_fleet(settings , screen , ship , aliens)
        ship.center_ship()
        
        sleep(0.5)

    else:
        stats.game_active = False
        


def check_aliens_bottom(settings , screen , ship , bullets , aliens , stats):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings , screen , ship , bullets , aliens , stats)
            break




        