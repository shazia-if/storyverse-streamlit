from sqlalchemy.orm import  declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from database import Base
from sqlalchemy import UniqueConstraint
#from datetime import date


# ==========================
# STORY TABLE
# ==========================
class Story(Base):
    __tablename__ = "story"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    title: Mapped[str]

    description: Mapped[str | None]

    tags: Mapped[str| None]
    status: Mapped[str |None]  #ongoing or completed
 



# ==========================
# CHARACTER TABLE
# ==========================
class Character(Base):
    __tablename__ = "character"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    story_id: Mapped[int] = mapped_column(
        ForeignKey("story.id")
    )

    name: Mapped[str]

    character_type: Mapped[str | None]

    motivation: Mapped[str | None]

    description: Mapped[str | None]

  



# ==========================
# LOCATION TABLE
# ==========================
class Location(Base):
    __tablename__= "location"

    id: Mapped[int]= mapped_column(primary_key=True)
    story_id: Mapped[int]= mapped_column(ForeignKey("story.id"))
    name: Mapped[str]
    location_type: Mapped[str|None]
    description: Mapped[str| None]
    parent_location_id: Mapped[int| None]= mapped_column(ForeignKey("location.id"),nullable= True)





# ==========================
# CHAPTERS TABLE
# ==========================
class Chapter(Base):
    __tablename__="chapter"
    id: Mapped[int]= mapped_column(primary_key=True)
    story_id: Mapped[int]= mapped_column(ForeignKey("story.id"))
    chapter_number:Mapped[int]
    chapter_title:Mapped[str| None]
    chapter_summary: Mapped[str| None]



# ==========================
# SCENES TABLE
# ==========================
class Scene(Base):
    __tablename__="scene"
    id: Mapped[int]= mapped_column(primary_key=True)
    story_id: Mapped[int]= mapped_column(ForeignKey("story.id"))
    chapter_id:Mapped[int]= mapped_column(ForeignKey("chapter.id"), nullable=True)

    title:Mapped[str|None]
    summary: Mapped[str|None]
    location_id: Mapped[int| None]=mapped_column(ForeignKey("location.id"))
    scene_type: Mapped[str|None]
    notes: Mapped[str|None]



class ReaderOrder(Base):
    __tablename__="SceneReaderOrder"
    id: Mapped[int]= mapped_column(primary_key=True)
    chapter_id: Mapped[int]= mapped_column(ForeignKey("chapter.id"), nullable=True)
    scene_id: Mapped[int]= mapped_column(ForeignKey("scene.id"), unique=True)
    position: Mapped[int]
    __table_args__ = (UniqueConstraint(
            "chapter_id",
            "position",
            name="uq_chapter_position"
        ),
    )




class TimelineOrder(Base):
    __tablename__="SceneTimelineOrder"
    id: Mapped[int]= mapped_column(primary_key=True)
    story_id: Mapped[int]= mapped_column(ForeignKey("story.id"))
    scene_id: Mapped[int]= mapped_column(ForeignKey("scene.id"), unique=True)
    position: Mapped[int]
    __table_args__ = ( UniqueConstraint(
            "story_id",
            "position",
            name="uq_story_timeline_position"
        ),
    )


# ==========================
# SCENE CHARACTER TABLE
# ==========================
class SceneCharacter(Base):
    __tablename__= "scene_character"
    id: Mapped[int]= mapped_column(primary_key=True)
    story_id: Mapped[int]= mapped_column(ForeignKey("story.id"))
    scene_id: Mapped[int]= mapped_column(ForeignKey("scene.id"))
    character_id: Mapped[int]= mapped_column(ForeignKey("character.id"))

