from uuid import uuid4


class Games:
    uuid: str
    title: str
    short_description: str
    long_description: str

    def __init__(
        self,
        title: str,
        short_description: str,
        long_description: str
    ):
        super().__init__()
        self.uuid = str(uuid4())
        self.title = title
        self.long_description = long_description
        self.short_description = short_description
