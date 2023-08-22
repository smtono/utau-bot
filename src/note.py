
from dataclasses import dataclass


@dataclass
class Note:
    """
    Represents a musical note with note name, accidental type, octave, and duration
    """
    name: str
    accidental: str
    octave: int
    duration: float
