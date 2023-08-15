from rest_framework.permissions import BasePermission


class CoursePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='moderator').exists():
            print(f'moderator: {request.user}')
            return True
        elif request.method in ['GET', 'PUT', 'PATCH'] and obj.owner == request.user:
            #print(f'владелец: {obj.owner}')
            return True
        else:
            return False

class IsLessonOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        print(request.user)
        if obj.owner == request.user:
            #print(f'владелец: {obj.owner}')
            return True
        return False

class IsNewModerator(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator') and request.method in ['GET', 'PUT', 'PATCH']:
            #print('i am moderator and method get, put, patch')
            return True
        return False
