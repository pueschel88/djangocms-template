Don't modify `backend.plugins.default` unless you do that in djangocms-template project - if you want to customize one of them copy-past it into another module under the `plugins` directory, eg `backend.plugins.plugin_name`.

The settings.py and requirements.in files are split into 4 categories, you must adhere to them. On older projets having 5 years worht of random or accidential extention of those files turn maintenence into hell.
- django core
- django packages
- django-cms core
- django-cms packages

The `backend/templates` directory is only for global templates, for anything else use app specific templates per django guidelines.
