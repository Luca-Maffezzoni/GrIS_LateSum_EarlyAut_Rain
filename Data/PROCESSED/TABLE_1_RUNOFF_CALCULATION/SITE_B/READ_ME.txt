Runoff Comparison Methodology

All runoff values produced by the scripts in this directory must be normalized
by the temporal window they represent before any comparison is performed.

Specifically, each runoff value must be divided by the number of days covered
by its corresponding time span in order to obtain a mean daily runoff value.
This normalization step is required because the different datasets refer to
time windows of unequal length.

All percentage increases or decreases must therefore be computed as the
percentage change in mean daily runoff, not on cumulative runoff values.

Runoff comparison definitions (See the paper for more info):

- RUNOFF 1:
  % Comparison between "runoff_pre_event" and "runoff_pre_pre_event".

- RUNOFF 2:
  % Comparison between "runoff_during_event" and "runoff_pre_event".

- RUNOFF 3:
  % Comparison between "runoff_during_event_only_cyclonic_days" and
  "runoff_week_before_event".

- RUNOFF 4:
  % Comparison between "runoff_during_event_only_cyclonic_days" and
  "runoff_pre_event".

All comparisons must follow the normalization rule described above to ensure
physical consistency and comparability across time periods.