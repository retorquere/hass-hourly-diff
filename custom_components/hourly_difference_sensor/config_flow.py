"""Config flow for Hourly Difference Sensor integration."""
from __future__ import annotations

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_NAME
from homeassistant.helpers import selector

DOMAIN = "hourly_difference_sensor"
CONF_SENSORS = "sensors"
CONF_SCAN_INTERVAL = "scan_interval_minutes"

class HourlyDifferenceSensorConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Hourly Difference Sensor."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            sensors = user_input.get(CONF_SENSORS, [])
            if not sensors:
                errors[CONF_SENSORS] = "required"
            else:
                return self.async_create_entry(
                    title=user_input.get(CONF_NAME, "Hourly Difference Sensor"),
                    data=user_input,
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Optional(CONF_NAME, default="Hourly Difference Sensor"): str,
                vol.Required(CONF_SENSORS): selector.EntitySelector(
                    {
                        "multiple": True,
                        "domain": "sensor"
                    }
                ),
                vol.Optional(CONF_SCAN_INTERVAL, default=60): vol.All(int, vol.Range(min=1)),
            }),
            errors=errors,
        )