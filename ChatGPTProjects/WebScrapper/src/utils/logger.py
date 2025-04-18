# /src/utils/logger.py
# Created by Mahros

# Status
class Status:
  error="error"
  info="info"
  warning="warning"
  question="question"

# Logger
class Logger:
    
  def __init__(self, format:str="%status% %message%"):
    self.__format=format.strip()

  def fstatus(self, status:Status):
    if status == Status.error:
      return "[-]"
    if status == Status.info:
      return "[+]"
    if status == Status.warning:
      return "[!]"
    if status == Status.question:
      return "[?]"

      
  def log(self, msg, status:Status=Status.info):
    # apply format
    result = self.__format.replace("%message%", msg).replace("%status%", self.fstatus(status))

    # then print it to console
    print(result)



# test
if __name__ == "__main__":
  try:
    logger = Logger(format="%status% %message%, now!")
    logger.log(Status.error)
  except Exception as Error:
    print(Error)
