time_needed_adjustment_factor = 0.5

class Goal():
    def __init__(self, expected_time_to_complete, input_start_date, input_end_date, input_hours_required, input_previous_hours, input_last_weekly_hours):
        self.expected_time_needed = expected_time_to_complete
        self.start_date = input_start_date
        self.end_date = input_end_date
        self.estimated_hours_required = input_hours_required
        self.hours_so_far = input_previous_hours
        self.last_week_hours_spent = input_last_weekly_hours

    def computeTimeDistribution(self):
        pass