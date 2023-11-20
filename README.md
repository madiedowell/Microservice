# Microservice
This is a microservice for my partners Met API project. It returns a random object ID. 

#Requesting Data
To request data from the microservice, you will need to write a simple get command to the DigiMetInput.txt file.
    
```
    with open("DigiMetInput.txt", "w", encoding = "utf-8") as f:
      f.write("get")
      f.close
```
    
When the microservice reads "get", it will begin execution.

  
#Receiving Data

  To receive data from the microservice, you must read from the DigiMetOutput.txt file. At the end of the microservice's execution, a random object ID will be written to that file as     a string. After you read the object ID string, you must clear the file so it is ready for the next call. 

  ```       
    with open("DigiMetOutput.txt", "r+", encoding = "utf-8") as f:
      objectID = f.readline()
      f.truncate(0)
      f.close()
  ```

#UML Diagram

[UML.pdf](https://github.com/madiedowell/Microservice/files/13358010/UML.pdf)



