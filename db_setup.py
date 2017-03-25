from models import *
from sqlalchemy import func
from db_connect import *


def populate_database():
    """Populate the item catalog database some initial content."""
    session = connect_to_database()
    
    # Make sure the database is empty before running this inital data dump.
    category_count = session.query(func.count(Category.id)).scalar()
    if category_count > 0:
	    session.close()
	    print("Did not populate db...")
    else:
	    category1 = Category(name='Xbox One')
	    session.add(category1)
	    session.commit()
	    category1 = session.query(Category).filter_by(name='Xbox One').one()
	
	    category2 = Category(name='Playstation 4')
	    session.add(category2)
	    session.commit()
	    category2 = session.query(Category).filter_by(name='Playstation 4').one()
	
	    category3 = Category(name='Nintendo Switch')
	    session.add(category3)
	    session.commit()
	    category3 = session.query(Category).filter_by(name='Nintendo Switch').one()
	
	    category4 = Category(name='Oculus Rift')
	    session.add(category4)
	    session.commit()
	    category4 = session.query(Category).filter_by(name='Oculus Rift').one()
	
	    # Create a dummy user for these initial items
	    user1 = User(name="Rick Gamer", email="rgamer@vg.com")
	    session.add(user1)
	    session.commit()
	    user = session.query(User).filter_by(email='rgamer@vg.com').one()
	
	    # Create some games
	    item1 = CategoryItem(
		    name="Titan Fall",
		    description="Humans inside robots gun fighting each other.",
		    # ,picture="https://upload.wikimedia.org/wikipedia/commons/6/66/Polar_Bear_-_Alaska_(cropped).jpg"
		    category="Xbox One",
		    category_id=category1.id,
		    user_id=user.id
	    )
	    session.add(item1)
	    session.commit()
	
	    item2 = CategoryItem(
		    name="The Last of Us",
		    description="Last remaining humans fighting off zombies or something"
		                " to stay alive",
		    # ,picture="https://upload.wikimedia.org/wikipedia/commons/6/66/Polar_Bear_-_Alaska_(cropped).jpg"
		    category="Playstation 4",
		    category_id=category2.id,
		    user_id=user.id
	    )
	    session.add(item2)
	    session.commit()
	
	    item3 = CategoryItem(
		    name="Rayman",
		    description="Some weird creature you play as.",
		    # ,picture="https://upload.wikimedia.org/wikipedia/commons/6/66/Polar_Bear_-_Alaska_(cropped).jpg"
		    category="Nintendo Switch",
		    category_id=category3.id,
		    user_id=user.id
	    )
	    session.add(item3)
	    session.commit()
	
	    item4 = CategoryItem(
		    name="Rollercoaster VR",
		    description="Virtual Reality Roller Coaster..",
		    # ,picture="https://upload.wikimedia.org/wikipedia/commons/6/66/Polar_Bear_-_Alaska_(cropped).jpg"
		    category="Oculus Rift",
		    category_id=category4.id,
		    user_id=user.id
	    )
	    session.add(item4)
	    session.commit()
	    
	    session.close()
	
	    print("Populated database with categories, user and video games...")


if __name__ == '__main__':
	populate_database()