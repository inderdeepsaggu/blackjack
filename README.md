<h1>Blackjack Project</h1>

<p>Blackjack is a console-based application that allows players to enjoy the classic card game of Blackjack. This game is designed and implemented using <strong>Object-Oriented Programming principles</strong> for a structured and maintainable codebase. It simulates a simplified version of Blackjack, where a player can play against a computer dealer.</p>

<h2>Features: </h2>
<ol>
  <li><strong>Card and Deck Classes:</strong></li>
    -The game utilizes a Deck class to represent a standard deck of 52 cards, and a Card class to define the properties of individual cards (suit, rank, and value).
  <li><strong>Hand and Chips Classes:</strong></li>
    -The game utilizes a Hand class to represent the cards in the players possession. The Hand class also adjusts for 'Ace' values since they can be 1 or 11. The Chips class represents the virtual currency the player currently possesses. Default amount the player starts with is 100.
  <li><strong>Game Logic:</strong></li>
    -The game logic follows the standard rules of Blackjack. Players are dealt two cards, and the objective is to get a hand value as close to 21 as possible without exceeding it. Players can choose to "hit" to receive another card or "stand" to keep their current hand.
  <li><strong>Betting System:</strong></li>
    -The game can include a simple betting system, where players start with a certain amount of virtual currency and can place bets on each hand. This is controlled through the Chips Class.
  <li><strong>User Interaction:</strong></li>
    -The game provides a text-based user interface in the console, allowing players to input their decisions (e.g., "hit" or "stand") via the keyboard.
  <li><strong>Win/Loss Scenarios:</strong></li>
    -The game checks for win, loss, or draw conditions based on the hand values and decides the outcome of each round.
  <li><strong>Continuation and Replay:</strong></li>
    -After each round, players can decide whether to continue playing, place a new bet, or exit the game.
  <li><strong>Error Handling:</strong></li>
    -The code includes error handling to prevent invalid inputs and ensure a smooth gaming experience.
</ol>

<p>By implementing these features using OOP principles, the code for Blackjack is organized, modular, and easy to maintain and extend. Players can enjoy the classic card game within the console and test their luck and skill in a digital Blackjack environment.</p>
