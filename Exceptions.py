class notValidName(Exception):
    def __init__(self):
        self.info = '\nThe given name is not valid. '

class notValidID(Exception):
    def __init__(self):
        self.info = '\nThe given ID is not valid. '
