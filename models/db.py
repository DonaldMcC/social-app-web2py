# -*- coding: utf-8 -*-
from gluon.tools import PluginManager
from plugin_social_auth.utils import SocialAuth

# Remove this in production
from gluon.custom_import import track_changes; track_changes(True)
from gluon.contrib.appconfig import AppConfig
myconf = AppConfig(reload=True)

# This needs to be replaced by your own db connection
db = DAL('sqlite://storage.sqlite')

auth = SocialAuth(db)
plugins = PluginManager()

# Enable the "username" field
auth.define_tables(username=True)

# Disable certain auth actions unless you're also using web2py account registration
auth.settings.actions_disabled = ['register', 'change_password', 'request_reset_password']

auth.settings.logout_next = URL(args=request.args, vars=request.get_vars)

# Make user props readonly since these will automatically be updated
# when the user logs on with a new social account anyway.
# NOTE: this fails when lazy tables used.
for prop in ['first_name', 'last_name', 'username', 'email']:
    auth.settings.table_user[prop].writable = False

############################################################################
##
## w2p-social-auth plugin configuration
##
############################################################################

# Configure your API keys
# This needs to be replaced by your actual API keys

    # Configure your API keys
    # This needs to be replaced by your actual API keys
    plugins.social_auth.SOCIAL_AUTH_TWITTER_KEY = myconf.take('psa.twitter_consumer_key')
    plugins.social_auth.SOCIAL_AUTH_TWITTER_SECRET = myconf.take('psa.twitter_secret_key')
    plugins.social_auth.SOCIAL_AUTH_FACEBOOK_KEY = myconf.take('psa.facebook_app_id')
    plugins.social_auth.SOCIAL_AUTH_FACEBOOK_SECRET = myconf.take('psa.facebook_app_secret')
    plugins.social_auth.SOCIAL_AUTH_GOOGLE_PLUS_KEY = myconf.take('psa.google_client_id')
    plugins.social_auth.SOCIAL_AUTH_GOOGLE_PLUS_SECRET = myconf.take('psa.google_client_secret')
    plugins.social_auth.SOCIAL_AUTH_LIVE_KEY = myconf.take('psa.live_key')
    plugins.social_auth.SOCIAL_AUTH_LIVE_SECRET = myconf.take('psa.live_secret')
    #plugins.social_auth.SOCIAL_AUTH_LIVE_LOGIN_REDIRECT_URL = 'http://www.netdecisionmaking.com/gdms/logged-in/'

    # Configure PSA with all required backends
    # Replace this by the backends that you want to use and have API keys for
    plugins.social_auth.SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
        # You need this one to enable manual input for openid.
        # It must _not_ be configured in SOCIAL_AUTH_PROVIDERS (below)
        'social_core.backends.google.GooglePlusAuth',
        'social_core.backends.live.LiveOAuth2',
        'social_core.backends.twitter.TwitterOAuth',
        'social_core.backends.facebook.FacebookOAuth2')

    # Configure the providers that you want to show in the login form.
    # <backend name> : <display name>
    # (You can find the backend name in the backend files as configured above.)
    # Replace this by the backends you want to enable
    # plugins.social_auth.SOCIAL_AUTH_PROVIDERS = {
    #    'live': 'Live',
    #    'twitter': 'Twitter',
    #    'facebook': 'Facebook',
    #    'google-plus': 'Google+',
    #    'persona': 'Mozilla Persona'}

    plugins.social_auth.SOCIAL_AUTH_PROVIDERS = {
    'twitter': 'Twitter',
    'facebook': 'Facebook',
    'google-plus': 'Google+',
    'live': 'Live'}

# Configure app index URL. This is where you are redirected after logon when
# auth.settings.logout_next is not configured.
# If both are not configured there may be no redirection after logout! (returns 'None')
plugins.social_auth.SOCIAL_AUTH_APP_INDEX_URL = URL('init', 'default', 'index')

# Remove or set to False if you are not using Persona
plugins.social_auth.SOCIAL_AUTH_ENABLE_PERSONA = True

# w2p-social-auth can be configured to show a dropdown or buttons.
# 'dropdown' does not require javascript (except for Persona backend) and
# 'buttons' requires js and jquery to be loaded.
# Uncomment this line to use dropdown in stead of the default buttons
# plugins.social_auth.SOCIAL_AUTH_UI_STYLE = 'dropdown'

# This setting only has effect when SOCIAL_AUTH_UI_STYLE = 'buttons'
# Uuncomment this line to apply bootstrap styles to the buttons
# plugins.social_auth.SOCIAL_AUTH_UI_BOOTSTRAP = False

# Uncomment this line to remove icons from buttons
# plugins.social_auth.SOCIAL_AUTH_UI_ICONS = False

