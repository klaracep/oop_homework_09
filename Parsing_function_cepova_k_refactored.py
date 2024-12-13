def create_usernames(data):
    """
    Filters active students and creates unique usernames for them.

    Args:
        data (dict): Input dictionary containing "students" and "active" lists.

    Returns:
        dict: Updated dictionary with filtered "students", "active" states,
              and a new key "usernames" containing unique usernames.
    """
    students = data["students"]
    active_states = data["active"]

    # Filter active students
    active_students = []
    for i in range(len(active_states)):
        if active_states[i]:
            active_students.append(students[i])

    # Create initial usernames
    preliminary_usernames = []
    for student in active_students:
        # Extract the first 3 letters of the first name and the first 5 letters of the last name.
        # Convert both parts to lowercase for consistency.
        first_name = student.split()[0][:3].lower()  # First name: take first 3 characters.
        last_name = student.split()[1][:5].lower()  # Last name: take first 5 characters.
        # Combine last name and first name to form a preliminary username.
        preliminary_usernames.append(last_name + first_name)

    # Ensure usernames are unique
    unique_usernames = []
    for username in preliminary_usernames:
        # Start with the preliminary username.
        unique_username = username
        count = 0  # Counter to modify the username if it's already in use.

        # Check if the username is already in the list of unique usernames.
        while unique_username in unique_usernames:
            count += 1  # Increment the counter to make the username unique.
            # Replace the last character with the counter value to create a new variant.
            unique_username = f"{username[:-1]}{count}"

            # Add the unique username to the list of final usernames.
        unique_usernames.append(unique_username)

    # Update the data dictionary
    updated_data = {
        "students": active_students,  # List of only active students.
        "active": [True] * len(active_students),  # Updated active states (all True).
        "usernames": unique_usernames,  # List of unique usernames.
    }

    return updated_data


# Example usage
data = {
    "students": [
        "Adam Levine", "Monica Muller", "John Deere", "John Deere",
        "John Deere", "Jay Z", "Jay Z", "Meghan Fox"
    ],
    "active": [True, False, True, True, True, True, True, True]
}

print(create_usernames(data))

