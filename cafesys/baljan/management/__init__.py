# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext as _
from django.db.models import signals

if "notification" in settings.INSTALLED_APPS:
    from notification import models as notification

    def create_notice_types(app, created_models, verbosity, **kwargs):
        notification.create_notice_type(
                "trade_request",
                _("Trade Request"),
                _("you have received a trade request message"))
        notification.create_notice_type(
                "signup",
                _("Sign-Up"),
                _("you have received a sign-up message"))
    signals.post_syncdb.connect(create_notice_types, sender=notification)
