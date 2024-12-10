package worker;

import vehicle.bike.bikeDecorator.*;
import exceptions.StationCapacityExceededException;
import observer.Station;
import vehicle.bike.*;

/**
 * The Worker interface represents a worker capable of performing various tasks on bikes.
 */
public interface Worker {

    /**
     * Perform work on a basic bike.
     *
     * @param bike The basic bike to perform work on.
     */
    void work(Bike bike);

    /**
     * Perform work on a bike with a basket decoration.
     *
     * @param basketBicycleDecor The bike with a basket decoration to perform work on.
     */
    void work(BasketBicycleDecor basketBicycleDecor);

    /**
     * Perform work on a bike with a luggage rack decoration.
     *
     * @param luggageRackDecor The bike with a luggage rack decoration to perform work on.
     */
    void work(LuggageRackDecor luggageRackDecor);

    /**
     * puts the user's bike into the station
     *
     * @param station the station where the user's bike will be dropped off.
     * @throws StationCapacityExceededException If the maximum station capacity is exceeded when adding the bike.
     */
    public void putInStation(Station station) throws StationCapacityExceededException;
}
