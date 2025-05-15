class Config():

    # TODO: implement the salt and pepper loading from the environment
    def __init__(self):
        self.salt = "RANDOMSALTNOTASECRET"
        self.pepper = "iLikeBrownieALot"

    def get_salt(self) -> str:
        return self.salt

    def get_pepper(self) -> str:
        return self.pepper