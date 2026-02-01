def calculate_monthly_units(
    ac_hours,
    fan_hours,
    lights_count,
    washing_per_week,
    fridge=True
):
    """
    Simple rule-based energy calculation
    Units = kWh per month
    """

    AC_UNIT = 1.5      # kWh per hour
    FAN_UNIT = 0.075
    LIGHT_UNIT = 0.06
    FRIDGE_UNIT = 1.2  # per day
    WASH_UNIT = 0.5    # per wash

    daily_units = (
        ac_hours * AC_UNIT +
        fan_hours * FAN_UNIT +
        lights_count * LIGHT_UNIT +
        (FRIDGE_UNIT if fridge else 0)
    )

    monthly_units = daily_units * 30
    monthly_units += washing_per_week * 4 * WASH_UNIT

    return round(monthly_units, 2)
