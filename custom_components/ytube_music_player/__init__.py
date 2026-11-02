"""Provide the initial setup."""
import importlib
import sys
import logging
from .const import *

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass, config):
	"""Provide Setup of platform."""
	return True


async def async_setup_entry(hass, config_entry):
	"""Set up this integration using UI/YAML."""
	hass.data.setdefault(DOMAIN, {})
	hass.data[DOMAIN][config_entry.entry_id] = {}
	hass.config_entries.async_update_entry(config_entry, data=ensure_config(config_entry.data))

	if not config_entry.update_listeners:
		config_entry.add_update_listener(async_update_options)

	# Add entities to HA
	await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)
	return True


async def async_remove_entry(hass, config_entry):
	"""Handle removal of an entry."""
	for platform in PLATFORMS:
		try:
			await hass.config_entries.async_forward_entry_unload(config_entry, platform)
			_LOGGER.info(
				"Successfully removed entities from the integration"
			)
		except ValueError:
			pass


async def async_update_options(hass, config_entry):
	_LOGGER.debug("Config updated, reload the entities and submodules.")
	for platform in PLATFORMS:
		await hass.config_entries.async_forward_entry_unload(config_entry, platform)
	for mod_name in [
		"custom_components.ytube_music_player.const",
		"custom_components.ytube_music_player.browse_media",
		"custom_components.ytube_music_player.sensor",
		"custom_components.ytube_music_player.select",
		"custom_components.ytube_music_player.media_player",
	]:
		if mod_name in sys.modules:
			try:
				importlib.reload(sys.modules[mod_name])
			except Exception as err:
				_LOGGER.warning("Reload %s failed: %s", mod_name, err)
	await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)
