"""Background work: asked for here, done somewhere else, and accounted for.

Work is separated into lanes named by the latency they promise, so a scan that
takes hours cannot sit in front of a webhook that has seconds. Within a lane
every tenant takes an equal turn up to a fixed cap, so one customer's backlog
cannot starve another's.

A claim on a job is a lease rather than a promise. A worker that is killed
writes nothing, so nothing running inside it could be what recovers its work:
instead the claim simply lapses and the next poll offers the job again. That is
also why delivery is at least once, and why work that must not be repeated says
so with `max_attempts=1` rather than hoping.
"""

from __future__ import annotations

from .contributions import Contributions
from .backoff import after as backoff_after
from .fairness import share
from .interfaces import (
    JobAdmin,
    JobBatches,
    JobHandler,
    JobMiddleware,
    JobQueue,
    JobStore,
    JobWakeup,
)
from .memory import InMemoryJobQueue, InMemoryJobStore
from .middleware import RateLimited, Throttled
from .models import (
    BACKGROUND,
    BATCH,
    BY_NOBODY,
    BY_REPOSITORY,
    BY_WORKSPACE,
    CANCELLED,
    DEAD,
    FAILED,
    INTERACTIVE,
    LANES,
    QUEUED,
    RUNNING,
    SUCCEEDED,
    Batch,
    Candidate,
    Job,
    JobOutcome,
    JobRequest,
    Lease,
)
from .sql import SQLJobStore
from .sweep import Sweeper
from .worker import Worker

__all__ = [
    "BACKGROUND",
    "BATCH",
    "BY_NOBODY",
    "BY_REPOSITORY",
    "BY_WORKSPACE",
    "Batch",
    "CANCELLED",
    "Candidate",
    "Contributions",
    "DEAD",
    "FAILED",
    "INTERACTIVE",
    "InMemoryJobQueue",
    "InMemoryJobStore",
    "Job",
    "JobAdmin",
    "JobBatches",
    "JobHandler",
    "JobMiddleware",
    "JobOutcome",
    "JobQueue",
    "JobRequest",
    "JobStore",
    "JobWakeup",
    "LANES",
    "Lease",
    "QUEUED",
    "RUNNING",
    "RateLimited",
    "SQLJobStore",
    "SUCCEEDED",
    "Sweeper",
    "Throttled",
    "Worker",
    "backoff_after",
    "share",
]
