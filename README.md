# jobs

Background work in lanes, stored in SQL (Postgres, MySQL or SQLite) or in memory.

- Lanes are named by the latency they promise, so long work cannot sit in front of urgent work.
- Every tenant takes an equal turn within a lane, up to a cap.
- A claim is a lease renewed by a heartbeat; a killed worker's job is offered again when the lease lapses.
- Batches fan work out and report when all of it is done; exclusive keys keep one job per key running; queued jobs can be cancelled.
- Handlers and middleware are passed to the worker through anything with `contributions(kind)`; `Contributions` is the minimal one.

```python
from jobs import Contributions, JobHandler, JobOutcome, JobRequest, SQLJobStore, Worker, INTERACTIVE

store = SQLJobStore(engine, create_schema=True)
store.enqueue(JobRequest(lane=INTERACTIVE, kind="film.step", payload={"film": "acme"}))

registry = Contributions()
registry.contribute(JobHandler, MyHandler())
Worker(store, INTERACTIVE, services=registry).work()
```

```bash
virtualenv .venv && .venv/bin/pip install -e '.[dev]'
.venv/bin/pytest
.venv/bin/black --check src tests
```
