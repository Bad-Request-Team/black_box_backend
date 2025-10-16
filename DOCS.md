# Backend api

### User web socket

endpoint: /user_ws

Messages from user:

1) type: "start_file_sending"
2) type: "file" <br>
   file_pice: blob
3) type: "end_file_sending"

Messages to user:

1) type: "thread" <br>
   aggressive_percent: list[float] (0 <= x <= 1)
   lane_percent: list[float] (0 <= x)

2) type: "last" <br>
   drivers_count: int (x >= 0) <br>
   aggressive_drivers_count: int (x >= 0) <br>
   normal_drivers_count: int (x >= 0) <br>
   abrupt_braking_count: int (x >= 0) <br>
   abrupt_acceleration_count: int (x >= 0) <br>
   avg_speed: float (x >= 0) <br>
   avg_angle: float (x >= 0) <br>
   avg_acc: float (x >= 0)


### Neural web socket

endpoint: /neural_ws

Messages from neural:

1) avg_speed: float (x >= 0) <br>
   aggressive_percent: float (0 <= x <= 1) <br>
   drivers_count: int (x >= 0) <br>
   aggressive_drivers_count: int (x >= 0) <br>
   normal_drivers_count: int (x >= 0) <br>
   abrupt_braking_count: int (x >= 0) <br>
   abrupt_acceleration_count: int (x >= 0) <br>
   max_speed: float (x >= 0) <br>
   min_speed: float (x >= 0)


Messaged to neural:

1) PNG image
