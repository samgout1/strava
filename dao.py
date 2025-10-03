from typing import List

from business_object import Utilisateur, Activity


class UtilisateurDAO:
    def get(id: str) -> Utilisateur:
        pass


class AcitivityDAO:
    def save(activity: Activity):
        pass

    def get_by_user_id(user_id) -> List[Activity]:
        pass
