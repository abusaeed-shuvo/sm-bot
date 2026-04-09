class UserService:
    def get_user_data(self, user):
        return {
            "name": user.name,
            "display_name": user.display_name,
            "id": user.id,
            "created_at": user.created_at,
            "avatar": user.display_avatar.url
        }

    def get_avatar(self, user):
        return {
            "name": user.name,
            "avatar": user.display_avatar.url
        }
