import voluptuous as vol
from solax.inverter import InverterPost
from solax.utils import div10, div100, to_signed, no_zero_div10


class X1_V3(InverterPost):
    # pylint: disable=duplicate-code
    _schema = vol.Schema({
        vol.Required('sn'): str,
        vol.Required('ver'): str,
        vol.Required('type'): int,
        vol.Required('Data'): vol.Schema(
            vol.All(
                [vol.Coerce(float)],
                vol.Any(
                    vol.Length(min=100, max=100),
                ),
            )
        ),
        vol.Required('Information'): vol.Schema(
            vol.All(
                vol.Length(min=10, max=10)
                )
            ),
    }, extra=vol.REMOVE_EXTRA)

    _sensor_map = {
        'PV1 Current':                (5, 'A', div10),
        'PV1 Voltage':                (3, 'V', div10),

        'Output Current':             (1, 'A', div10),
        'Network Voltage':            (0, 'V', div10),
        'AC Power':                   (48, 'W', to_signed),

        'Operating Hours Counter':    (41, 'h', to_signed),
        'Inverter Temperature':       (55, 'C', to_signed),
        'Today\'s Energy':            (13, 'kWh', no_zero_div10),
        'Total Energy':               (11, 'kWh', no_zero_div10),
        'PV1 Power':                  (7, 'W'),

        'Total Feed-in Energy':       (50, 'kWh', no_zero_div10),
        'Total Consumption':          (52, 'kWh', no_zero_div10),

        'Power Now':                  (2, 'W', to_signed),
        'Grid Frequency':             (9, 'Hz', div100),
    }
     # pylint: enable=duplicate-code
