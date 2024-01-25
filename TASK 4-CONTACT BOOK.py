contacts = []  # List to store contact dictionaries

def add_contact():
  """Add a new contact to the list."""
  name = input("Enter name: ")
  phone = input("Enter phone number: ")
  email = input("Enter email address (optional): ")
  address = input("Enter address (optional): ")
  contact = {"name": name, "phone": phone, "email": email, "address": address}
  contacts.append(contact)
  print("Contact added successfully!")

def view_contacts():
  """Display all contacts in the list."""
  if not contacts:
    print("No contacts found!")
  else:
    print("---------- Contact List ----------")
    for contact in contacts:
      print(f"Name: {contact['name']}")
      print(f"Phone: {contact['phone']}")
      if contact["email"]:
        print(f"Email: {contact['email']}")
      if contact["address"]:
        print(f"Address: {contact['address']}")
      print("-------")

def search_contact():
  """Search for a contact by name or phone number."""
  name_or_phone = input("Enter name or phone number: ")
  for contact in contacts:
    if name_or_phone.lower() in contact["name"].lower() or name_or_phone == contact["phone"]:
      print(f"Found contact:")
      print(f"Name: {contact['name']}")
      print(f"Phone: {contact['phone']}")
      if contact["email"]:
        print(f"Email: {contact['email']}")
      if contact["address"]:
        print(f"Address: {contact['address']}")
      break
  else:
    print("Contact not found!")

def update_contact():
  """Update an existing contact."""
  name = input("Enter name of the contact to update: ")
  for i, contact in enumerate(contacts):
    if name.lower() == contact["name"].lower():
      field = input("What field do you want to update? (name, phone, email, address): ")
      new_value = input("Enter the new value: ")
      contacts[i][field] = new_value
      print("Contact updated successfully!")
      break
  else:
    print("Contact not found!")

def delete_contact():
  """Delete a contact."""
  name = input("Enter name of the contact to delete: ")
  for i, contact in enumerate(contacts):
    if name.lower() == contact["name"].lower():
      del contacts[i]
      print("Contact deleted successfully!")
      break
  else:
    print("Contact not found!")

def main():
  # Display menu options
  print("---------- Contact Book ----------")
  print("1. Add Contact")
  print("2. View Contact List")
  print("3. Search Contact")
  print("4. Update Contact")
  print("5. Delete Contact")
  print("6. Exit")

  # User input loop
  while True:
    choice = input("Enter your choice: ")
    if choice.isdigit() and int(choice) in range(1, 7):
      if choice == "1":
        add_contact()
      elif choice == "2":
        view_contacts()
      elif choice == "3":
        search_contact()
      elif choice == "4":
        update_contact()
      elif choice == "5":
        delete_contact()
      else:
        break
    else:
      print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
  main()
