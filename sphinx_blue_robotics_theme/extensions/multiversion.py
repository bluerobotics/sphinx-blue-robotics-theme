import json
import os
from pathlib import Path
from typing import Any, Dict

from sphinx.application import Sphinx
from sphinx.errors import ExtensionError

__version__ = '1.0.0'

def load_versions_config(app: Sphinx) -> Dict[str, Any]:
    """Load versions configuration from either local file or remote URL."""
    config = app.config
    
    try:
        local_path = Path(app.confdir) / config.versions_local_path
        with open(local_path) as f:
            return json.load(f)
        
        if not versions_config.get('versions'):
            raise ValueError("No versions defined in the configuration.")
        
        default_versions = [v for v in versions_config['versions'] if v.get('is_default')]
        if not default_versions:
            raise ValueError("No default version defined in the configuration.")

        if len(default_versions) > 1:
            raise ValueError("More than one default version defined in the configuration.")

    except Exception as e:
        if config.versions_raise_on_error:
            raise ExtensionError(f"Failed to load versions configuration: {e}")
        
        app.warn(f"Could not load versions configuration: {e}")

def update_context(app: Sphinx, pagename: str, templatename: str, context: Dict, doctree: Any) -> None:
    """Update the HTML context with version information."""
    context['versions'] = app.config.versions_config['versions']
    context['current_version_name'] = os.getenv('MULTIVERSION_CURRENT_NAME', 'latest')
    context['current_version_branch'] = os.getenv('MULTIVERSION_CURRENT_BRANCH', 'master')

def setup(app: Sphinx) -> Dict[str, Any]:
    """Setup the extension."""
    # Add configuration values
    app.add_config_value('versions_source', 'local', 'env')
    app.add_config_value('versions_local_path', '../versions.json', 'env')
    app.add_config_value('versions_raise_on_error', True, 'env')
    
    # Connect events
    app.connect('config-inited', lambda app, config: setattr(config, 'versions_config', 
                                                            load_versions_config(app)))
    app.connect('html-page-context', update_context)
    
    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }