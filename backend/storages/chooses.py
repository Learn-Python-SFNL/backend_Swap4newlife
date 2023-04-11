from backend.db import db_session
from backend.models import Choose


class ChoosesStorage:

    def add(self, source_id: int, target_id: int) -> Choose:
        choose = Choose(
            source_product_id=source_id,
            target_product_id=target_id,
        )
        db_session.add(choose)
        db_session.commit()
        return choose
