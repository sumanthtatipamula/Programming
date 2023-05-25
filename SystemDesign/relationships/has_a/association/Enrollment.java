package relationships.has_a.association;

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
