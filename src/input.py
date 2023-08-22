


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
    #time_sig_pattern = re.compile("[0-9]+/[0-9]+")

    # Time signature
    time_sig = tokens[0]
    #time_sig_pattern.match(time_sig)
    # if match
    # if valid then keep, else break with error
    # find out why the fuck this breaks
    #meter.is_valid(float(time_sig))

    # Find out if token is of valid type
    # Find out what type it is and attach it to token
    # add to final token list
    return tokens

# possible put somewhere else
def parse():
    """
    Creates a parse tree based on tokenized values
    """

def interpret():
    """
    Convert tokens to actual MIDI output
    Each token is assigned meaning, and then passed to the mingus library
    """