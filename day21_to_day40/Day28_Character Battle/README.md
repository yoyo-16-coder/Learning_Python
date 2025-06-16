## Character Battle
- Continuation of the previous day. 
- I love this. My first proper game.
- Uses subroutines- healthstat, strength and rolldice. Color coded. Multiple while loops. Plus I have tried to clutter it less and there is less chance of recursion since I have also tried for minimum repetition. 
- Asks user their name, type of character calls out subroutine healthstat() and gives them their health. Shows the page for limited seconds then clears the screen and we see the next page that says Round (whichever round that is) and rolls random strength for both the people, whichever person has the higher strength out of the two, wins that particular round, Suppose person1 had strength 33 while person 2 had strength 27.  Person 1 wins the round 1 and the damage caused to person 2's health is strength of person 1 - strength of person 2, in this case it is 6. It shows this screen for about 7 secs before continuing loop until either person 1 or person 2 reaches 0 or some negative number. It declares the winner and how many rounds it took for the winner to win. It also asks if they want to rematch or play again.
main
