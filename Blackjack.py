from IPython.display import clear_output
import random
import time

# initializing our values for suits, ranks, values, and a playing variable that
# will be true as long as the player keeps playing

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

# defining the Card, Deck, Chips, and Hand classes

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
                
    def __str__(self):
        deck_list = ''
        for card in self.deck:
            deck_list += '\n' + card.__str__()
        return "The deck has: " + deck_list
        
    def shuffle_deck(self):
        return random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()


class Chips:
    
    def __init__(self, amount = 100):
        self.total = amount
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        self.bet = 0
    
    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0


class Hand:
    
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_cards(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
            
    def hand_value(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
        return self.value
    
    def view_hand(self):
        cards_in_hand = ''
        for card in self.cards:
            cards_in_hand += '\n' + card.__str__()
        return cards_in_hand
        
    def __str__(self):
        current_cards = ''
        for card in self.cards:
            current_cards = current_cards + card.rank + ' of ' + card.suit + '\n'
        return self.name + f' has {len(self.cards)} cards. \nCurrent cards: \n{current_cards}'


# show_some_cards will only show a portion of cards while it is the players turn
# show_all_cards is called when the player ends their turn


def show_some_cards(player, dealer):
    
    print(f"\n{player.name} has {player.hand_value()}: {player.view_hand()}")
    print(f"\nDealer has {dealer.cards[0].value}: \n{dealer.cards[0]}\nFace Down Card\n")
    
def show_all_cards(player, dealer):
    
    print(f"\n{player.name} has {player.hand_value()}: {player.view_hand()}")
    print(f"\nDealer has {dealer.hand_value()}: {dealer.view_hand()}")


# ask player for betting value


def take_bet(chips):
    
    while True:
        try:
            bet = int(input("Enter an amount to bet: "))
        except ValueError:
            print('You entered an invalid value, try again')
        else:
            if chips.total < bet:
                print(f"You don't have enough chips. Current balance: {chips.total}")
            elif bet <= 0:
                print("You can't choose a negative/zero betting value")
            else:
                chips.bet = bet
                break


def player_name():
    name = input("Please enter your name: ")
    return name


# hit function will check if its the dealer that needs cards or the player


def hit(hand, deck):
    if hand.name == 'Dealer':
        if hand.hand_value() < 17:
            while hand.hand_value() < 17:
                dealer_card = deck.deal()
                dealer.add_cards(dealer_card)
                time.sleep(1.5)
                print(f"Dealer dealt {dealer_card}, current value: {hand.hand_value()}")
                time.sleep(1.5)
    else:
        dealt_card = deck.deal()
        hand.add_cards(dealt_card)
        time.sleep(1.5)
        print(f"You were dealt {dealt_card}, current value: {hand.hand_value()}")
        time.sleep(1.5)
            

# playing variable will be changed if player chooses to stand, otherwise players turn will continue

            
def hit_or_stand(player, deck):
    global playing
    answers = ['H', 'S']
    user_input = ''
    if player.hand_value() == 21:
        playing = False
        return
    while user_input not in answers:
        user_input = input(f"{player.name}, would you like to hit or stand? (H for hit / S for stand): ").upper()
        if user_input == 'H':
            hit(player, deck)
        elif user_input == 'S':
            print('Your turn is over')
            playing = False
        else:
            print(f"{player.name} you entered an incorrect value, please enter H or S")
            


# end_game provides possibilities of who wins, player or dealer


def end_game(player, dealer, chips):
    
    if dealer.hand_value() > 21:
        dealer_busts(dealer, chips)
    elif player.hand_value() > 21:
        player_busts(player, chips)
    elif player.hand_value() > dealer.hand_value():
        player_wins(player, chips)
    elif dealer.hand_value() > player.hand_value():
        dealer_wins(dealer, chips)
    else:
        push(player, dealer, chips)

def player_busts(player, chips):
    print(f"\n{player.name} you bust!")
    chips.lose_bet()

def player_wins(player, chips):
    print(f"\n{player.name} you win!")
    chips.win_bet()

def dealer_busts(dealer, chips):
    print("\nDealer bust!")
    chips.win_bet()
    
def dealer_wins(dealer, chips):
    print("\nDealer wins!")
    chips.lose_bet()
    
def push(player, dealer, chips):
    print(f"\nDealer and {player.name} tied! Push!")
    chips.bet = 0


# play_again contains the same global variable 'playing', this will be True if player continues to play


def play_again(player, chips):
    global playing
    play_again = ''
    
    while play_again not in ['Y', 'N']:
        
        play_again = input(f"{player.name}, would you like to play again? (Y/N): ").upper()
            
        if play_again == 'Y':
            playing = True
            clear_output()
            print(f"{player.name} your current chip count is: {player_chips.total}")
            return True
        elif play_again == 'N':
            print(f"\nThank you for playing {player.name}. Final chip count: {chips.total}.\nGoodbye!")
            return False
        else:       
            print('That was an invalid entry, please enter Y or N')



if __name__ == '__main__':
    print("Welcome to Blackjack! The aim of the game is to beat the dealer but be careful, don't go over 21!\nYou are provided with 100 chips, goodluck!\n")

    player_chips = Chips()
    choose_player_name = player_name()

    while True:
        
        
        deck = Deck()
        deck.shuffle_deck()
        player = Hand(choose_player_name)
        dealer = Hand('Dealer')
        
        take_bet(player_chips)

        for i in range(2):
            player.add_cards(deck.deal())
            dealer.add_cards(deck.deal())
        
        show_some_cards(player, dealer)
        
        while playing:
            
            hit_or_stand(player, deck)
            
            if player.hand_value() > 21:
                player_busts(player, player_chips)
                break
            elif player.hand_value() == 21:
                print("\nBlackjack!\n")
                player_wins(player, player_chips)
                
        if player.hand_value() < 21:
        
            clear_output()
            
            show_all_cards(player, dealer)

            hit(dealer, deck)

            end_game(player, dealer, player_chips)

        print(f"{player.name} your current chip count is: {player_chips.total}")
        
        if player_chips.total == 0:
            print(f"{player.name} you do not have enough chips to continue. Goodbye!")
            break
        
        if play_again(player, player_chips):
            continue
        else:
            break