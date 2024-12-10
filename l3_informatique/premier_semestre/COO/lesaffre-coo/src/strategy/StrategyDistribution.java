package strategy;

import observer.*;
import vehicle.Vehicle;
import java.util.List;
import exceptions.*;

/**
 * An interface representing a distribution strategy for redistributing vehicles.
 */
public interface StrategyDistribution {

    /**
     * Redistribute vehicles from a source station to other stations.
     *
     * @param vehicles The list of vehicles to be redistributed.
     * @param stations The list of stations to which vehicles are redistributed.
     * @throws StationCapacityExceededException If the maximum station capacity is exceeded during redistribution.
     */
    void redistribute(List<Vehicle> vehicles, List<Station> stations) throws StationCapacityExceededException;
}
