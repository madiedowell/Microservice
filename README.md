# Microservice
This is a microservice for my partners Met API project

A. Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call.

  - To request data from the microservice, you will need to write a simple get command to the DigiMetInput.txt file.
    
  - Here is an example call:
    with open("DigiMetInput.txt", "w", encoding = "utf-8") as f:\n
      f.write("get")
      f.close
    
  - When the microservice reads "get", it will begin execution.

  
B. Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.

  -To receive data from the microservice, you must read from the DigiMetOutput.txt file. At the end of the microservice's execution, a random object ID will be written to that file as     a string. After you read the object ID string, you must clear the file so it is ready for the next call. 

  -Here is an example call for reading DigiMetOutput.txt:         
    with open("DigiMetOutput.txt", "r+", encoding = "utf-8") as f:
      objectID = f.readline()
      f.truncate(0)
      f.close()

C. UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your partner (and your grader) will understand

[UML.pdf](https://github.com/madiedowell/Microservice/files/13358010/UML.pdf)



