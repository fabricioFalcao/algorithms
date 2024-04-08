def study_schedule(permanence_period, target_time):
    counter = 0
    try:
        assert 0 <= target_time <= 24
        for log_in_time, log_out_time in permanence_period:
            assert 0 <= log_in_time <= 24
            assert 0 <= log_out_time <= 24

            if log_in_time <= target_time <= log_out_time:
                counter += 1
    except (TypeError, AssertionError, ValueError):
        return None

    return counter
