import voluptuous as vol

from solax.inverter import Inverter
from solax.units import Total, Units
from solax.utils import startswith
from solax.utils import div10, div100, to_signed

class X1G4(Inverter):
    # pylint: disable=duplicate-code
    _schema = vol.Schema(
        {
            vol.Required("type"): vol.All(str, startswith("X1-")),
            vol.Required("SN"): str,
            vol.Required("ver"): str,
            vol.Required("Data"): vol.Schema(
                vol.All(
                    [vol.Coerce(float)],
                    vol.Any(
                        vol.Length(min=100, max=100),
                    ),
                )
            ),
            vol.Required("Information"): vol.Schema(vol.All(vol.Length(min=10, max=10))),
        }, extra=vol.REMOVE_EXTRA
    )

    @classmethod
    def response_decoder(cls):
        return {
            "PV1 Current": (5, Units.A, div10),
            "PV1 Voltage": (3, Units.V, div10),

            "Output Current": (1, Units.A, div10),
            "Network Voltage": (0, Units.V, div10),
            "AC Power": (48, Units.W, to_signed),

            "Operating Hours": (41, Units.H),
            "Inverter Temperature": (55, Units.C, to_signed),
            "Today's Energy": (13, Units.KWH, div10),
            "Total Energy": (11, Total(Units.KWH), div10),
            "PV1 Power": (7, Units.W),

            "Total Feed-in Energy": (50, Total(Units.KWH), div10),
            "Total Consumption": (52, Total(Units.KWH), div10),

            "Power Now": (2, Units.W, to_signed),
            "Grid Frequency": (9, Units.HZ, div100)
        }
    # pylint: enable=duplicate-code
