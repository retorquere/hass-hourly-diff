# Home Assistant Hourly Difference Sensor

[![Open in HACS](https://img.shields.io/badge/Open%20in-HACS-41BDF5?logo=home-assistant&logoColor=white)](https://my.home-assistant.io/redirect/hacs_repository/?owner=retorquere&repository=hass-hourly-diff&category=integration)

This custom component for Home Assistant creates a sensor that calculates the difference between the sum of one or more other sensors at a configurable interval (default: every hour). It is designed to help users monitor changes in sensor values over time.

## Installation

1. **One-Click HACS Installation**:  
   [![Open in HACS](https://img.shields.io/badge/Open%20in-HACS-41BDF5?logo=home-assistant&logoColor=white)](https://my.home-assistant.io/redirect/hacs_repository/?owner=retorquere&repository=hass-hourly-diff&category=integration)  
   Click the button above to open HACS and install this integration directly (Home Assistant 2023.11 or newer).

2. **Manual HACS Installation** (if the button above does not work):
   - Ensure you have [HACS](https://hacs.xyz/) installed in your Home Assistant instance.
   - Add this repository to HACS by going to the HACS interface, selecting "Integrations," and then clicking on the "+" button to add a new repository. Enter the URL of this repository.

3. **Manual Installation**:
   - Clone this repository or download it as a ZIP file.
   - Place the `hourly_difference_sensor` folder in your Home Assistant `custom_components` directory.

## Configuration

To configure the `HourlyDifferenceSensor`, add the following to your `configuration.yaml`:

```yaml
sensor:
  - platform: hourly_difference_sensor
    name: Hourly Difference Sensor
    sensors:
      - sensor.first_sensor
      - sensor.second_sensor
    scan_interval_minutes: 60
```

**Parameters:**

- `name` (string, optional): The name of the sensor.
- `sensors` (list, required): One or more sensor entity IDs to sum.  
  Example:  
  ```yaml
  sensors:
    - sensor.first_sensor
    - sensor.second_sensor
    - sensor.third_sensor
  ```
- `scan_interval_minutes` (integer, required, default: 60): The interval in minutes at which the sum and difference are calculated. Minimum: 1.

Replace the example sensor entity IDs with those you want to sum.

## Usage

Once configured, the `HourlyDifferenceSensor` will automatically calculate the sum of the specified sensors at the configured interval and emit the difference from the previous interval's sum. You can view the sensor's value in the Home Assistant dashboard.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.