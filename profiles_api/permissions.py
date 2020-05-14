from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Ensure that the edition is done by an allowed person"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Ensure that the status is updated by the owner only"""

    def has_object_permission(self, request, view, obj):
        """Check if the user as the permission"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
