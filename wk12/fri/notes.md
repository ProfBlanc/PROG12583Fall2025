You have a problem.
What's the problem?
You have tasks to do but only have a limited amout of time.
How do you determine which tasks to complete given your free time?

- FreeTime 
    - free time is designated by dow (Day of Week)

- Task
    - name
    - duration (in mins)
    - priority (high, medium, low)


Question to ask when deciding to make attribute
public or private
    - do we want to have control over the data type and value or this attribute?
        Yes: private
        No: public

UML Diagram
U   Unified
M   Modeling
L   Language

*********************************
FreeTime is an interesting class

name: FreeTime
attributes
    - _free_time_by_dow: dict<str:int>
    + foo: str

actions
    + get_free_time(dow: str) -> int
    + set_free_time(dow: str, time: int) -> None
    + use_free_time(dow: str, time_used: int) ->  