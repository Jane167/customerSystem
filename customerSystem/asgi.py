# customerSystem/asgi.py
# import os
 
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# import project.routing
 
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
 
# application = ProtocolTypeRouter({
#   "http": get_asgi_application(),
#   "websocket": AuthMiddlewareStack(
#         URLRouter(
#             project.routing.websocket_urlpatterns
#         )
#     ),
# })
import os

import django
from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from project import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": AllowedHostsOriginValidator(    # 新增部分
            AuthMiddlewareStack(                         
                URLRouter(
                    routing.websocket_urlpatterns
                )
            )
        ),
})