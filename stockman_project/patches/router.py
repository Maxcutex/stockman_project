from rest_framework import routers


class DefaultRouter(routers.DefaultRouter):
    """
    Extends 'DefaultRouter class to add a method for extending url routes from another router
    """

    def extend(self, router):
        """
        Extend the routes with url routes fo the passed in router 

        Args:
            router: SimpleRouter instance containing route definitions
        """

        self.registry.extend(router.registery)
