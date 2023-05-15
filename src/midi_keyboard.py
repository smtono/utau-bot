"""
Fucking hell!
I want to write a god damn music bot to help get me out of this funk (haha get it?)
of a depression that i'm in. i hope that by making this bot it will be easier for
artists to share ideas quickly with users in a server their musical ideas
with this simple to use bot. 

the basic premise is to allow two modes of input,
one with standard text input, and another that utilizes discord embeds and reactions
both those inputs will be passed through this keyboard parser, where input is analyzed
and passed to a mingus container where a composition can then be created, midi output
can then be ascertained from this composition class.

MIDI Keyboard:
An interactive keyboard that uses plain text input to create a MIDI output.
This is used for parsing Discord messages that use plain text, 
and does not require and special input

Notation:
For simple notes, simply put the name of the note.
A B C D E F G

Time signature is also self explanatory, input a common signature using slash notation just
as you would when typing it out.
Ex. 4/4, 3/4, 12/8 etc

End of bars are notated with a |
End of pieces are notated with ||

It may be possible in the future to also just input at random and the parser will determine everything
for the user. this will make it so there is less overhead that needs to be done by the user
overall, just a jack shit bot for a jack shit / useless application.

thank you
"""

import re

from mingus.core import meter

def tokenize(user_input: str) -> list[str]:
    """
    Convert user input into usable tokens by the program
    The following tokens can be created:
        Notes
        Accidentals
        Octave

    The user input will follow the general structure of:
        Time signature, Notes, Bar, Notes, End bar
        Ex.
        44 1B1 2C1 1B1 | 4A1 ||
    Args:
        user_input
    Returns:
        A list of tokens used to construct a Composition
    Raises:
        SyntaxError if syntax error occurs
    """
    # return_tokens = []
    tokens = user_input.split()
    time_sig_pattern = re.compile("[0-9]+/[0-9]+")

    # Time signature
    time_sig = tokens[0]
    time_sig_pattern.match(time_sig)
    # if match
    # if valid then keep, else break with error
    meter.is_valid(time_sig)

    # Find out if token is of valid type
    # Find out what type it is and attach it to token
    # add to final token list
    return tokens

def parse():
    """
    Creates a parse tree based on tokenized values
    """

def interpret():
    """
    Convert tokens to actual MIDI output
    Each token is assigned meaning, and then passed to the mingus library
    """

if __name__ == "__main__":
    fuck = input("input shit:\n")
    TOKENS = tokenize(fuck)
    print(TOKENS)
