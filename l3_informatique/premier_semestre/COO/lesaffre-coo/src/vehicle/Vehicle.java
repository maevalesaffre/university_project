package vehicle;

import observer.ControlCenter;
import worker.Worker;

/**
 * The Vehicle interface represents a general vehicle in a transportation system.
 */
public interface Vehicle {

    /**
     * Get the unique identifier of the vehicle.
     *
     * @return The vehicle's identifier.
     */
    int getId();

    /**
     * Get the current state of the vehicle.
     *
     * @return True if the vehicle is taken, false otherwise.
     */
    boolean getState();

    /**
     * Set the state of the vehicle.
     *
     * @param state True if the vehicle is taken, false otherwise.
     */
    void setState(boolean state);

    /**
     * Get the condition of the vehicle.
     *
     * @return True if the vehicle is stolen, false otherwise.
     */
    boolean getCondition();

    /**
     * Set the condition of the vehicle.
     *
     * @param condition True if the vehicle is stolen, false otherwise.
     */
    void setCondition(boolean condition);

    /**
     * Get the control center associated with the vehicle.
     *
     * @return The control center associated with the vehicle.
     */
    ControlCenter getControlCenter();

    /**
     * Set the control center associated with the vehicle.
     *
     * @param controlCenter The control center to be set.
     */
    void setControlCenter(ControlCenter controlCenter);

    /**
     * Get the off-service status of the vehicle.
     *
     * @return True if the vehicle is not in working order, false otherwise.
     */
    boolean getOffService();


    /**
     * get the number of locations
     * @return number of locations
     */
    int getNbLocations();


    /**
     * get the max number of locations
     * @return max number of locations
     */
    public int getMaxNbLocations();

    /**
     * Set the off-service status of the vehicle.
     *
     * @param offService True if the vehicle is not in working order, false otherwise.
     */
    void setOffService(boolean offService);

    /**
     * Notify the observer (control center) linked to the vehicle.
     */
    void notifyObserver();

    /**
     * Accept a worker for performing specific tasks on the vehicle.
     *
     * @param worker The worker to perform tasks on the vehicle.
     */
    void accept(Worker worker);


     /**
     * add a location for this bike
     */
    void AddNbLocations();


}
