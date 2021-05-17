// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

contract userRecords {
    enum genderType {male, female}
    struct user {
        string name;
        genderType gender;
    }
    user user_obj;

    function setUser(string memory name, string memory gender) public {
        genderType gender_type = getGenderFromString(gender);
        user_obj = user({name: name, gender: gender_type});
    }

    function getUser() public view returns (string memory, string memory) {
        return (user_obj.name, getGenderToString(user_obj.gender));
    }

    function getGenderFromString(string memory gender)
        internal
        pure
        returns (genderType)
    {
        if (compare(gender, "male")) {
            return genderType.male;
        } else {
            return genderType.female;
        }
    }

    function getGenderToString(genderType gender)
        internal
        pure
        returns (string memory)
    {
        if (gender == genderType.male) {
            return "male";
        } else {
            return "female";
        }
    }

    function compare(string memory a, string memory b)
        internal
        pure
        returns (bool)
    {
        return keccak256(abi.encodePacked(a)) == keccak256(abi.encodePacked(b));
    }
}
