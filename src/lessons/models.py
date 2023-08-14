import uuid

from sqlalchemy import Column, String, UUID, Text, ForeignKey
from sqlalchemy.orm import relationship

from database import Base
from course_modules.models import CourseModule


class Lesson(Base):
    __tablename__ = "lesson"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    video = Column(String, nullable=True)
    course_id = Column(UUID(as_uuid=True), ForeignKey("course.id"))
    module_id = Column(UUID(as_uuid=True), ForeignKey("course_module.id"))

    course = relationship("Course", back_populates="lessons")
    module = relationship("CourseModule", back_populates="lessons")

