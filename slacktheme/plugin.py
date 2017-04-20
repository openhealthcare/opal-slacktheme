"""
Plugin definition for the slacktheme OPAL plugin
"""
from opal.core import plugins

from slacktheme.urls import urlpatterns

class SlackthemePlugin(plugins.OpalPlugin):
    """
    Main entrypoint to expose this plugin to our OPAL application.
    """
    urls = urlpatterns
    javascripts = {
        # Add your javascripts here!
        'opal.slacktheme': [
            # 'js/slacktheme/app.js',
            # 'js/slacktheme/controllers/larry.js',
            # 'js/slacktheme/services/larry.js',
        ]
    }

    stylesheets = [
        'css/slack.css'
    ]

    def list_schemas(self):
        """
        Return any patient list schemas that our plugin may define.
        """
        return {}

    def roles(self, user):
        """
        Given a (Django) USER object, return any extra roles defined
        by our plugin.
        """
        return {}
