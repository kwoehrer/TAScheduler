import abc

from app.models import User, TA, Instructor, Admin


class AbstractUser(abc.ABC):
    @abc.abstractmethod
    def getID(self):
        pass

    @abc.abstractmethod
    def getFirstName(self):
        pass

    @abc.abstractmethod
    def getUsername(self):
        pass

    @abc.abstractmethod
    def getEmail(self) -> str:
        pass

    @abc.abstractmethod
    def getLastName(self):
        pass

    @abc.abstractmethod
    def setFirstName(self, first_name: str):
        pass

    @abc.abstractmethod
    def setLastName(self, last_name: str):
        pass

    @abc.abstractmethod
    def getPhoneNumber(self):
        pass

    @abc.abstractmethod
    def setPhoneNumber(self, phone_number: str):
        pass

    @abc.abstractmethod
    def getHomeAddress(self):
        pass

    @abc.abstractmethod
    def setHomeAddress(self, new_address: str):
        pass

    @abc.abstractmethod
    def getUserType(self):
        pass

    @abc.abstractmethod
    def setUserType(self, new_user_type: str):
        pass

    @abc.abstractmethod
    def setPassword(self, param):
        pass

    @abc.abstractmethod
    def setUsername(self, param):
        pass

    @abc.abstractmethod
    def setEmail(self, param):
        pass


class TAUser(AbstractUser):

    def __init__(self, model: TA):
        self.model = model

    def getUsername(self) -> str:
        return self.model.account_ID.username

    def getEmail(self) -> str:
        return self.model.account_ID.email

    def getID(self) -> int:
        return self.model.account_ID.account_ID

    def getFirstName(self) -> str:
        return self.model.account_ID.first_name

    def getLastName(self) -> str:
        return self.model.account_ID.last_name

    def setFirstName(self, first_name: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.first_name = first_name
        user_obj.save()

    def setLastName(self, last_name: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.last_name = last_name
        user_obj.save()

    def getPhoneNumber(self) -> str:
        return self.model.account_ID.phone_number

    def setPhoneNumber(self, phone_number: str):
        # TODO check if phone number is unique
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.phone_number = phone_number
        user_obj.save()

    def getHomeAddress(self) -> str:
        return self.model.account_ID.home_address

    def setHomeAddress(self, new_address: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.home_address = new_address
        user_obj.save()

    def getUserType(self) -> str:
        return self.model.account_ID.user_type

    def setUserType(self, new_user_type):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.user_type = new_user_type
        user_obj.save()

    def setPassword(self, new_pass: str):
        if new_pass == "" or len(new_pass) < 8:
            raise ValueError("Password must be more than 8 characters long.")
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.password = new_pass
        user_obj.save()

    def setUsername(self, username: str):
        if len(User.objects.filter(username=username)) != 0:
            raise ValueError("A user with this username already exists.")
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.username = username
        user_obj.save()

    def setEmail(self, email):
        if len(User.objects.filter(email=email)) != 0:
            raise ValueError("A user with this email already exists.")
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.email = email
        user_obj.save()


class InstructorUser(AbstractUser):
    def __init__(self, model: Instructor):
        self.model = model

    def getID(self) -> int:
        return self.model.account_ID.account_ID

    def getUsername(self) -> str:
        return self.model.account_ID.username

    def getEmail(self) -> str:
        return self.model.account_ID.email

    def getFirstName(self) -> str:
        return self.model.account_ID.first_name

    def getLastName(self) -> str:
        return self.model.account_ID.last_name

    def setFirstName(self, first_name: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.first_name = first_name
        user_obj.save()

    def setLastName(self, last_name: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.last_name = last_name
        user_obj.save()

    def getPhoneNumber(self) -> str:
        return self.model.account_ID.phone_number

    def setPhoneNumber(self, phone_number: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.phone_number = phone_number
        user_obj.save()

    def getHomeAddress(self) -> str:
        return self.model.account_ID.home_address

    def setHomeAddress(self, new_address: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.home_address = new_address
        user_obj.save()

    def getUserType(self) -> str:
        return self.model.account_ID.user_type

    def setUserType(self, new_user_type):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.user_type = new_user_type
        user_obj.save()

    def setPassword(self, new_pass: str):
        if new_pass == "" or len(new_pass) < 8:
            raise ValueError("Password must be more than 8 characters long.")
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.password = new_pass
        user_obj.save()

    def setUsername(self, username: str):
        if len(User.objects.filter(username=username)) != 0:
            raise ValueError("A user with this username already exists.")
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.username = username
        user_obj.save()

    def setEmail(self, email):
        if len(User.objects.filter(email=email)) != 0:
            raise ValueError("A user with this email already exists.")
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.email = email
        user_obj.save()


class AdminUser(AbstractUser):
    def __init__(self, model: Admin):
        self.model = model

    def getID(self) -> int:
        return self.model.account_ID.account_ID

    def getUsername(self) -> str:
        return self.model.account_ID.username

    def getEmail(self) -> str:
        return self.model.account_ID.email

    def getFirstName(self) -> str:
        return self.model.account_ID.first_name

    def getLastName(self) -> str:
        return self.model.account_ID.last_name

    def setFirstName(self, first_name: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.first_name = first_name
        user_obj.save()

    def setLastName(self, last_name: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.last_name = last_name
        user_obj.save()

    def getPhoneNumber(self) -> str:
        return self.model.account_ID.phone_number

    def setPhoneNumber(self, phone_number: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.phone_number = phone_number
        user_obj.save()

    def getHomeAddress(self) -> str:
        return self.model.account_ID.home_address

    def setHomeAddress(self, new_address: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.home_address = new_address
        user_obj.save()

    def getUserType(self) -> str:
        return self.model.account_ID.user_type

    def setUserType(self, new_user_type: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.user_type = new_user_type
        user_obj.save()

    def setPassword(self, new_pass: str):
        if new_pass == "" or len(new_pass) < 8:
            raise ValueError("Password must be more than 8 characters long.")
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.password = new_pass
        user_obj.save()

    def setUsername(self, username: str):
        if len(User.objects.filter(username=username)) != 0:
            raise ValueError("A user with this username already exists.")
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.username = username
        user_obj.save()

    def setEmail(self, email):
        if len(User.objects.filter(email=email)) != 0:
            raise ValueError("A user with this email already exists.")
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.email = email
        user_obj.save()
