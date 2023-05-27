package solid_principle.open_closed.good_class;


/**
 * With this approach,
 * the Shape class is closed for modification because new shapes can be added through
 * inheritance without changing its implementation.
 * It is open for extension because new shapes can be introduced without impacting existing code,
 * promoting maintainability and flexibility.
 */
abstract class Shape {
    public abstract void draw();
}
