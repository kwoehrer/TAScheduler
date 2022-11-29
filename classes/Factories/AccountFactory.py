from abc import ABC, abstractmethod


class AbstractAccountFactory(ABC):
    @abstractmethod
    def create_account(self, creator: User, newAccountAttrbitutes: []):
        pass

    @abstractmethod
    def delete_account(self, deletor: User, newAccountAttrbitutes: []):
        pass


class ConcreteAccountFactory(AbstractAccountFactory):

    def create_account(self, creator: User, newAccountAttrbitutes: []):
        pass

    def delete_account(self, deletor: User, newAccountAttrbitutes: []):
        pass
