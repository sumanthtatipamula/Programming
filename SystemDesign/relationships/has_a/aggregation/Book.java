package relationships.has_a.aggregation;

/**
 * Aggregation represents a "has-a relationship"
 * where one class contains or holds a reference to another class
 * as a part of its structure.
 * The aggregated object can exist independently outside the scope of the containing object.
 */
public class Book {
    private String title;
    private String author;

    public Book(String title, String author) {
        this.title = title;
        this.author = author;
    }

    // Book properties and behaviors
}
