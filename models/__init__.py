from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
	__tablename__ = 'user'
	
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	email = Column(String(250), nullable=False)
	picture = Column(String(250))


class Category(Base):
	__tablename__ = 'category'
	
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	user_id = Column(Integer, ForeignKey('user.id'))
	user_relationship = relationship(User)
	
	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'name': self.name,
			'id': self.id,
			'user_id': self.user_id
		}


class CategoryItem(Base):
	__tablename__ = 'catalog_item'
	
	name = Column(String(80), nullable=False)
	id = Column(Integer, primary_key=True)
	description = Column(String(250))
	picture = Column(String(250))
	category = Column(String(250))
	category_id = Column(Integer, ForeignKey('category.id'))
	category_relationship = relationship(Category)
	user_id = Column(Integer, ForeignKey('user.id'))
	user_relationship = relationship(User)
	
	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'name': self.name,
			'description': self.description,
			'picture': self.picture,
			'id': self.id,
			'catalog': self.catalog,
		}


engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)

