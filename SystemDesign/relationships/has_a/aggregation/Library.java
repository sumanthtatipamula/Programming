package relationships.has_a.aggregation;

import java.util.ArrayList;
import java.util.List;

/**
 *  The Library class has a list of Book objects as a member variable.
 *  The Library class aggregates Book objects, and a Book can exist independently,
 *  even if the Library no longer exists.
 *  The Library class doesn't control the lifespan or ownership of the Book objects.
 */
public class Library {
    private List<Book> books;

    public Library() {
        books = new ArrayList<>();
    }

    public void addBook(Book book) {
        books.add(book);
    }
}
