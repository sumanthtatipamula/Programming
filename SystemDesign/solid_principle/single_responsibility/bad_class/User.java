package solid_principle.single_responsibility.bad_class;

/***
 * In this example the `User` class has multiple responsibilities.
 * It handles authentication, saving user to database, and sending emails.
 */


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
