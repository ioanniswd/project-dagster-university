# from typing import Union

# import dagster as dg


# @dg.schedule(cron_schedule="@daily", target="*")
# def schedules(context: dg.ScheduleEvaluationContext) -> Union[dg.RunRequest, dg.SkipReason]:
#     return dg.SkipReason("Skipping. Change this to return a RunRequest to launch a run.")

import dagster as dg
from dagster_essentials.defs.jobs import trip_update_job, weekly_update_job

trip_update_schedule = dg.ScheduleDefinition(
    job=trip_update_job,
    cron_schedule="0 0 5 * *", # every 5th of the month at midnight
)

weekly_update_schedule = dg.ScheduleDefinition(
    job=weekly_update_job,
    cron_schedule="0 0 * * 1"
)
