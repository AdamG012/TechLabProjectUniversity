from django.apps import AppConfig


class TrendsConfig(AppConfig):
    name = 'trends'

    def ready(self):
        from trends.db.admin import article_admin,authentication,usermgmt
        from trends.db.obj import articleModel,adminModel
        from trends.db import article
