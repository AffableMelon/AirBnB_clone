# Welcome to AirBnB clone project version 1

<p>
The final goal of the project is to deploy my own server as a simple copy of the AirBnB website.
On this part of the poject I will work on the command interpreter to manipulate data without any gui.
The track for the next few months is to deploy a front end website showing the final product, forming a database to store data and objects, an API that provides a commmunication interface between front end and back end data. (Retrieve Create Delete Update...)
</p>

## First Step-
### Building our own COMMAND INTERPRETER!!!
	-Very vital for the rest of the comming projects (milestones above)
	-Manages the followinng:
		- Create a new object (ex: a new User or a new Place)
		- Retrieve an object from a file, a database etc…
		- Do operations on objects (count, compute stats, etc…)
		- Update attributes of an object
		- Destroy an object
BaseModel (class) - takes care of initialization,  serialization and deserialization
Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file:
	-You can’t store and restore a Python instance of a class as “Bytes”, the only way is to convert it to a serializable data
	structure:
		1. Convert an instance to Python built in serializable data structure (list, dict, number and string) - for us it will be 		   the method my_instance.to_json() to retrieve a dictionary
		2. Convert this data structure to a string (JSON format, but it can be YAML, XML, CSV…) - for us it will be a my_string = 		   JSON.dumps(my_dict)
		3. Write this string to a file on disk
	And the process of deserialization?
	The same but in the other way:
		1. Read a string from a file on disk
		2. Convert this string to a data structure. This string is a JSON representation, so it’s easy to convert - for us it will 		   be a my_dict = JSON.loads(my_string)
		3. Convert this data structure to instance - for us it will be a my_instance = MyObject(my_dict) 

