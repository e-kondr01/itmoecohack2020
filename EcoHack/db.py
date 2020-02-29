"""
1: box_id, place_id, is_full
2: place_id, building_id, floor, otdel
3: building_id, box_num, people_num
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""
Base = declarative_base()
engine = create_engine("sqlite:///C:\\itmoecohack\\boxes.db")
session = sessionmaker(bind=engine)
"""


class Boxe(Base):
    __tablename__ = "boxes"
    box_id = Column(Integer, primary_key=True)
    place_id = Column(Integer, ForeignKey("Place.place_id"))
    is_full = Column(Boolean, default=False)


class Place(base):
    __tablename__ = "places"
    place_id = Column(Integer, primary_key=True)
    building_id = Column(Integer, ForeignKey("Building.building_id"))
    floor = Column(Integer)
    otdel = Column(Text)


class Building(base):
    __tablename__ = "buildings"
    building_id = Column(Integer, primary_key=True)
    box_num = Column(Integer)
    people_num = Column(Integer)


"""
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    s = session()
    news_list = get_news("https://news.ycombinator.com/", n_pages=35)
    for post in news_list:
        news = News(title=post['title'],
                    author=post['author'],
                    url=post['url'],
                    comments=post['comments'],
                    points=post['points'])
        s.add(news)
        s.commit()
"""
