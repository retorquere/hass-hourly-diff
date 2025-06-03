from datetime import timedelta
import logging
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.event import track_time_interval
from homeassistant.helpers.restore_state import RestoreEntity

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    name = entry.data.get("name", "Hourly Difference Sensor")
    sensors = entry.data.get("sensors", [])
    scan_interval = entry.data.get("scan_interval_minutes", 60)
    async_add_entities([HourlyDifferenceSensor(name, sensors, scan_interval)])

class HourlyDifferenceSensor(SensorEntity, RestoreEntity):
    def __init__(self, name, sensors, scan_interval_minutes=60):
        self._attr_name = name
        self._attr_icon = "mdi:stopwatch"
        self._attr_unique_id = f"{name.lower().replace(' ', '_')}_hourly_difference"
        self._sensors = sensors  # List of sensor entity_ids
        self._state = None
        self._previous_sum = None
        self._scan_interval = timedelta(minutes=scan_interval_minutes)

    @property
    def state(self):
        return self._state

    async def async_added_to_hass(self):
        await super().async_added_to_hass()
        old_state = await self.async_get_last_state()
        if old_state is not None:
            try:
                self._state = float(old_state.state)
            except (ValueError, TypeError):
                self._state = None
            self._previous_sum = old_state.attributes.get("previous_sum")
            if self._previous_sum is not None:
                try:
                    self._previous_sum = float(self._previous_sum)
                except (ValueError, TypeError):
                    self._previous_sum = None
        self._update_state()
        track_time_interval(self.hass, self._update_state, self._scan_interval)

    def _update_state(self, now=None):
        sum_current = 0
        for sensor in self._sensors:
            state_obj = self.hass.states.get(sensor)
            try:
                value = float(state_obj.state)
            except (AttributeError, ValueError, TypeError):
                value = 0
            sum_current += value
        if self._previous_sum is not None:
            self._state = sum_current - self._previous_sum
        self._previous_sum = sum_current
        self.async_write_ha_state()

    @property
    def extra_state_attributes(self):
        return {
            "previous_sum": self._previous_sum
        }

    async def async_update(self):
        self._state = 0  # Implement your logic to calculate the difference here
