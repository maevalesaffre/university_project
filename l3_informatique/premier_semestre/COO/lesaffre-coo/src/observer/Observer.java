package observer;
import vehicle.Vehicle;

/**
 * The Observer interface defines the contract for objects that observe changes in a system.
 */
public interface Observer {

    /**
     * Called to notify the observer about an update in a vehicle.
     *
     * @param vehicle The vehicle that has been updated.
     */
    void update(Vehicle vehicle);

    /**
     * Called to notify the observer about the addition of a new vehicle.
     *
     * @param vehicle The vehicle that has been added.
     */
    void addVehicle(Vehicle vehicle);
}
