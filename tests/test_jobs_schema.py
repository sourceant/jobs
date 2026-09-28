"""Whose job it is to make the queue's tables."""

import sqlalchemy as sa

from jobs.models import INTERACTIVE, JobRequest
from jobs.sql import SQLJobStore


def test_the_store_makes_its_tables_when_asked_to(tmp_path):
    engine = sa.create_engine(f"sqlite:///{tmp_path}/asked.db")

    store = SQLJobStore(engine, create_schema=True)

    assert sa.inspect(engine).has_table("jobs")
    assert store.enqueue(JobRequest(lane=INTERACTIVE, kind="test.work"))


def test_the_store_leaves_its_tables_to_migrations_by_default(tmp_path):
    engine = sa.create_engine(f"sqlite:///{tmp_path}/migrated.db")

    SQLJobStore(engine)

    assert not sa.inspect(engine).has_table("jobs")
