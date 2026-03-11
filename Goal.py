time_needed_adjustment_factor = 0.5

import time
from datetime import date

class Goal():
    def __init__(self, input_start_date, input_end_date, input_hours_required, input_previous_hours, input_last_weekly_hours):
        self.start_date = input_start_date
        self.end_date = input_end_date
        self.estimated_hours_required = input_hours_required
        self.hours_so_far = input_previous_hours
        self.last_week_hours_spent = input_last_weekly_hours

    def computeHoursPerWeek(self):
        '''
        This function computes the amount of time expected to be
        spent on a goal over the course of a week. It considers
        the start date of the goal, its end date, and the number
        of hours expected to complete it. It also takes into account
        the number of hours that have already been spent upon it, to
        more accurately update the amount of time needed as the goal
        goes on.

        Output: number of hours to spend on the goal, on average
        (The user can then, based on available time that week,
        choose to give more or less time to that goal in particular.
        Over time, this will allow the user to gauge their overall
        goal-setting and how realistic their estimate of time needed
        for a goal was.)

        '''

        '''
        1. Compute the adjusted hours needed through the product of
        user expected hours and 1 + the adjustment factor
        '''
        adjustedHours = self.estimated_hours_required * (1 + time_needed_adjustment_factor)

        '''
        2. Compute the number of weeks between now and the end date.
        '''
        self.start_date = date.fromisoformat(self.start_date)
        self.end_date = date.fromisoformat(self.end_date)

        timeOfGoal = self.end_date - date.fromtimestamp(time.time())
        weeks = timeOfGoal.days / 7

        '''
        3. Compute the adjusted hours left by subtracting the number of
        hours put in thus far from the adjusted hours required.
        '''
        adjustedHoursLeft = adjustedHours - self.hours_so_far

        '''
        4. Compute the division of the adjusted hours left by the number of
        weeks.
        '''
        timePerWeek = adjustedHoursLeft / weeks
        

        '''
        5. Return that value. If start date of goal has not yet come,
        recommend setting aside one hour to start the goal.
        '''
        if (self.start_date > date.fromtimestamp(time.time())):
            return 1
        else:
            return timePerWeek


        

