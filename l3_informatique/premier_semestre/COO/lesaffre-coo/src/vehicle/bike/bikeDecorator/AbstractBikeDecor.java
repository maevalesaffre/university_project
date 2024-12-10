package vehicle.bike.bikeDecorator; 

import vehicle.bike.Bike;
import observer.*;
/**
 * An abstract decorator class for decorating a Bike with additional features.
 */
public abstract class AbstractBikeDecor extends Bike {
    private Bike decoratedBike;

    /**
     * Constructs an abstract decorator bike.
     *
     * @param decoratedBike The bike to decorate.
     */
    public AbstractBikeDecor(Bike decoratedBike) {
        super(decoratedBike.getId(), decoratedBike.getState(), decoratedBike.getCondition(), decoratedBike.getOffService(), decoratedBike.getControlCenter());
        this.decoratedBike = decoratedBike;
    }

    /**
     * Get the identifier of the decorated bike.
     *
     * @return The identifier of the decorated bike.
     */
    @Override
    public int getId() {
        return decoratedBike.getId();
    }

    /**
     * Get the state of the decorated bike.
     *
     * @return true if the state is active, false otherwise.
     */
    @Override
    public boolean getState() {
        return decoratedBike.getState();
    }

    /**
     * Get the condition of the decorated bike.
     *
     * @return true if in good condition, false otherwise.
     */
    @Override
    public boolean getCondition() {
        return decoratedBike.getCondition();
    }

    /**
     * Check if the decorated bike is out of service.
     *
     * @return true if the bike is out of service, false otherwise.
     */
    @Override
    public boolean getOffService() {
        return decoratedBike.getOffService();
    }

    /**
     * Get the controlCenter that is connected to the bike.
     *
     * @return the controlCenter corresponding
     */
    @Override
    public ControlCenter getControlCenter(){
        return decoratedBike.getControlCenter();
    }


}
