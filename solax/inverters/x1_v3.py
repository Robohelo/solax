import voluptuous as vol
from solax.inverter import InverterPost
from solax.utils import twoway_div10, div10, div100, to_signed


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
        'PV1 Current':                (5, 'A', div10),  # ok /10
        #'PV2 Current':                (6, 'A', div10),  # ok /10
        'PV1 Voltage':                (3, 'V', div10),  # ok /10
        #'PV2 Voltage':                (4, 'V', div10),  # ok /10

        'Output Current':             (1, 'A', div10), # ok /10
        'Network Voltage':            (0, 'V', div10), # ok /10
        'AC Power':                   (48, 'W', to_signed), # ok    #Feed-In

        'Inverter Temperature1':       (38, 'C', to_signed), # ok ? o. 41 o. 55
        'Inverter Temperature2':       (41, 'C', to_signed), # ok ? o. 41 o. 55
        'Inverter Temperature3':       (55, 'C', to_signed), # ok ? o. 41 o. 55
        'Today\'s Energy':            (13, 'kWh', div10), # ok /10
        'Total Energy':               (11, 'kWh', div10), # ok /10
        'PV1 Power':                  (7, 'W'), # ok
        #'PV2 Power':                  (8, 'W'), # ok

        'Total Feed-in Energy':       (50, 'kWh', div10),  # ok /10 on grid yield
        'Total Consumption':          (52, 'kWh', div10), # ok /10

        'Power Now':                  (2, 'W', to_signed), # ok power inverter
        'Grid Frequency':             (9, 'Hz', div100), # ok /100
    }
     # pylint: enable=duplicate-code
