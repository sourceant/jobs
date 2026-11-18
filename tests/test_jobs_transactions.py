import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from jobs import BACKGROUND, JobRequest, SQLJobStore


@pytest.mark.parametrize("orm", [False, True])
def test_enqueued_work_commits_and_rolls_back_with_the_callers_transaction(
    tmp_path, orm
):
    engine = create_engine(f"sqlite:///{tmp_path / 'jobs.sqlite'}")
    store = SQLJobStore(engine, create_schema=True)
    try:
        with pytest.raises(RuntimeError, match="Rollback"):
            with engine.begin() as connection:
                session = Session(bind=connection) if orm else connection
                identifier = store.enqueue(
                    JobRequest(BACKGROUND, "events.deliver"), session=session
                )
                if orm:
                    session.close()
                raise RuntimeError("Rollback")
        assert store.read(identifier) is None
        with engine.begin() as connection:
            session = Session(bind=connection) if orm else connection
            identifier = store.enqueue(
                JobRequest(BACKGROUND, "events.deliver"), session=session
            )
            if orm:
                session.close()
        assert store.read(identifier).state == "queued"
    finally:
        engine.dispose()
