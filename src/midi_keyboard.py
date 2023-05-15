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
        Time signature

    Args:
        user_input
    Returns:
    Raises:
    """
    
    tokens = user_input.split()
    for token in tokens:
        

def parse():
    """
    Creates a parse tree based on tokenized values
    """

def interpret():
    """
    Convert tokens to actual MIDI output
    Each token is assigned meaning, and then passed to the mingus library
    """
