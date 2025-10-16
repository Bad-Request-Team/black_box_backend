from database.database import RoadAnalyst
from database.workers.base import DatabaseWorker


class AnalystWorker(DatabaseWorker):
    def __init__(self, database_path: str):
        super().__init__(RoadAnalyst, database_path)

    def add_analyst(self, user: RoadAnalyst):
        self.session.add(user)
        self.session.commit()

    def get_all_analysts(self):
        return self.session.query(RoadAnalyst).all()

    def get_analyst(self, analyst_id: int):
        return self.session.query(RoadAnalyst).filter_by(id=analyst_id).first()