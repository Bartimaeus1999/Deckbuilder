class Card:
    def __init__(self):
        self.card_deck = None
        self.card_cost = None
        self.card_rarity = None

#meine erste Karte vom Typ Card
Attackpoints = Card()
Attackpoints.card_cost = 10
Attackpoints.card_deck = "Main-Deck"
Attackpoints.card_rarity = "legendär"
print(Attackpoints.card_cost)
print(Attackpoints.card_deck)
print(Attackpoints.card_rarity)