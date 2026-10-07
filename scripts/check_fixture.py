"""Validate the source fixture manifest; runtime behavior belongs to its consumer."""
import configparser
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
config = configparser.ConfigParser(interpolation=None)
config.read_string((root / 'plugin.cfg').read_text())
if config.sections() != ['plugin']:
    raise ValueError('fixture must declare exactly one plugin')
plugin = {key: value.strip().strip('"') for key, value in config['plugin'].items()}
if set(plugin) != {'name', 'description', 'author', 'version', 'script'} or not all(plugin.values()):
    raise ValueError('fixture plugin metadata is incomplete')
if not re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+', plugin['version']):
    raise ValueError('fixture version must be explicit')
script = Path(plugin['script'])
if script.is_absolute() or len(script.parts) != 1 or script.suffix != '.gd':
    raise ValueError('fixture entrypoint must be a local GDScript file')
path = root / script
if not path.is_file() or path.is_symlink():
    raise ValueError('fixture entrypoint is absent or a symlink')
source = path.read_text()
if not source.startswith('@tool\nextends EditorPlugin\n'):
    raise ValueError('fixture must remain an editor plugin')
print('Fixture manifest and source entrypoint verified; no engine runtime claim')
