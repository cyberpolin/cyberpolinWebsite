 // Design Basic Game Solo Challenge

// This is a solo challenge

// Your mission description:To complete a line of the same figure, horizontal, diagonal or vertical
// Overall mission: To win all the time :)
// Goals: make a line of the same kind before computer does
// Characters:You and the computer
// Objects:tic tac toe
// Functions:clear_board, refresh_board, turn

// Pseudocode
// Make a Tictactoe class
  // Initialize the instance
  // Paint the board
  // Take a turn UNTIL someones win
    // Check if some one won
  // Clear the board

//
//
//
//

// Initial Code
turns = 0
board_state = [[" "," "," "],
               [" "," "," "],
               [" "," "," "]];
var Tictactoe = {
  take_turn : function(user){
    mark = prompt("It is your turn, where do you want to mark?");
      horizontal =  mark[1];
      vertical = mark[0].toUpperCase();
      if (vertical == "A"){
        vertical = 0
      } else if (vertical == "B"){
        vertical = 1
      } else {
        vertical = 2
      }
        board_state[horizontal-1][vertical] = user
        console.log(board_state)
  },
  print_board : function(){
     line = ""
      console.log("    A   B   C")
      for (i in board_state){
        new_line = "\n   ═══╬═══╬═══\n"
        for (x in board_state[i]){
          ln = parseInt(i);
          if (x == 0){line = (ln+1)+"  "}
          if (x == 2) {
            if (i == 2){new_line = "\n"}
            line += " "+board_state[i][x]+new_line;
          } else {
          line += " "+board_state[i][x]+" ║"
          }
        }
      console.log(line);
    }
  }
}



alert ("Welcome to @cyberpolin's Tic Tac Toe\n So it is the turn of User 1, please select where you want to mark...")
Tictactoe.print_board()

while (turns < 9){
  if (turns%2 == 0){
    Tictactoe.take_turn("o");
  } else {
    Tictactoe.take_turn("x");
  }

  Tictactoe.print_board();
  turns++;
}

// RELECTION
// What was the most difficult part of this challenge?
  // Order my toughts to make the code works as i wannted, also as javascript is not a language thinked for terminal it was difficult to figure out how it was going to work.

// What did you learn about creating objects and functions that interact with one another?
  // Is like in ruby, i think of them as just methods

// Did you learn about any new built-in methods you could use in your refactored solution? If so, what were they and how do they work?
  // The only one i used was toUpperCase, ad they are like Ruby methods even tough Javascript have a different syntax.

// How can you access and manipulate properties of objects?
  // like in Ruby object[property] = new_value, or the JS way object.property = new_value

// TODO'S

// Check if a place is marked already
// Check if you have winned
// Make it playable with computer
// MAKE IT GRAPHICAL!!!!