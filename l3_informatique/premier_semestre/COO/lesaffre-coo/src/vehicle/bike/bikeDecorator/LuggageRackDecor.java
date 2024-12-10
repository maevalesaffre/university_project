package vehicle.bike.bikeDecorator;

import vehicle.bike.Bike;
import worker.*;

/**
 * A decorator class representing a bicycle with a luggage rack.
 */
public class LuggageRackDecor extends AbstractBikeDecor {

    private int luggageRackCapacity;
    private boolean luggageRackDetached;

    /**
     * Constructs a bicycle with a luggage rack decorator.
     *
     * @param bike The bike to decorate with a luggage rack.
     * @param luggageRackCapacity The capacity of the luggage rack.
     */
    public LuggageRackDecor(Bike bike, int luggageRackCapacity) {
        super(bike);
        this.luggageRackCapacity = luggageRackCapacity;
        this.luggageRackDetached = false;
    }

    /**
     * Get the capacity of the luggage rack.
     *
     * @return The capacity of the luggage rack.
     */
    public int getLuggageRackCapacity() {
        return luggageRackCapacity;
    }

    /**
     * Check if the luggage rack is detached from the bicycle.
     *
     * @return true if the luggage rack is detached, false otherwise.
     */
    public boolean isLuggageRackDetached() {
        return luggageRackDetached;
    }

    /**
     * Set the status of the luggage rack detachment.
     *
     * @param luggageRackDetached true if the luggage rack is detached, false otherwise.
     */
    public void setLuggageRackDetached(boolean luggageRackDetached) {
        this.luggageRackDetached = luggageRackDetached;
    }

    /**
     * Accept a worker for performing specific tasks on the bicycle with a luggage rack.
     * This method invokes the corresponding work method on the provided worker, passing itself as the parameter.
     *
     * @param worker The worker to perform tasks on the bicycle with a luggage rack.
     */
    @Override
    public void accept(Worker worker) {
        worker.work(this);
    }
}
