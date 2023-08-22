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

It may be possible in the future to also just input at random 
and the parser will determine everything
for the user. this will make it so there is less overhead that needs to be done by the user
overall, just a minimum viable product/prototype for a fun chat experience.

thank you
"""

from mingus.containers import NoteContainer
from mingus.midi import midi_file_out

from note import Note

class MidiKeyboard:
    """
    a
    """

    def __init__(self, instrument: int, notes: list[Note]) -> None:
        self.composition = NoteContainer()
        self.instrument = 0 if not instrument else instrument
        self.notes = notes
    
    def compose(self):
        """
        Composes a MIDI file based on user input
        """
        for note in self.notes:
            musical_note = Note(note)
            composition.add_notes(musical_note)
    
    def _export(self):
        """
        Exports a MIDI file for output to send back to the user
        """
    

if __name__ == "__main__":
    pass
