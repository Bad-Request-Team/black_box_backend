from database import RoadAnalyst


class AnalystWorker:
    def __init__(self, connect_link: str):
        self.connect_link = connect_link

    def add(self, data: RoadAnalyst):
        pass