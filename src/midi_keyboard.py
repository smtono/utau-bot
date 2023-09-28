"""

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

import os
from mingus.containers import NoteContainer, Note, Track, Bar
from mingus.midi import midi_file_out
from midi2audio import FluidSynth

#from note import Note

class MidiKeyboard:
    """
    a
    """

    def __init__(self, instrument: int, notes: list) -> None:
        self.composition = Track()
        self.instrument = 0 if not instrument else instrument
        self.notes = notes

    def compose(self):
        """
        Composes a MIDI file based on user input
        """
        # Grab time signature
        time_signature = self.notes[0]
        note_type = time_signature[2]

        # Add bars to composition
        new_bar = Bar()
        for i, note in enumerate(self.notes[1:]):
            if note == "|" or (i+1) == len(self.notes[1:]): # TODO: error checking for correct number of notes in bar
                self.composition.add_bar(new_bar)
                new_bar = Bar()
                continue
            new_bar.place_notes(note, int(note_type))
        self._export()

    def _export(self):
        """
        Exports a MIDI file for output to send back to the user
        """
        output = os.path.join(os.getcwd(), "output", "output.mid")
        final = os.path.join(os.getcwd(), "output", "output.mp3")
        midi_file_out.write_Track(output, self.composition)
        FluidSynth().midi_to_audio(output, final)
        


if __name__ == "__main__":
    composition_notes = ["4/4", "C", "E", "G", "C", "|", "A", "B", "C", "D"] # chord
    composition_eee = MidiKeyboard(0, composition_notes)
    composition_eee.compose()
