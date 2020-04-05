Don't modify `backend.plugins.default` unless you do that in djangocms-template project - if you want to customize one of them copy-past it into another module under the `plugins` directory, eg `backend.plugins.plugin_name`. Otherwise they will overwritten.

The `backend/templates` directory is only for global templates, for anything else use app specific templates per django guidelines.

The settings.py and requirements.in files are split into 4 categories, you must adhere to them. On older projects having 5 years worth of random or accidental extension of those files turn maintenance into hell.
- django core
- django packages
- django-cms core
- django-cms packages

The project dependencies are hierarchical, the indentation indicates that the packages below were added as peer-dependencies. 