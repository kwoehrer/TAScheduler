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
        if not (isinstance(creator, AdminUser)) or creator.getUserType() != "Admin":
            raise TypeError("Only admin user accounts can create accounts.")
        # Verify newAccountAttributes is correct

        username = newAccountAttributes['username']
        if len(User.objects.filter(username=username)) != 0:
            raise ValueError("A user with this username already exists.")

        password = newAccountAttributes['password']
        if password == "" or len(password) < 8:
            raise ValueError("Password must be more than 8 characters long.")

        first_name = newAccountAttributes['first_name']
        last_name = newAccountAttributes['last_name']

        phone_number = None
        home_address = None
        try:
            if newAccountAttributes['phone_number'] != None and newAccountAttributes['phone_number'] != '':
                phone_number = newAccountAttributes['phone_number']
                if len(User.objects.filter(phone_number=phone_number)) != 0:
                    raise ValueError("A user with this phone number already exists.")

            home_address = newAccountAttributes['home_address']
        except KeyError:
            pass

        email = newAccountAttributes['email']
        if len(User.objects.filter(email=email)) != 0:
            raise ValueError("A user with this email already exists.")

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
        if not isinstance(deletor, AdminUser) or deletor.getUserType() != "Admin":
            raise TypeError("Only admin user accounts can delete accounts.")

        #verify account is not already deleted
        deletee_id = deletee.getID()
        if len(User.objects.filter(account_ID=deletee_id)) == 0:
            raise ValueError("Cannot delete an account that has already been deleted.")

        User.objects.filter(account_ID=deletee_id).delete() #should propagate to subtable due to cascade effects

