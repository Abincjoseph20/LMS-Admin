from django.core.exceptions import PermissionDenied
from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.timezone import now
from datetime import datetime


from functools import wraps
from django.core.exceptions import PermissionDenied

def allowed_roles(roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Check if user is an admin or superuser
            user_role = request.user.roles
            print("User Role:", request.user.roles)
            if 'admin' in roles and (request.user.roles == 'admin' or request.user.is_superadmin):
                return view_func(request, *args, **kwargs)
               
             # Allow if role is admin, teacher, or guest (treated as instructor)
            if 'admin_and_instructor' in roles and (
                user_role == 'admin' or user_role == 'Teacher' or user_role == 'guest'
            ):
                return view_func(request, *args, **kwargs)

            # Direct match
            if user_role in roles:
                return view_func(request, *args, **kwargs)

            # If none match, deny access
            raise PermissionDenied
        
        return _wrapped_view
    return decorator