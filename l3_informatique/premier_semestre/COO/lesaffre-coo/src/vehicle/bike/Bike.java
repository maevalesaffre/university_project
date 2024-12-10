package vehicle.bike; 
import observer.ControlCenter;
import vehicle.*;
import worker.Worker;

/**
 * The Bike class represents a bicycle in the vehicle management system.
 * It implements the Vehicle interface to provide information about the bike.
 */
public class Bike implements Vehicle {
    protected int id;
    protected boolean state; // true il est pas pris , false pris 
    protected boolean condition;
    protected boolean offService;
    protected ControlCenter controlCenter;

    protected int nblocations;
    protected static final int  MAXNBLOCATIONS = 2;

    /**
     * Constructor for the Bike class.
     *
     * @param id           The identifier of the bike.
     * @param state        The state of the bike (true if active, false otherwise).
     * @param condition    The condition of the bike (true if in good condition, false otherwise).
     * @param offService   Indicates if the bike is out of service (true if out of service, false otherwise).
     * @param controlCenter Indicates which controlCenter the bike is connected to.
     */
    public Bike(int id, boolean state, boolean condition, boolean offService, ControlCenter controlCenter) {
        this.id = id;
        this.state = state;
        this.condition = condition;
        this.offService = offService;
        this.controlCenter = controlCenter;
        
        this.nblocations = 0;
    }

    /**
     * Get the identifier of the bike.
     *
     * @return The identifier of the bike.
     */
    @Override
    public int getId() {
        return id;
    }

    /**
     * Get the state of the bike.
     *
     * @return true if the state is active, false otherwise.
     */
    @Override
    public boolean getState() {
        return state;
    }

    /**
     * Get the condition of the bike.
     *
     * @return true if in good condition, false otherwise.
     */
    @Override
    public boolean getCondition() {
        return condition;
    }

    /**
     * Get the controlCenter that is connected to the bike.
     *
     * @return the controlCenter corresponding.
     */
    @Override
    public ControlCenter getControlCenter(){
        return controlCenter;
    }

    /**
     * Check if the bike is out of service.
     *
     * @return true if the bike is out of service, false otherwise.
     */
    @Override
    public boolean getOffService() {
        return offService;
    }

    /**
     * get the number of locations
     * @return number of locations
     */
    public int getNbLocations(){
        return this.nblocations;
    }
    
    /**
     * get the max number of locations
     * @return max number of locations
     */
    public int getMaxNbLocations(){
        return Bike.MAXNBLOCATIONS;
    }

    
    /**
     * Set the state of the bike.
     *
     * @param state The new state of the bike (true if active, false otherwise).
     */
    @Override
    public void setState(boolean state) {
        this.state = state;
        notifyObserver();
    }

    /**
     * Set the condition of the bike.
     *
     * @param condition The new condition of the bike (true if in good condition, false otherwise).
     */
    @Override
    public void setCondition(boolean condition) {
        this.condition = condition;
        notifyObserver();
    }

    /**
     * Define which control center the bike is connected to.
     *
     * @param ControlCenter the new control center where the bike is affiliated.
     */
    @Override
    public void setControlCenter(ControlCenter controlCenter) {
        this.controlCenter = controlCenter;
    }

    /**
     * Set the out of service status of the bike.
     *
     * @param offService Indicates if the bike is out of service (true if out of service, false otherwise).
     */
    @Override
    public void setOffService (boolean offService) {
        this.offService = offService;
        notifyObserver();
    }

    /**
     * Notifies if the bike undergoes any change.
     */
    @Override
    public void notifyObserver() {
        controlCenter.update(this);
    }

    /**
     * Accept a worker for performing specific tasks on the bike. This method invokes the corresponding
     * work method on the provided worker, passing itself as the parameter.
     *
     * @param worker The worker to perform tasks on the bike.
     */
    @Override
    public void accept(Worker worker){
        this.AddNbLocations();
        worker.work(this);
    }



    /**
     * add a location for this bike
     */
    public void AddNbLocations(){
        this.nblocations ++;
    }

}
