---
title: Relationships
tags:
  - Design Principles
  - System Design
  - Basics
---

## Introduction

There are two types of relationships

- Is-a relationship(inheritance)
- Has-a relationship

### Is-a Relationship

- The "is-a" relationship is a fundamental concept in object-oriented programming that represents inheritance or specialization between classes. It signifies that a subclass is a specific type of its superclass. The "is-a" relationship can be understood as a relationship of classification or categorization.

- In an "is-a" relationship, the subclass inherits the properties, methods, and behavior of the superclass. It means that objects of the subclass can be treated as objects of the superclass, and they can be used in any context where the superclass is expected. This concept is also known as subtype polymorphism.

### Has-a Relationship

In object-oriented programming, the "has-a" relationship represents a composition or aggregation between classes, indicating that one class has another class as a part or component. There are several types of "has-a" relationships that can exist between classes. Here are some common types:

- **Composition:**
  Composition represents a strong "has-a" relationship where one class is composed of one or more objects of another class. The lifetime of the composed objects is tightly coupled with the lifetime of the parent object. If the parent object is destroyed, the composed objects are also destroyed. The composed objects cannot exist independently outside of the parent object.

```java
/**
 * A "has-a relationship" represents composition or aggregation,
 * where one class contains an instance of another class as a member variable.
 * It signifies that an object has another object as a part of its composition
 * or as a member of its collection.
 */
public class Car {
    /**
     * the Car class has a member variable engine of type Engine.
     * It represents a composition relationship,
     * where a car has an engine as one of its components.
     * The Car class contains an instance of the Engine class,
     * and it can utilize the engine's properties and behaviors.
     */
    private Engine engine;

    // Other car properties and behaviors

    public Car() {
        engine = new Engine();
    }
}
```

- **Aggregation:**
  Aggregation is a type of "has-a" relationship where one class has a reference to another class, but the referenced object can exist independently and have a longer lifetime than the parent object. In aggregation, the child objects are not tightly bound to the parent object's lifecycle. The child objects can be shared by multiple parent objects or exist even when the parent object is destroyed.

```java
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
```

```java
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
```

- **Association:**
  Association is a looser form of the "has-a" relationship where one class is associated with another class, but they may not have a strong containment or ownership relationship. The associated objects can exist independently and have their own lifecycles. Associations can be bi-directional or uni-directional, and they can have multiplicity (one-to-one, one-to-many, many-to-many) indicating the cardinality of the relationship.

```java
/**
 * The Enrollment class represents the association between a Student and a Course.
 * An enrollment connects a student to a course,
 * but the Student and Course objects can exist independently.
 * The Enrollment class holds references to both the Student and Course objects
 * and manages the relationship between them.
 */
public class Enrollment {
    private Student student;
    private Course course;

    // Enrollment properties and behaviors

    public Enrollment(Student student, Course course) {
        this.student = student;
        this.course = course;
    }
}
```

- **Dependency:**
  Dependency represents a weaker form of the "has-a" relationship, indicating that one class depends on another class for some functionality, but there is no containment or ownership involved. The dependent class uses the services or functionality provided by the other class, but there is no direct reference or direct object relationship between them.

It's important to choose the appropriate type of "has-a" relationship based on the specific requirements and nature of the classes involved. By properly defining and managing these relationships, we can establish the desired object structure and behavior in an object-oriented system.
