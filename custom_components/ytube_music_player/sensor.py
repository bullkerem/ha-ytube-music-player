"""Platform for sensor integration."""
import logging
import json
import urllib.request
from datetime import timedelta
from homeassistant.helpers.entity import Entity
from homeassistant.exceptions import NoEntitySpecifiedError
from . import DOMAIN
from .const import *


_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(seconds=15)

EQ_NAMES = {"0": "Normal (Flat)", "1": "Klasik", "2": "Pop / Bass", "3": "Caz (Jazz)", "4": "Vokal"}
CH_NAMES = {"0": "Stereo", "1": "Sol Kanal (L)", "2": "Sağ Kanal (R)"}
MODE_NAMES = {"0": "Boşta", "1": "AirPlay", "2": "DLNA", "10": "Wi-Fi Yayın", "20": "HTTP API", "31": "Spotify", "40": "AUX / Line-In", "41": "Bluetooth", "99": "Uyku"}


def fetch_fabriq_telemetry(ip):
	res = {
		"online": False,
		"ip": ip,
		"device_name": "",
		"firmware": "",
		"rssi": None,
		"wifi_ch": "",
		"group": "0",
		"eq": "0",
		"eq_name": "Normal (Flat)",
		"ch": "0",
		"ch_name": "Stereo",
		"mode": "10",
		"mode_name": "Wi-Fi Yayın",
		"status": "stop",
		"vol": 0,
		"mute": False,
	}
	try:
		with urllib.request.urlopen(f"http://{ip}/httpapi.asp?command=getStatusEx", timeout=2.0) as r1:
			st_ex = json.loads(r1.read().decode("utf-8", errors="ignore"))
		with urllib.request.urlopen(f"http://{ip}/httpapi.asp?command=getPlayerStatus", timeout=2.0) as r2:
			pl_st = json.loads(r2.read().decode("utf-8", errors="ignore"))
		res["online"] = True
		res["device_name"] = st_ex.get("DeviceName", "")
		res["firmware"] = st_ex.get("firmware", "")
		res["rssi"] = st_ex.get("RSSI", "")
		res["wifi_ch"] = st_ex.get("WifiChannel", "")
		res["group"] = str(st_ex.get("group", "0"))
		eq_val = str(pl_st.get("eq", "0"))
		ch_val = str(pl_st.get("ch", "0"))
		md_val = str(pl_st.get("mode", "10"))
		res["eq"] = eq_val
		res["eq_name"] = EQ_NAMES.get(eq_val, eq_val)
		res["ch"] = ch_val
		res["ch_name"] = CH_NAMES.get(ch_val, ch_val)
		res["mode"] = md_val
		res["mode_name"] = MODE_NAMES.get(md_val, md_val)
		res["status"] = pl_st.get("status", "stop")
		res["vol"] = int(pl_st.get("vol", 0))
		res["mute"] = str(pl_st.get("mute", "0")) == "1"
	except Exception:
		pass
	return res


async def async_setup_entry(hass, config, async_add_entities):
	# Run setup via Storage
	_LOGGER.debug("init ytube sensor")
	async_add_entities([yTubeMusicSensor(hass, config)], update_before_add=True)


class yTubeMusicSensor(Entity):
	# Extra Sensor for the YouTube Music player integration + Fabriq Hardware Telemetry

	def __init__(self, hass, config):
		# Initialize the sensor.
		self.hass = hass
		self._state = STATE_ON
		self._device_id = config.entry_id
		self._device_name = config.data.get(CONF_NAME)
		self._attr_unique_id = config.entry_id + "_extra"
		self._attr_has_entity_name = True
		self._attr_name = "Extra"
		self._attr_icon = 'mdi:youtube'
		self.hass.data[DOMAIN][self._device_id]['extra_sensor'] = self
		self._attr = {'tracks', 'search', 'lyrics', 'playlists', 'total_tracks', 'fabriq_salon', 'fabriq_mutfak'}
		self._attributes = {
			'tracks': [],
			'search': [],
			'lyrics': '',
			'playlists': {},
			'total_tracks': 0,
			'fabriq_salon': {},
			'fabriq_mutfak': {}
		}
		_LOGGER.debug("init ytube sensor done")

	@property
	def device_info(self):
		return {
			'identifiers': {(DOMAIN, self._device_id)},
			'name': self._device_name,
			'manufacturer': "Google Inc.",
			'model': DOMAIN
		}

	@property
	def name(self):
		return self._attr_name

	@property
	def state(self):
		return self._state

	@property
	def should_poll(self):
		return True

	async def async_update(self):
		self._ready = True
		_LOGGER.debug("updating ytube sensor")
		try:
			salon_info = await self.hass.async_add_executor_job(fetch_fabriq_telemetry, "192.168.8.124")
			mutfak_info = await self.hass.async_add_executor_job(fetch_fabriq_telemetry, "192.168.8.241")
			self.hass.data[DOMAIN][self._device_id]['fabriq_salon'] = salon_info
			self.hass.data[DOMAIN][self._device_id]['fabriq_mutfak'] = mutfak_info
		except Exception:
			pass

		for attr in self._attr:
			if attr in self.hass.data[DOMAIN][self._device_id]:
				self._attributes[attr] = self.hass.data[DOMAIN][self._device_id][attr]

		try:
			self.async_schedule_update_ha_state()
		except NoEntitySpecifiedError:
			pass

	@property
	def extra_state_attributes(self):
		return self._attributes
