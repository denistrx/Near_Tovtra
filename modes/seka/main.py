import pygame
from random import randrange

pygame.init()

EXISTS = False


class Game(pygame.sprite.Sprite):
    bg = pygame.image.load('modes//seka//images//bg_seka.png')
    cards_images = {}
    players = []
    deck_of_cards = [
        'H_10',
        'H_J',
        'H_Q',
        'H_K',
        'H_A',
        'D_10',
        'D_J',
        'D_Q',
        'D_K',
        'D_A',
        'C_10',
        'C_J',
        'C_Q',
        'C_K',
        'C_A',
        'S_10',
        'S_J',
        'S_Q',
        'S_K',
        'S_A',
        'J_7',
    ]

    def __init__(self):
        for card in self.deck_of_cards:
            self.cards_images[card] = pygame.image.load(
                'modes//seka//images//' + card + '.png')

    def create_player(self, num):
        for i in range(num):
            number = len(self.players) + 1
            self.players.append({
                'player': number,
                'money': None,
                'cards': [],
                'point': 10
            })

    def distribution(self):
        for cards in range(3):
            number = 0
            for players in range(len(self.players)):
                car_number = randrange(0, len(self.deck_of_cards))
                self.players[number]['cards'].append(
                    self.deck_of_cards[car_number]
                )
                self.deck_of_cards.pop(car_number)
                number += 1

    def checks(self):
        number = 0
        for cards in range(len(self.players)):
            card1 = {
                'suit': self.players[number]['cards'][0][0],
                'name': self.players[number]['cards'][0][2]
            }
            card2 = {
                'suit': self.players[number]['cards'][1][0],
                'name': self.players[number]['cards'][1][2]
            }
            card3 = {
                'suit': self.players[number]['cards'][2][0],
                'name': self.players[number]['cards'][2][2]
            }
            if card1['name'] in card2['name'] in card3['name'] or (
                card1['name'] in card2['name'] and card3['name'] in '7') or (
                card1['name'] in card3['name'] and card2['name'] in '7') or (
                card2['name'] in card3['name'] and card1['name'] in '7'
            ):
                if card1['name'] in 'A':
                    point = 37
                elif card1['name'] in 'K':
                    point = 36
                elif card1['name'] in 'Q':
                    point = 35
                elif card1['name'] in 'J':
                    point = 34
                elif card1['name'] in '1':
                    point = 33
            elif card1['suit'] in card2['suit'] in card3['suit']:
                if (
                    card1['name'] in 'A') or (
                    card2['name'] in 'A') or (
                    card3['name'] in 'A'
                ):
                    point = 31
                else:
                    point = 30
            elif (
                card1['suit'] in card2['suit']) or (
                card1['suit'] in card3['suit']) or (
                card2['suit'] in card3['suit']
            ):
                if card1['suit'] in card2['suit']:
                    if card3['name'] in '7':
                        if card1['name'] in 'A' or card2['name'] in 'A':
                            point = 32
                        else:
                            point = 31
                    elif card1['name'] in 'A' or card2['name'] in 'A':
                        point = 21
                    else:
                        point = 20
                elif card1['suit'] in card3['suit']:
                    if card2['name'] in '7':
                        if card1['name'] in 'A' or card3['name'] in 'A':
                            point = 32
                        else:
                            point = 31
                    elif card1['name'] in 'A' or card3['name'] in 'A':
                        point = 21
                    else:
                        point = 20
                elif card2['suit'] in card3['suit']:
                    if card1['name'] in '7':
                        if card2['name'] in 'A' or card3['name'] in 'A':
                            point = 32
                        else:
                            point = 31
                    elif card2['name'] in 'A' or card3['name'] in 'A':
                        point = 21
                    else:
                        point = 20
            elif (
                card1['name'] in card2['name'] and card1['name'] in 'A') or (
                card1['name'] in card3['name'] and card1['name'] in 'A') or (
                card2['name'] in card3['name'] and card2['name'] in 'A') or (
                card1['name'] in 'A' and card2['name'] in '7') or (
                card1['name'] in 'A' and card3['name'] in '7') or (
                card2['name'] in 'A' and card1['name'] in '7') or (
                card2['name'] in 'A' and card3['name'] in '7') or (
                card3['name'] in 'A' and card1['name'] in '7') or (
                card3['name'] in 'A' and card2['name'] in '7'
            ):
                point = 22
            else:
                if (
                    card1['name'] in '7') or (
                    card2['name'] in '7') or (
                    card3['name'] in '7'
                ):
                    point = 21
                elif (
                    card1['name'] in 'A') or (
                    card2['name'] in 'A') or (
                    card3['name'] in 'A'
                ):
                    point = 11
            self.players[number]['point'] = point
            number += 1
