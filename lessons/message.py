"""Class to store a message (operator overload, union types, default parameters)."""

class Message:

    to: str
    content: str
    important: bool


    def __init__(self, recipient: str | int, message_content: str = "", importance_flag: bool = False):
        """Consruct a message."""
        self.to = recipient
        self.content = message_content
        self.important = importance_flag

    
    def __str__(self) -> str: 
        output: str = f"Message to {self.to}:\n"
        output += f"Important? {self.important}\n"
        output += f'"{self.content}"'
        return output


    def __mul__(self, factor: int): 
        """Multiplication operator overload."""
        copy_val: str = self.content
        for loop_number in range(1, factor):
            self.content += " " + copy_val


msg_to_self: Message = Message("me", "Do your 110 homework!", True)
print(msg_to_self)
msg_to_camilla: Message = Message("camilla", "you inspire the students!")
print(msg_to_camilla)
msg_to_bear: Message = Message("1")
print(msg_to_bear)
msg_to_bear.content = "Good boy!"
msg_to_bear.important = True
print(msg_to_bear)