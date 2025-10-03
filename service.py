from dao import AcitivityDAO

class ActivityService:
    def get_feed(user_id):
        activities = AcitivityDAO().get_by_user_id(user_id)
        return activities
