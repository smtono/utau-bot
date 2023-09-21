"""Suite of functions used to parse user input and format it in a way 
that can be used to form a composition using the Mingus library

I want to write a god damn music bot to help get me out of this funk (haha get it?)
of a depression that i'm in. i hope that by making this bot it will be easier for
artists to share ideas quickly with users in a server their musical ideas
with this simple to use bot. 

the basic premise is to allow two modes of input,
one with standard text input, and another that utilizes discord embeds and reactions
both those inputs will be passed through this keyboard parser, where input is analyzed
and passed to a mingus container where a composition can then be created, midi output
can then be ascertained from this composition class.

Example Usage:

"""

from midi_keyboard import MidiKeyboard


def parse(user_input: str) -> list[str]:
    """Convert user input into usable tokens by the program 
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
    # TODO: specify composition name
    # add more capabilities with kinds of notes, accidentals, etc
    notes = user_input.split()
    if not _is_valid(notes):
        return # error
    midi = MidiKeyboard(0, notes)
    midi.compose()
    
    # Check for midi file
    

def _is_valid(notes) -> bool:
    """Checks if notes are valid, returns error if not

    Valid means that the note exists on the musical scale (ABCDEFG)
    if outside of this scope it is not a valid note in the classical sense
    Accidentals are parsed separately
    
    Args:
        notes
    Returns:
    Raises:
    """
    valid_notes = list(map(chr, range(ord('a'), ord('g')+1)))

    for note in notes:
        if note.lower() not in valid_notes:
            return False
    return True

if __name__ == "__main__":
    pass
