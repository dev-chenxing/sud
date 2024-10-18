class Player:
    def __init__(self, id: str):
        self.id = id
        self.surname = ""
        self.given_name = ""
        self.ad_password = ""

    def __str__(self):
        return f"Player {{ id: {self.id} }}"
