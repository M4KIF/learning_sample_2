from typing import Annotated

from feedback_platform.infrastructure.persistence.connectors import get_db_session
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

SqliteSessionDep = Annotated[AsyncSession, Depends(get_db_session)]