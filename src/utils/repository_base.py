from abc import ABC, abstractmethod

from fastapi import HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from starlette import status


class AbstractRepository(ABC):
    @abstractmethod
    async def create(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def list(self):
        raise NotImplementedError

    @abstractmethod
    async def retrieve(self, id):
        raise NotImplementedError


class RepositoryBase(AbstractRepository):
    model = None

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create(self,  data: dict):
        query = insert(self.model).values(**data).returning(self.model)
        res = await self.db_session.execute(query)
        await self.db_session.commit()
        return res.scalar_one_or_none()

    async def list(self):
        query = select(self.model)
        res = await self.db_session.execute(query)

        result = res.scalars().all()

        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Not found"
            )

        return result

    async def retrieve(self, id: str):
        query = select(self.model).where(self.model.id == id)
        result = await self.db_session.execute(query)

        instance = result.scalar_one_or_none()

        if not instance:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Not found"
            )

        return instance

    async def retrieve_with_related(self, id: str, related_model):
        query = select(self.model)\
            .where(self.model.id == id)\
            .options(selectinload(getattr(self.model, related_model)))

        result = await self.db_session.execute(query)

        instance = result.scalar_one_or_none()

        if not instance:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Not found"
            )

        return instance
