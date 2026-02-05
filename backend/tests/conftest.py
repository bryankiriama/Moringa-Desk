import os
import sys
from pathlib import Path

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Ensure backend/app is on the import path for tests.
BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

# Provide safe defaults so settings can load during tests.
os.environ.setdefault("DATABASE_URL", "DUMMY_DATABASE_URL")
os.environ.setdefault("JWT_SECRET", "test-secret")

from app.core.database import Base


@pytest.fixture(scope="session")
def db_url() -> str:
    url = os.getenv("TEST_DATABASE_URL") or os.getenv("DATABASE_URL")
    if not url or url.startswith("DUMMY_"):
        pytest.skip("TEST_DATABASE_URL or DATABASE_URL is required for DB tests")
    return url


@pytest.fixture(scope="session")
def engine(db_url: str):
    engine = create_engine(db_url)
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def db_session(engine):
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.rollback()
        session.close()
