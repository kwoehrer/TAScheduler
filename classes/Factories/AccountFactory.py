from abc import ABC, abstractmethod


class AbstractAccountFactory(ABC):
    @abstractmethod
    def create_account(self, creator: User, newAccountAttrbitutes:[]):
        pass

    @abstractmethod
    def delete_account(self, deletor: User, newAccountAttrbitutes:[]):
        pass

    @abstractmethod
    def edit_account(self, editor: User, newAccountAttrbitutes:[]):
        pass

    @abstractmethod
    def edit_username(self, editee: User, newAccountAttrbitutes:[]):
        pass

    @abstractmethod
    def edit_password(self, editee: User, newAccountAttrbitutes:[]):
        pass

    @abstractmethod
    def get_all_users(self, editee: User, newAccountAttrbitutes:[]):
        pass

class ConcreteAccountFactory(AbstractAccountFactory):

    def create_account(self, creator: User, newAccountAttrbitutes:[]):
        pass

    def delete_account(self, deletor: User, newAccountAttrbitutes:[]):
        pass

    def edit_account(self, editor: User, newAccountAttrbitutes:[]):
        pass

    def edit_username(self, editee: User, newAccountAttrbitutes:[]):
        pass

    def edit_password(self, editee: User, newAccountAttrbitutes:[]):
        pass

    def get_all_users(self, editee: User, newAccountAttrbitutes:[]):
        pass