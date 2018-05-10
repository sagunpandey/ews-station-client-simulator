# Early Warning System: River Station Simulator
A client app/script written in Python to simulate river water level monitoring stations.

Water client uses multiprocessing to create multiple processes. These processes each generate a random water level. This water level is stored along with the time of reading and process id. This data is then displayed on the screen using Tkinter, which is a library that is included in python to create a GUI. The data is also converted to JSON format and sent using the Rest API to the main server. Each process updates its water level at varying intervals and resends the data to the screen and main server.

**NOTE** Currently, you need to have your EWS Server running in order to run this app. Configure the server address and make sure it is calling the API `/reading`.
