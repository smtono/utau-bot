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
import midi2audio

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
        notes_in_bar = 0
        for i, note in enumerate(self.notes[1:]):
            if (note == "|" and notes_in_bar == int(time_signature[0])) or ((i+1) == len(self.notes[1:])):
                self.composition.add_bar(new_bar)
                new_bar = Bar()
                notes_in_bar = 0
                continue
            new_bar.place_notes(note, int(note_type))
            # check for num notes in bar
            notes_in_bar += 1

        # done
        self._export()

    def _export(self):
        """
        Exports a MIDI file for output to send back to the user
        """
        output = os.path.join(os.getcwd(), "output", "output.mid")
        final = os.path.join(os.getcwd(), "output", "output.mp3")
        midi_file_out.write_Track(output, self.composition)
        converter = midi2audio.FluidSynth()
        converter.midi_to_audio(output, final)

if __name__ == "__main__":
    composition_notes = ["4/4", "C", "E", "G", "C", "|", "A", "B", "C", "D"] # chord
    composition_eee = MidiKeyboard(0, composition_notes)
    composition_eee.compose()
