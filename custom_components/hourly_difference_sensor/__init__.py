async def async_setup(hass, config):
    """Set up the Hourly Difference Sensor integration (for discovery)."""
    return True

async def async_setup_entry(hass, entry):
    """Set up Hourly Difference Sensor from a config entry."""
    # Set up your sensor platform here, or forward to the sensor platform
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True

async def async_unload_entry(hass, entry):
    """Unload a config entry."""
    return await hass.config_entries.async_forward_entry_unload(entry, "sensor")