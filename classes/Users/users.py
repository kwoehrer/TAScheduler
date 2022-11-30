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


class TAUser(AbstractUser):

    def __init__(self, model: TA):
        self.model = model

    def getID(self) -> User:
        return self.model.account_ID

    def getFirstName(self) -> str:
        return (User.objects.get(account_ID=self.model.account_ID)).first_name

    def getLastName(self) -> str:
        return (User.objects.get(account_ID=self.model.account_ID)).last_name

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
        return (User.objects.get(account_ID=self.model.account_ID)).phone_number

    def setPhoneNumber(self, phone_number: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.phone_number = phone_number
        user_obj.save()

    def getHomeAddress(self) -> str:
        return (User.objects.get(account_ID=self.model.account_ID)).home_address

    def setHomeAddress(self, new_address: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.home_address = new_address
        user_obj.save()

    def getUserType(self) -> str:
        return (User.objects.get(account_ID=self.model.account_ID)).email

    def setUserType(self, new_user_type):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.user_type = new_user_type
        user_obj.save()


class InstructorUser(AbstractUser):
    def __init__(self, model: Instructor):
        self.model = model

    def getID(self) -> User:
        return self.model.account_ID

    def getFirstName(self) -> str:
        return (User.objects.get(account_ID=self.model.account_ID)).first_name

    def getLastName(self) -> str:
        return (User.objects.get(account_ID=self.model.account_ID)).last_name

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
        return (User.objects.get(account_ID=self.model.account_ID)).phone_number

    def setPhoneNumber(self, phone_number: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.phone_number = phone_number
        user_obj.save()

    def getHomeAddress(self) -> str:
        return (User.objects.get(account_ID=self.model.account_ID)).home_address

    def setHomeAddress(self, new_address: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.home_address = new_address
        user_obj.save()

    def getUserType(self) -> str:
        return (User.objects.get(account_ID=self.model.account_ID)).email

    def setUserType(self, new_user_type):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.user_type = new_user_type
        user_obj.save()


class AdminUser(AbstractUser):
    def __init__(self, model: Admin):
        self.model = model

    def getID(self) -> User:
        return self.model.account_ID

    def getFirstName(self) -> str:
        return (User.objects.get(account_ID=self.model.account_ID)).first_name

    def getLastName(self) -> str:
        return (User.objects.get(account_ID=self.model.account_ID)).last_name

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
        return (User.objects.get(account_ID=self.model.account_ID)).phone_number

    def setPhoneNumber(self, phone_number: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.phone_number = phone_number
        user_obj.save()

    def getHomeAddress(self) -> str:
        return (User.objects.get(account_ID=self.model.account_ID)).home_address

    def setHomeAddress(self, new_address: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.home_address = new_address
        user_obj.save()

    def getUserType(self) -> str:
        return (User.objects.get(account_ID=self.model.account_ID)).email

    def setUserType(self, new_user_type: str):
        acc_id = self.model.account_ID
        user_obj = User.objects.get(account_ID=acc_id)
        user_obj.user_type = new_user_type
        user_obj.save()