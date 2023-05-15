"""
MIDI Keyboard:

An interactive keyboard that uses plain text input to create a MIDI output.
This is used for parsing Discord messages that use plain text, and does not require and special input

Notation:
For simple notes, simply put the name of the note.
A B C D E F G

"""

import mingus.core.notes as notes
import mingus.core as diatonic
from mingus.containers import Composition
from mingus.containers import NoteContainer

def tokenize(user_input: str):
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
    """
    return_tokens = []
    tokens = user_input.split()
    for token in tokens:
        # Find out if token is of valid type
        # Find out what type it is and attach it to token
        # add to final token list
        pass

def parse():
    """
    Creates a parse tree based on tokenized values
    """

def interpret():
    """
    Convert tokens to actual MIDI output
    Each token is assigned meaning, and then passed to the mingus library
    """
