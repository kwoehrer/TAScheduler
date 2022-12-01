from abc import ABC, abstractmethod

from app.models import User, Admin, TA, Instructor
from classes.Users.users import InstructorUser, TAUser, AdminUser, AbstractUser


class AbstractAccountFactory(ABC):
    @abstractmethod
    def create_account(self, creator: AbstractUser, newAccountAttrbitutes: []):
        pass

    @abstractmethod
    def delete_account(self, deletor: AbstractUser, newAccountAttrbitutes: []):
        pass


class ConcreteAccountFactory(AbstractAccountFactory):

    def create_account(self, creator: AbstractUser, newAccountAttributes: []):
        # Verify creator is an admin
        if not (isinstance(creator, AdminUser)):
            raise TypeError("Only admin user accounts can create accounts.")
        # Verify newAccountAttributes is correct
        username = newAccountAttributes['username']
        password = newAccountAttributes['password']
        if password == "" or len(password) < 8:
            raise ValueError("Password must be more than 8 characters long.")
        first_name = newAccountAttributes['first_name']
        last_name = newAccountAttributes['last_name']
        phone_number = newAccountAttributes['phone_number']
        home_address = newAccountAttributes['home_address']
        email = newAccountAttributes['email']
        user_type = newAccountAttributes['user_type']

        new_user = User(username=username, password=password, first_name=first_name, last_name=last_name,
                        phone_number=phone_number, home_address=home_address, email=email, user_type=user_type)
        new_user.save()

        # look at type of user and create a reference to the user in its sub-table
        new_subtype = None
        if user_type == "Admin":
            new_subtype = Admin(account_ID=new_user)
        elif user_type == "TA":
            new_subtype = TA(account_ID=new_user)
        elif user_type == "Instructor":
            new_subtype = Instructor(account_ID=new_user)

        new_subtype.save()  # Should throw erorr if usertype was not correct.

    def delete_account(self, deletor: AbstractUser, deletee: AbstractUser):
        #verify our logged in user/deletor can delete accounts
        if not (isinstance(deletor, AdminUser)):
            raise TypeError("Only admin user accounts can delete accounts.")

        deletee_id = deletee.get_id()

        User.objects.filter(account_ID=deletee_id).delete() #should propagate to subtable due to cascade effects

