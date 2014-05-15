# ===================================================================
# App Kernel - kernel.py
# ===================================================================
#!/usr/bin/env python2

# define app structure
from app import app
from app.models import models
from app.views import views
from app.controllers import controllers
from app.forms import forms


# register app structure
app.register_blueprint(models)
app.register_blueprint(views)
app.register_blueprint(controllers)
app.register_blueprint(forms)

# run the app
import os
if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='localhost', port=port, debug=True, use_debugger=True)