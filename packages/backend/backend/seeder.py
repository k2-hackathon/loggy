import sys
import os
pardir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pardir)

import models
from database import session


session = session()

def seed():
    user = models.users.User(
        id = "eeee3e9e-ec6e-ecb9-6d14-da6acfa91824",
        name = "haruki_kurosawa",
    )
    user_details = models.user_details.UserDetails(
        user_id = "eeee3e9e-ec6e-ecb9-6d14-da6acfa91824",
        email = "sample@sample.com",
    )
    lodging = models.lodgings.Lodging(
        user_id = "eeee3e9e-ec6e-ecb9-6d14-da6acfa91824",
    )
    stay = models.stays.Stay(
        user_id = "eeee3e9e-ec6e-ecb9-6d14-da6acfa91824",
    )
    session.add(user)
    session.add(user_details)
    session.add(lodging)
    session.add(stay)
    session.commit()

if __name__ == '__main__':
    BOS = '\033[92m'  # 緑色表示用
    EOS = '\033[0m'

    print(f'{BOS}Seeding data...{EOS}')
    seed()