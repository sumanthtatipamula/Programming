package relationships.has_a.composition;


import relationships.has_a.composition.Engine;

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