"""
Write a program that asks for a note, check if it is valid and output the note which is five half notes away from it.
Get the minor equivalent of a valid note and diminish it.
Generate the first thousand fibonacci numbers and use a modulo 12 operation (eg. n % 12) to convert each value to a note.
"""
import mingus.core.notes as notes
import mingus.core as diatonic
from mingus.containers import Composition
from mingus.containers import NoteContainer

note = input('Enter a note: ')
if notes.is_valid_note(note):
    new_note = notes.note_to_int(note)
    new_note = notes.int_to_note(new_note)
    print(notes.augment(new_note))

fibs = []
for i in range(1000):
    fibs.append(i + (i+1))

for num in fibs:
    note = num % 12
    print(notes.int_to_note(note))

"""
Write a program that lets the user input a key, get the notes in the key and print the half note steps between the notes. 
What do you notice when you ask for different keys?
For every note in basic_keys: Convert the numbers 0-11 using diatonic.int_to_note and notes.int_to_note. 
If the values are different, output the values, the number and the key to screen.
"""

key = input('Enter a key: ')
if notes.is_valid_note(key):
    notes_in_sig = diatonic.get_notes(key)
for note in notes_in_sig:
    half_step = notes.note_to_int(note) + 1
    print(diatonic.int_to_note(half_step, key))

"""
Take the minor and major thirds and fourths of the note C. 
Output the note and the note as integer to the screen. Do you notice something?
Create a program where a user can input a key 
and a note and gets the note + the natural third + the natural fifth back. 
This is a called a natural triad (= chord made out of three notes).
"""

"""
Working with containers
"""
c = Composition()
c.set_author('Author', 'tono')
c.set_title('First Mingus Composition')
n = NoteContainer(["C", "E", "G"])

# Transfer note container to composition
# Somehow make composition into container that can then do a MIDI file
