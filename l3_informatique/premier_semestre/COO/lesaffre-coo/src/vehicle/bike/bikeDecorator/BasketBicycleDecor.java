package vehicle.bike.bikeDecorator;  

import vehicle.bike.Bike;
import worker.*;

/**
 * A decorator class representing a bicycle with a basket.
 */
public class BasketBicycleDecor extends AbstractBikeDecor {

    private int basketCapacity;
	private boolean basketDetached;

    /**
     * Constructs a bicycle with a basket decorator.
     *
     * @param bike The bike to decorate with a basket.
     * @param basketCapacity The capacity of the basket.
     */
    public BasketBicycleDecor(Bike bike, int basketCapacity) {
        super(bike);
        this.basketCapacity = basketCapacity;
        this.basketDetached = false;
    }

    /**
     * Get the capacity of the basket.
     *
     * @return The capacity of the basket.
     */
    public int getBasketCapacity() {
        return basketCapacity;
    }

    /**
     * Check if the basket is detached from the bicycle.
     *
     * @return true if the basket is detached, false otherwise.
     */
    public boolean isBasketDetached() {
        return basketDetached;
    }

    /**
     * Set the status of the basket detachment.
     *
     * @param basketDetached true if the basket is detached, false otherwise.
     */
    public void setBasketDetached(boolean basketDetached) {
        this.basketDetached = basketDetached;
    }

    /**
     * Accept a worker for performing specific tasks on the bicycle with a basket.
     * This method invokes the corresponding work method on the provided worker, passing itself as the parameter.
     *
     * @param worker The worker to perform tasks on the bicycle with a basket.
     */
    @Override
    public void accept(Worker worker) {
        worker.work(this);
    }
}
