package solid_principle.open_closed.bad_class;

enum ShapeType {
    CIRCLE,
    RECTANGLE
}


/**
 * In the bad example, the draw() method in the Shape class uses conditional statements
 * to determine the shape type and execute the corresponding drawing logic.
 * If a new shape type is introduced, such as a triangle,
 * the Shape class would need to be modified, violating the Open-Closed Principle.
 */
public class Shape {
    private ShapeType type;

    public Shape(ShapeType type) {
        this.type = type;
    }

    public void draw() {
        if (type == ShapeType.CIRCLE) {
            // Draw circle logic
        } else if (type == ShapeType.RECTANGLE) {
            // Draw rectangle logic
        }
    }
}

