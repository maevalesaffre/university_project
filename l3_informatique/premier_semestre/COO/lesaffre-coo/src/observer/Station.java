package observer;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import exceptions.StationCapacityExceededException;
import exceptions.StationEmptyException;
import vehicle.Vehicle;
import worker.Repairer;
import worker.User;
import worker.Worker;

/**
 * The Station class represents a location where vehicles can be stored.
 */
public class Station {

    private int idStation;
    private String name;
    private int capacity;
    private ArrayList<Vehicle> vehicles;
    private long time;
    private ControlCenter controlCenter;

    /**
     * Creates a station with the given ID, name, and capacity.
     *
     * @param idStation The unique identifier for the station.
     * @param name      The name of the station.
     */
    public Station(int idStation, String name) {
        this.time = System.nanoTime();
        this.idStation = idStation;
        this.name = name;
        this.capacity = 10 + (int) (Math.random() * 10);
        this.vehicles = new ArrayList<>();
        this.controlCenter = ControlCenter.getInstance();
    }

    /**
     * Returns the unique identifier of the station.
     *
     * @return The station's ID.
     */
    public int getIdStation() {
        return this.idStation;
    }

    /**
     * Returns the name of the station.
     *
     * @return The station's name.
     */
    public String getName() {
        return this.name;
    }

    /**
     * Returns the maximum capacity of the station.
     *
     * @return The station's capacity.
     */
    public int getCapacity() {
        return this.capacity;
    }

    /**
     * Get the list of vehicles available at the station.
     *
     * @return The list of vehicles at the station.
     */
    public List<Vehicle> getVehicles() {
        return this.vehicles;
    }

    /**
     * Adds a vehicle to the station's inventory.
     *
     * @param vehicle The vehicle to add.
     * @throws StationCapacityExceededException If the maximum station capacity is reached.
     */
    public void addVehicle(Vehicle vehicle) throws StationCapacityExceededException {
        if (vehicles.size() >= capacity) {
            throw new StationCapacityExceededException();
        } else {
            vehicles.add(vehicle);
            vehicle.setState(true);
            time = System.nanoTime();
            System.out.println("The vehicle "+ vehicle.getId() + " is placed at the station "+this.idStation);
        }
    }

    /**
     * Removes a vehicle from the station's inventory.
     *
     * @param vehicle The vehicle to remove.
     * @throws StationEmptyException If you try to remove a vehicle from an empty station.
     */
    public void removeVehicle(Vehicle vehicle) throws StationEmptyException {
        if (vehicles.isEmpty()) {
            throw new StationEmptyException();
        } else {
            vehicles.remove(vehicle);
            vehicle.setState(false);
            time = System.nanoTime();
        }
    }

    /**
     * Checks if the station has no vehicles.
     *
     * @return True if the station has no vehicles, false otherwise.
     */
    public boolean isEmpty() {
        return this.vehicles.isEmpty();
    }

    /**
     * Checks the number of free places in the station.
     *
     * @return The number of free places.
     */
    public int nbPlacesAvailables() {
        return capacity - vehicles.size();
    }

    /**
     * Get the control center.
     *
     * @return The control center.
     */
    public ControlCenter getControlCenter() {
        return this.controlCenter;
    }

    /**
     * Notifies the control center with a boolean if the station is empty or if the size of the station is exceeded after more than 2 turns.
     *
     * @return True if this is the case, False otherwise.
     */
    public boolean notifyControlCenter() {
        if ((this.vehicles.isEmpty() || this.vehicles.size() == this.capacity) && time >= this.controlCenter.getInterval() * 2) {
            return true;
        }
        return false;
    }

    /**
     * Takes a vehicle from the station for repair by a Repairer.
     *
     * @param user The Repairer requesting the vehicle.
     * @return The vehicle taken for repair, or null if the station is empty.
     */
    public Vehicle takeVehicle(Repairer user) {
        if (vehicles.size() == 0) {
            System.out.println("Change the station because this station is empty ");
            return null;
        }
        Iterator<Vehicle> itVehicle = this.vehicles.iterator();

        while (itVehicle.hasNext()) {
            Vehicle vehicle = itVehicle.next();
            if (vehicle.getState()) {
                vehicle.accept(user);
                vehicles.remove(vehicle);
                time = System.nanoTime();
                return vehicle;
            }
        }

        System.out.println("Change the station because this station has no vehicle for you");
        return null;
    }

    /**
     * Takes a vehicle from the station for repair by a Repairer.
     *
     * @param user The User requesting the vehicle.
     * @return The vehicle taken for repair, or null if the station is empty.
     */
    public Vehicle takeVehicle(Worker user) {
        if (vehicles.size() == 0) {
            System.out.println("Change the station because this station is empty ");
            return null;
        }
        Iterator<Vehicle> itVehicle = this.vehicles.iterator();

        while (itVehicle.hasNext()) {
            Vehicle vehicle = itVehicle.next();
            if (vehicle.getState() && !vehicle.getOffService()) { // We check if the vehicle is available (boolean equals to true)
            
                vehicle.accept(user);
                vehicles.remove(vehicle);
                time = System.nanoTime();  
                System.out.println("The user take vehicle "+ vehicle.getId()+"\n");
                return vehicle;
            }
        }

        System.out.println("Change the station because this station has no vehicle for you");
        return null;
    }

    /**
     * Checks the vehicles in the station and sets the condition to true for vehicles with zero locations after more than 2 turns.
     */
    public void checkVehicles() {
        for (Vehicle v : this.vehicles) {
            if (v.getNbLocations() == 0 && time >= this.controlCenter.getInterval() * 2) {
                v.setCondition(true);
            }
        }
    }
}
