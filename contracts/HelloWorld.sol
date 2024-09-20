// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HelloWorld {
    event MessageChanged(address indexed user, string amount);

    // State variable to store the message
    string public message;

    // Constructor runs only once, when the contract is deployed
    constructor(string memory initialMessage) {
        message = initialMessage;
    }

    // Function to update the message
    function updateMessage(string memory newMessage) public {
        message = newMessage;
        emit MessageChanged(msg.sender, message);
    }

    // Function to get the current message
    function getMessage() public view returns (string memory) {
        return message;
    }
}