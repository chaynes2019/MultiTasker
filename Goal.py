time_needed_adjustment_factor = 0.5

class Goal():
    def __init__(self, expected_time_to_complete, input_start_date, input_end_date):
        self.expected_time_needed = expected_time_to_complete
        self.start_date = input_start_date
        self.end_date = input_end_date

    def computeTimeDistribution(self):
        pass