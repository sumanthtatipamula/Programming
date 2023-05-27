---
title: Single Responsibility Principle
tags:
  - Design Principles
  - System Design
  - Basics
  - SOLID
---

## Introduction

The Single Responsibility Principle (SRP) is a software development principle that states that a class or module should have only one reason to change. In other words, a class should have a single responsibility or job, and that responsibility should be encapsulated within the class.

## Example

### Without SRP

- In this example the `User` class has multiple responsibilities.

- **Authentication Responsibility**: The User class has a method authenticate() that handles user authentication logic. This method checks the username and password and performs the necessary authentication procedures. This is a significant responsibility on its own.

- **Persistence Responsibility**: The User class also has a method save() that handles saving the user to the database. It contains logic for connecting to the database and storing user data. This is another distinct responsibility that should be separated.

- **Email Sending Responsibility**: Additionally, the User class has a method sendEmail() that handles sending emails. It contains the logic for composing and sending email messages. This responsibility is unrelated to authentication or persistence and should be separate.

- This violates the Single Responsibility Principle because the User class has multiple reasons to change. Any modifications or bug fixes related to authentication, persistence, or email sending could potentially impact other parts of the class. It also makes the class harder to understand, test, and maintain.

```java
public class User {
    private String username;
    private String password;

    /**
     * Handles user authentication logic.
     * This method checks the username and password and performs the necessary authentication procedures.
     * This is a significant responsibility on its own.
     */
    public void authenticate(){

    }

    /**
     * Handles saving the user to the database.
     * It contains logic for connecting to the database and storing user data.
     * This is another distinct responsibility that should be separated.
     * @param user
     */
    public void save(User user){

    }

    /**
     * Handles sending emails.
     * It contains the logic for composing and sending email messages.
     * This responsibility is unrelated to authentication or persistence and should be separate.
     * @param user
     * @param message
     */
    public void sendEmail(User user, String message){

    }
}
```

### With SRP

```java

class UserAuthenticator {
  public void authenticate() {
    // Authentication logic
  }
}

class UserRepository {
  public void save(User user) {
    // Save user to the database logic
  }
}

class EmailService {
  public void sendEmail(User user, String message) {
    // Send email logic
  }
}

public class User {
    private String username;
    private String password;
}
```

- **UserAuthenticator class**: This class is responsible for handling user authentication. It contains the logic for verifying user credentials, interacting with authentication mechanisms, and ensuring the user is authenticated. By separating this responsibility into its own class, we have a clear and focused implementation for authentication-related operations.

- **UserRepository class**: This class is responsible for saving user data to the database. It provides methods for interacting with the database, such as inserting or updating user records. By isolating the persistence responsibility in a separate class, we have a dedicated place for handling database operations.

- **EmailService class**: This class is responsible for sending emails. It encapsulates the logic for composing email messages, connecting to an email server, and sending the messages. By abstracting the email sending functionality into its own class, we have a modular and reusable component for handling email-related tasks.

- By adhering to the Single Responsibility Principle, each class now has a clearly defined and single responsibility. It improves code organization, makes the classes more focused and understandable, and allows for easier maintenance and future enhancements. Each class can be independently modified or replaced without affecting the others, promoting code modularity and extensibility.
