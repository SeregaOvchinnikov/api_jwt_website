from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    """Дает возможность изменять или удалять только тот контент,
    автором которого является пользователь."""

    message = 'Изменение чужого контента запрещено'

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
